from multiprocessing import get_logger

from database.models.supabase import SupabaseClient

logger = get_logger()

SIGNED_URL_EXPIRATION_PERIOD_IN_SECONDS = 600


def generate_file_signed_url(path):
    supabase_client = SupabaseClient()
    storage = supabase_client.storage("transcribed-audio-files")

    try:
        response = storage.create_signed_url(
            path,
            SIGNED_URL_EXPIRATION_PERIOD_IN_SECONDS,
            options={
                "download": True,
                "transform": None,
            },
        )
        logger.info("RESPONSE SIGNED URL", response)
        return response
    except Exception as e:
        logger.error(e)
