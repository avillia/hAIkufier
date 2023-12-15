from logging import basicConfig as BasicLogging
from logging import DEBUG

from aiohttp.web import run_app

from configs import DEV_HOST
from main import app

if __name__ == '__main__':
    BasicLogging(level=DEBUG)
    run_app(app, host=DEV_HOST, port=8080)
