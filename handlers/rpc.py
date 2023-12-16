from aiohttp.web_request import Request
from aiohttp.web_response import json_response

from handlers.haikufy import haikufy
from handlers.save_haiku import choose_haiku_variant

method_table = {
    "haikufy": haikufy,
    "saveHaiku": choose_haiku_variant,
}


async def process_rpc(request: Request):
    rpc_call = await request.json()

    method_name: str
    rpc_id: str
    params: list

    method_name, rpc_id, params = rpc_call["method"], rpc_call["id"], rpc_call["params"]

    return json_response(await method_table[method_name](*params))
