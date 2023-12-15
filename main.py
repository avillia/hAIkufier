from aiohttp.web import Application, get, static

from configs import STATIC_DIRECTORY_PATH
from handlers.index import index

app = Application()
app.add_routes(
    [
        get("/", index),
        static("/static", STATIC_DIRECTORY_PATH, ),
    ]
)
