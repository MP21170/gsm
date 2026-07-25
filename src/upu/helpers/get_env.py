import os
from dotenv import load_dotenv

# Charger les variables d'environnement du fichier .env
load_dotenv(override=True)


def get_env(key: str, default=None):
    return os.getenv(key, default)


if __name__ == "__main__":

    from dotenv import find_dotenv, dotenv_values

    w = int(str(get_env("UPU_WINDOW_LEFT", 1912)))
    # print(w)
    print(repr(w))
    # print(find_dotenv())
    # print(os.environ.get("UPU_WINDOW_LEFT"))
    # print(dotenv_values(".env"))
