from shutil import rmtree
from stat import S_IWRITE
import subprocess
import os
DLN = r"E:\PC\Downloads\New"
DL =  r"E:\PC\Downloads"


def removeReadOnly(func: callable, path: str, _: None) -> None:
    os.chmod(path, S_IWRITE)
    func(path)


def recurse(folderPath: str, lst: list) -> None:
    for file in os.listdir(folderPath):
        ext, filePath = os.path.splitext(file)[1].lower(), fr"{folderPath}\{file}"
        if os.path.isdir(filePath):
            continue
        elif ext in (".zip", ".7z"):
            zipExtractor(filePath)
            continue

        lst[0] += 1
        prefix = f"000{lst[0]}"[-4:] + f" {file}"
        if ext in (".png", ".jpg", ".jpeg", ".gif"):
            os.rename(filePath, fr"{DLN}\{prefix}")
        elif ext == '.jpe':
            os.rename(filePath, fr"{DLN}\{prefix[:-4]}.jpg")
        else:
            os.rename(filePath, fr"{DLN}\Else\{prefix}")

    # Delve deeper into possible subfolders:
    for file in os.listdir(folderPath):
        recurse(fr"{folderPath}\{file}", lst)
    rmtree(folderPath, onerror=removeReadOnly)


def zipExtractor(archivePath: str) -> None:
    if os.path.isdir(dest := os.path.splitext(archivePath)[0]):
        rmtree(dest)
    ret = subprocess.run(fr'"C:\Program Files\7-Zip\7z.exe" x "{archivePath}" -p0 -o"{dest}"',
                         creationflags=subprocess.CREATE_NO_WINDOW,
                         capture_output=True)
    # Good extraction:
    if ret.returncode == 0:
        os.remove(archivePath)
    # Incorrect/No password passed
    elif ret.returncode == 2:
        folderDir, n = archivePath[archivePath.rfind('\\') + 1:], "01"
        if os.path.isdir(dest):
            rmtree(dest)
        while os.path.exists(fr"{DL}\{n}-PASS-{folderDir}"):
            n = f"0{int(n) + 1}"[-2:]
        os.rename(archivePath,
                  fr"{DL}\{n}-PASS-{folderDir}")


def folderManifest() -> None:
    fileNum = 0
    if os.path.isdir(DLN):
        for fileName in reversed(os.listdir(DLN)):
            if fileName == "desktop.ini" or fileName == "Else": continue
            fileNum = int(fileName[:4])
            break
        for fileName in reversed(os.listdir(fr"{DLN}\Else")):
            if fileName == "desktop.ini": continue
            fileNum = max(fileNum, int(fileName[:4]))
            break
    else:
        os.mkdir(DLN)
        os.mkdir(fr"{DLN}\Else")

    folders, archives = [], []
    fileNum = [fileNum]

    for f in os.listdir(DL):
        if not os.path.isdir(fr"{DL}\{f}") or f == "New":
            continue
        folders.append((os.path.getctime(fr"{DL}\{f}"),
                        f))

    for i, f in enumerate(os.listdir(DL)):
        ext = os.path.splitext(f)
        if ext[1].lower() not in (".zip", ".7z", ".rar"):
            continue

        expected, ctime = ext[0], os.path.getctime(fr"{DL}\{f}")
        if os.path.isdir(fr"{DL}\{expected}"):
            expected = f"{i}_{ctime}"
            os.rename(fr"{DL}\{f}",
                      fr"{DL}\{expected}{ext[1]}")

        archives.append((ctime, expected))
        zipExtractor(fr"{DL}\{archives[-1][1]}{ext[1]}")

    folders.extend(archives)
    folders.sort(key=lambda x: x[0])

    for fTuple in folders:
        curFolderPath = fr"{DL}\{fTuple[1]}"
        print(curFolderPath)
        if not os.path.isdir(curFolderPath):
            continue
        recurse(curFolderPath, fileNum)

    if len(os.listdir(DLN)) == 1 and len(os.listdir(fr"{DLN}\Else")) == 0:
        os.rmdir(fr"{DLN}\Else"); os.rmdir(DLN)


if __name__ == "__main__":
    folderManifest()