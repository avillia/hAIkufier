from aiohttp.web_request import Request
from aiohttp.web_response import json_response

from configs import PROMPT_FILE_PATH

with open(PROMPT_FILE_PATH, mode="r", encoding="utf-8-sig") as file:
    PROMPT = file.read().strip()


async def haikufy(request: Request):
    user_prompt: str = (await request.json())["text"]

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

    content = PROMPT

    haiku_title = user_prompt[:50] + "..." if len(user_prompt) > 50 else user_prompt

    return json_response(data={"userPrompt": user_prompt, "haikuTitle": haiku_title, "processedText": content})
