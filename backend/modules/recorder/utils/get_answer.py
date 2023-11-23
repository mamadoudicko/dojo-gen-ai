import os

import openai

from backend.modules.recorder.utils.get_previous_messages import get_previous_messages
from backend.modules.recorder.utils.get_relevant_chunks import get_relevant_chunks

openai.api_key = os.environ["OPENAI_API_KEY"]


def get_answer(question: str):
    context = get_relevant_chunks(question)
    history = get_previous_messages()

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant which answer questions about the audio recorded by the user and given to you as context.",
        },
        {"role": "user", "content": f"Context: {context}"},
    ]

    for message in history:
        messages.append({"role": "user", "content": message["question"]})
        messages.append({"role": "assistant", "content": message["answer"]})

    messages.append({"role": "user", "content": f"{question}"})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    return response["choices"][0]["message"]["content"]
