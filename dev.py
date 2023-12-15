from aiohttp.web import run_app

from configs import DEV_HOST
from main import app

if __name__ == '__main__':
    run_app(app, host=DEV_HOST)
