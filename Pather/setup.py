from os import remove
from os.path import isdir


def setup() -> None:
    print('\n Place the "Pather" folder where you would like.\n')
    pDir = input(" Enter the Pather folder path :: ").strip().replace('"', '')
    if not pDir.endswith("Pather") or not isdir(pDir):
        print(f"\n Invalid path :: {pDir}")
        return

    for path in ("menu.py", "run.py", "Pather.bat"):
        with open(path, 'r', encoding="utf-8") as f: c = f.read()
        with open(path, 'w', encoding="utf-8") as f:
            c = c.replace("@@@", pDir)
            f.write(c)
    c = c.replace("@@@", pDir)
    with open(r"Pather.bat", 'w', encoding="utf-8") as f:
        c = c.replace("@@@", pDir)
        f.write(c)

    print("\n Make sure the Pather.bat file is accessible via the PATH system variable.")

    try:                 remove("setup.py")
    except OSError as e: input(f"Error deleting setup file ::\n\t{e}")


if __name__ == "__main__": setup()