from get_env import get_env
import os

print(get_env("UPU_WINDOW_LEFT", 555))

if __name__ == "__main__":

    # print('Flet is' , ('running' if os.environ.get("FLET_RUNNING") else 'not yet started'))
    if os.environ.get("FLET_RUNNING") != "1":
        import subprocess

        os.environ["FLET_RUNNING"] = "1"
        subprocess.run(["flet", "run", "src/upu/helpers/quick_test.py"])
