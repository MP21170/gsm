import os
from dotenv import load_dotenv

# Charger les variables d'environnement du fichier .env
load_dotenv(override=True)

_CHECK_TIME_FORMAT = "%Y-%m-%d %H:%M"
APP_NAME = "Up You!"

#################################################
DEFAULT_ROUTE = "/archives"  # 2ar unused
DEFAULT_ROUTE = "/react"
DEFAULT_ROUTE = "/home"
DEFAULT_ROUTE = "/tests2"
DEFAULT_ROUTE = "/tests"
DEFAULT_ROUTE = "/icons"
DEFAULT_ROUTE = "/calculator"
DEFAULT_ROUTE = "/about"
DEFAULT_ROUTE = "/counter"
#################################################

def get_env(key: str, default=None):
    return os.getenv(key, default)

def _env_int(name: str, default: int = 0) -> int:
    raw = str(os.getenv(name, str(default)) or "").strip()

    if not raw:
        return default

    # Tolère les valeurs de type "1526 # commentaire" dans .env.
    raw = raw.split("#", 1)[0].strip()
    match = re.search(r"[-+]?\d+", raw)
    if not match:
        return default

    try:
        return int(match.group(0))
    except (TypeError, ValueError):
        return default

if __name__ == "__main__":

    w = int(str(get_env("gsm_WINDOW_LEFT", 1912)))
    # print(w)
    print(repr(w))
    # from dotenv import find_dotenv, dotenv_values
    # print(find_dotenv())
    # print(os.environ.get("gsm_WINDOW_LEFT"))
    # print(dotenv_values(".env"))
