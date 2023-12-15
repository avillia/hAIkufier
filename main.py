from aiohttp.web import Application, get, static
from aiohttp.web_routedef import post

from configs import STATIC_DIRECTORY_PATH
from handlers.rpc import process_rpc
from handlers.index import index

app = Application()
app.add_routes(
    [
        static("/static", STATIC_DIRECTORY_PATH),
        get("/", index),
        post("/rpc", process_rpc),
    ]
)
