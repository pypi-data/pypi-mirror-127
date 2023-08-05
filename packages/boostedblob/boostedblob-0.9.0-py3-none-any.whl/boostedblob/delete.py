import asyncio
import os
import shutil
from typing import AsyncIterator, Optional, Union

from .boost import BoostExecutor, consume
from .listing import glob_scandir, listtree
from .path import AzurePath, BasePath, CloudPath, GooglePath, LocalPath, isdir, isfile, pathdispatch
from .request import Request, azure_page_iterator, azurify_request, googlify_request

# ==============================
# remove
# ==============================


@pathdispatch
async def remove(path: Union[BasePath, str]) -> BasePath:
    """Delete the file ``path``.

    :param path: The path to delete.

    """
    raise ValueError(f"Unsupported path: {path}")


@remove.register  # type: ignore
async def _azure_remove(path: AzurePath) -> AzurePath:
    request = await azurify_request(
        Request(
            method="DELETE",
            url=path.format_url("https://{account}.blob.core.windows.net/{container}/{blob}"),
            success_codes=(202,),
            failure_exceptions={404: FileNotFoundError(path)},
        )
    )
    try:
        await request.execute_reponseless()
    except FileNotFoundError:
        # Note that this continues to allow the deletion of directory marker files
        if await isdir(path):
            raise IsADirectoryError(path) from None
        raise
    return path


@remove.register  # type: ignore
async def _google_remove(path: GooglePath) -> GooglePath:
    request = await googlify_request(
        Request(
            method="DELETE",
            url=path.format_url("https://storage.googleapis.com/storage/v1/b/{bucket}/o/{blob}"),
            success_codes=(204,),
            failure_exceptions={404: FileNotFoundError(path)},
        )
    )
    try:
        await request.execute_reponseless()
    except FileNotFoundError:
        # Note that this continues to allow the deletion of directory marker files
        if await isdir(path):
            raise IsADirectoryError(path) from None
        raise
    return path


@remove.register  # type: ignore
async def _local_remove(path: LocalPath) -> LocalPath:
    os.remove(path)
    return path


# ==============================
# glob_remove
# ==============================


async def glob_remove(
    path: Union[BasePath, str], executor: BoostExecutor
) -> AsyncIterator[BasePath]:
    """Delete all files that match the glob ``path``.

    :param path: The glob to match against.
    :param executor: An executor.

    """
    async for subpath in executor.map_unordered(
        lambda x: remove(x.path), executor.eagerise(glob_scandir(path))
    ):
        yield subpath


# ==============================
# rmtree
# ==============================


async def rmtree_iterator(path: CloudPath, executor: BoostExecutor) -> AsyncIterator[BasePath]:
    """Delete the directory ``path``.

    Yields the deleted paths as they are deleted.

    :param path: The path to delete.
    :param executor: An executor.

    """
    # Note that this function almost works for LocalPath, except that we wouldn't remove empty
    # directories. To get this to work, we'd need a variant of scantree that also yields
    # directories, ensuring they're in the right order. This would also allow us to get rid of the
    # current directory file marker special casing.
    dirpath = path.ensure_directory_like()

    # listtree will not list the directory itself, so we need to remove the marker file if present
    async def remove_directory_marker() -> Optional[BasePath]:
        try:
            return await remove(dirpath)
        except (FileNotFoundError, IsADirectoryError, PermissionError):
            return None

    marker_task = asyncio.create_task(remove_directory_marker())

    try:
        async for subpath in executor.map_unordered(remove, executor.eagerise(listtree(dirpath))):
            yield subpath
    except FileNotFoundError:
        if await isfile(path):
            raise NotADirectoryError(path)
        raise

    marker = await marker_task
    if marker:
        yield marker


@pathdispatch
async def rmtree(path: Union[BasePath, str], executor: BoostExecutor) -> None:
    """Delete the directory ``path``.

    :param path: The path to delete.
    :param executor: An executor.

    """
    raise ValueError(f"Unsupported path: {path}")


@rmtree.register  # type: ignore
async def _cloud_rmtree(path: CloudPath, executor: BoostExecutor) -> None:
    await consume(rmtree_iterator(path, executor))


@rmtree.register  # type: ignore
async def _local_rmtree(path: LocalPath, executor: BoostExecutor) -> None:
    shutil.rmtree(path)


# ==============================
# undelete
# ==============================


async def _azure_undelete_tree(path: Union[str, AzurePath], executor: BoostExecutor) -> None:
    """Experimental code to undelete blobs. It should work, but e.g. doesn't have tests."""
    if isinstance(path, str):
        path = AzurePath.from_str(path)

    it = azure_page_iterator(
        Request(
            method="GET",
            url=path.format_url("https://{account}.blob.core.windows.net/{container}"),
            params=dict(comp="list", restype="container", prefix=path.blob, include="deleted"),
        )
    )

    deleted_blobs = []
    async for result in it:
        blobs = result["Blobs"]
        if blobs is None:
            continue
        if "Blob" in blobs:
            if isinstance(blobs["Blob"], dict):
                blobs["Blob"] = [blobs["Blob"]]
            for b in blobs["Blob"]:
                if not b.get("Deleted", False):
                    continue
                # maybe get DeletedTime, RemainingRetentionDays
                blob = b["Name"]
                path = AzurePath(path.account, path.container, blob)
                deleted_blobs.append(path)

    # Not sure if this is true, especially in the presence of versioning / overwrites
    assert len(deleted_blobs) == len(set(deleted_blobs))

    # We might want to eagerise deleted_blobs
    async for blob in executor.map_unordered(_azure_undelete, iter(deleted_blobs)):
        # And turn this into an async iterator, instead of printing
        print(f"Undeleted {blob}")


async def _azure_undelete(path: AzurePath) -> AzurePath:
    request = await azurify_request(
        Request(
            method="PUT",
            url=path.format_url("https://{account}.blob.core.windows.net/{container}/{blob}"),
            params=dict(comp="undelete"),
            success_codes=(200,),
        )
    )
    await request.execute_reponseless()
    return path
