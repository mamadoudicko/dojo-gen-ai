import logging
import os

from dotenv import load_dotenv
from pydantic import BaseSettings
from supabase.client import Client, create_client


class SupabaseClient(BaseSettings):
    client: Client

    def __init__(self):
        load_dotenv()  # load environment variables from .env file
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_service_key = os.getenv("SUPABASE_SERVICE_KEY")
        if supabase_url is None or supabase_service_key is None:
            logging.error(
                "SUPABASE_URL or SUPABASE_SERVICE_KEY is not set in the .env file."
            )
            return

        supabase_client: Client = create_client(supabase_url, supabase_service_key)
        return supabase_client

    def storage(self, storage_name: str):
        return self.client.storage.from_(storage_name)
