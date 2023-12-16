from string import ascii_letters, digits
from random import choice as random_choice

from configs import PROMPT_FILE_PATH
from db import save_to_db

with open(PROMPT_FILE_PATH, mode="r", encoding="utf-8-sig") as file:
    PROMPT = file.read().strip()


def generate_random_string(length: int):
    characters = ascii_letters + digits
    random_string = "".join(random_choice(characters) for _ in range(length))
    return random_string


async def haikufy(user_prompt: str) -> dict:
    # response: ChatCompletion = openai_client.chat.completions.create(
    #   model="gpt-3.5-turbo-1106",
    #   messages=[{"role": "user", "content": PROMPT.format(user_prompt)}],
    #   temperature=0.7,
    #   max_tokens=64,
    #   top_p=1
    # )
    # choice = response.choices[0]
    # message = choice.message
    # content = message.content

    haiku_id = generate_random_string(8)

    choices = ["\n".join(generate_random_string(16) for _ in range(3)) for _ in range(3)]

    haiku_variants = {generate_random_string(8): choice for choice in choices}

    save_to_db(haiku_id, {"user_prompt": user_prompt, "haiku_variants": haiku_variants})

    haiku_title = user_prompt[:50] + "..." if len(user_prompt) > 50 else user_prompt

    data = {
        "haikuId": haiku_id,
        "haikuData": {
            "userPrompt": user_prompt,
            "haikuTitle": haiku_title,
            "haikuVariants": [{"id": key, "text": haiku_variants[key]} for key in haiku_variants]
        },
    }

    return data
