from get_env import get_env
import os

print(get_env("UPU_WINDOW_LEFT", 555))
print(os.environ.get("FLET_RUNNING"))

if __name__ == "__main__":

    if os.environ.get("FLET_RUNNING") != "1":
        import subprocess

        env["FLET_RUNNING"] = "1"
        subprocess.run(["flet", "run", "src/upu/helpers/quick_test.py"])
