from os.path import dirname, join, abspath
from yaml import safe_load, YAMLError


APP_DIRECTORY_PATH = dirname(abspath(__name__))

STATIC_DIRECTORY_PATH = join(APP_DIRECTORY_PATH, "static")

TEMPLATES_DIRECTORY_PATH = join(APP_DIRECTORY_PATH, "templates")
INDEX_PAGE_FILE_PATH = join(TEMPLATES_DIRECTORY_PATH, "index.html")

YAML_FILE_PATH = join(APP_DIRECTORY_PATH, "config.yaml")
PROMPT_FILE_PATH = join(APP_DIRECTORY_PATH, "prompt.txt")


def read_yaml_file_and_extract(config_value: str) -> str:
    try:
        with open(YAML_FILE_PATH, "r") as file:
            data = safe_load(file)
            api_key = data.get(config_value)
            return api_key
    except FileNotFoundError:
        print(f"Error: File '{YAML_FILE_PATH}' not found.")
    except YAMLError as e:
        print(f"Error while parsing YAML: {e}")


OPENAI_API_KEY = read_yaml_file_and_extract("openai_api_key")

DEV_HOST = read_yaml_file_and_extract("dev_host")


if __name__ == '__main__':
    for path in [
        APP_DIRECTORY_PATH,
        PROMPT_FILE_PATH,
        STATIC_DIRECTORY_PATH,
        TEMPLATES_DIRECTORY_PATH
    ]:
        print(path)
