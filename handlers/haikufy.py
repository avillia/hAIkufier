from configs import PROMPT_FILE_PATH

with open(PROMPT_FILE_PATH, mode="r", encoding="utf-8-sig") as file:
    PROMPT = file.read().strip()


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

    content = PROMPT

    haiku_title = user_prompt[:50] + "..." if len(user_prompt) > 50 else user_prompt

    return {
        "userPrompt": user_prompt,
        "haikuTitle": haiku_title,
        "processedText": content,
    }
