#!/usr/bin/env python3


import sys
import os
import site


if __name__ == "__main__":
    path_venv = os.environ.get("VIRTUAL_ENV")
    if path_venv:
        print("MATRIX STATUS: Welcom to the construct")
        path_python = sys.executable
        name_venv = os.path.basename(path_venv)
        print(f"Current Python: {path_python}")
        print(f"Virtual Environment: {name_venv}")
        print(f"Environment Path: {path_venv}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install package without affecting the global system")
        print()
        path_install = site.getsitepackages()[0]
        print("Package installation path:")
        print(f"{path_install}")
    else:
        print("MATRIX STATUS: You're still plugges in")
        print()
        path_python = sys.executable
        print(f"Current Python: {path_python}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machine can see everything you install")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")
