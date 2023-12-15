from aiohttp.web_request import Request
from aiohttp.web_response import Response

from configs import INDEX_PAGE_FILE_PATH


with open(INDEX_PAGE_FILE_PATH, mode="r", encoding="utf-8-sig") as file:
    INDEX_PAGE_TEMPLATE = file.read().strip()


async def index(request: Request):
    web_page = INDEX_PAGE_TEMPLATE.format(
        "/static/styles.css", "/static/scripts.js",
    )
    return Response(
        text=web_page,
        content_type='text/html'
    )
