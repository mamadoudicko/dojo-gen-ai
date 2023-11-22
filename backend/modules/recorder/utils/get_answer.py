import os

import openai

from backend.modules.recorder.utils.get_relevant_chunks import get_relevant_chunks

openai.api_key = os.environ["OPENAI_API_KEY"]


def get_answer(question: str):
    context = get_relevant_chunks(question)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant which answer questions about the audio recorded by the user and given to you as context.",
            },
            {"role": "user", "content": f"Context: {context}"},
            {"role": "user", "content": f"{question}"},
        ],
    )

    return response["choices"][0]["message"]["content"]
