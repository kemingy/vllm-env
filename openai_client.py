from random import randint
import concurrent.futures

import openai

openai.api_key = "EMPTY"
openai.api_base = "http://localhost:8000/v1"


def query(max_tokens=20):
    chat = openai.ChatCompletion.create(
        model="mosaicml/mpt-30b-chat",
        messages=[{
            "role": "user",
            "content": "Who are you?",
        }],
        stream=True,
        max_tokens=max_tokens,
    )
    for result in chat:
        delta = result.choices[0].delta
        print(delta.get('content', ''), end='', flush=True)
    print()


def batch_test():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(query, max_tokens=randint(20, 200)) for _ in range(20)
        ]
        for future in concurrent.futures.as_completed(futures):
            future.result()


if __name__ == "__main__":
    query(100)
