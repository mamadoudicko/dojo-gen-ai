import os

from supabase.client import create_client

supabase_url = os.environ["SUPABASE_URL"]
supabase_key = os.environ["SUPABASE_KEY"]


def save_question_and_response(question, answer):
    supabase_client = create_client(supabase_url, supabase_key)

    supabase_client.table("history").insert(
        {"question": question, "answer": answer}
    ).execute()
