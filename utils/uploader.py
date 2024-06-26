from utils.clients import get_client
from pyrogram import Client
from pyrogram.types import Message
from config import STORAGE_CHANNEL
import os
from utils.logger import Logger

logger = Logger("Uploader")
PROGRESS_CACHE = {}
STOP_TRANSMISSION = []


async def progress_callback(current, total, id, client: Client):
    global PROGRESS_CACHE, STOP_TRANSMISSION

    PROGRESS_CACHE[id] = ("running", current, total)
    if id in STOP_TRANSMISSION:
        client.stop_transmission()


async def start_file_uploader(file_path, id, directory_path, filename, file_size):
    global PROGRESS_CACHE
    from utils.directoryHandler import DRIVE_DATA

    logger.info(f"Uploading file {file_path} {id}")

    if file_size > 1.98 * 1024 * 1024 * 1024:
        # Use premium client for files larger than 2 GB
        client: Client = get_client(premium_required=True)
    else:
        client: Client = get_client()

    PROGRESS_CACHE[id] = ("running", 0, 0)

    message: Message = await client.send_document(
        STORAGE_CHANNEL,
        file_path,
        progress=progress_callback,
        progress_args=(id, client),
    )
    size = (message.document or message.audio).file_size

    DRIVE_DATA.new_file(directory_path, filename, message.id, size)
    PROGRESS_CACHE[id] = ("completed", size, size)

    os.remove(file_path)
    logger.info(f"Uploaded file {file_path} {id}")
