import os

import openai

openai.api_key = os.environ["OPENAI_API_KEY"]


def get_answer(question: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant which answer questions about the audio recorded by the user and given to you as context.",
            },
            {"role": "user", "content": f"{question}"},
        ],
    )

    return response["choices"][0]["message"]["content"]
