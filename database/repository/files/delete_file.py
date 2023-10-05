from multiprocessing import get_logger

from database.models.supabase import SupabaseClient

logger = get_logger()


def delete_file_from_storage(file_identifier: str):
    supabase_client = SupabaseClient()
    storage = supabase_client.storage("transcribed-audio-files")

    try:
        response = storage.remove([file_identifier])
        return response
    except Exception as e:
        logger.error(e)
        raise e
