from multiprocessing import get_logger


from database.models.supabase import SupabaseClient

logger = get_logger()


def upload_file_storage(file, file_identifier: str):
    supabase_client = SupabaseClient()
    storage = supabase_client.storage("transcribed-audio-files")
    # res = supabase_client.storage.create_bucket("transcribed-audio-files")
    response = None

    try:
        response = storage.upload(file_identifier, file)
        return response
    except Exception as e:
        logger.error(e)
        raise e
