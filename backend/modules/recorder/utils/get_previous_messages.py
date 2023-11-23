import os

from supabase.client import create_client

supabase_url = os.environ["SUPABASE_URL"]
supabase_key = os.environ["SUPABASE_KEY"]


def get_previous_messages():
    """
    Get the previous messages from the database.
    """
    supabase_client = create_client(supabase_url, supabase_key)

    response = (
        supabase_client.table("history")
        .select("*")
        .order("created_at", desc=False)
        .execute()
    )

    return response.data
