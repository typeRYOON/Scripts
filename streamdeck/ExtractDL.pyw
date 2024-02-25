from shutil import rmtree
import subprocess
import os
DL = r"E:\PC\Downloads"


def zipExtractor(archivePath: str) -> None:
    if os.path.isdir(dest := os.path.splitext(archivePath)[0]):
        rmtree(dest)
    ret = subprocess.run(fr'"C:\Program Files\7-Zip\7z.exe" x "{archivePath}" -p0 -o"{dest}"',
                         creationflags=subprocess.CREATE_NO_WINDOW,
                         capture_output=True)
    # Good extraction:
    if ret.returncode == 0: os.remove(archivePath)

    # Incorrect/No password passed
    elif ret.returncode == 2:
        folderDir, n = archivePath[archivePath.rfind('\\') + 1:], "01"

        if os.path.isdir(dest): rmtree(dest)
        while os.path.exists(fr"{DL}\{n}-PASS-{folderDir}"):
            n = f"0{int(n) + 1}"[-2:]
        os.rename(archivePath,
                  fr"{DL}\{n}-PASS-{folderDir}")


def looper() -> None:
    types = (".zip", ".7z", ".rar")
    archives = [f for f in os.listdir(DL) if os.path.splitext(f.lower())[1] in types]
    archives.sort(key=lambda x: os.path.getctime(fr"{DL}\{x}"))
    for folder in archives:
        zipExtractor(fr"{DL}\{folder}")


if __name__ == "__main__":
    looper()