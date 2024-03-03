from shutil import rmtree
from stat import S_IWRITE
import subprocess
import os
sZip =  r"C:\Program Files\7-Zip\7z.exe"
DL   =  r"E:\PC\Downloads" # DL folder, no rmtree
DLN  = fr"{DL}\New"        # rmtree here, careful with path


def removeReadOnly(func: callable, path: str, _: None) -> None:
    os.chmod(path, S_IWRITE)
    func(path)


def recurse(folderPath: str, lst: list) -> None:
    for file in os.listdir(folderPath):
        ext, filePath = os.path.splitext(file)[1].lower(), fr"{folderPath}\{file}"
        if os.path.isdir(filePath):
            continue
        elif ext in (".zip", ".7z", ".rar", ".cbz"):
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
    ret = subprocess.run(fr'"{sZip}" x "{archivePath}" -p0 -o"{dest}"',
                         creationflags=subprocess.CREATE_NO_WINDOW,
                         capture_output=True)
    # Good extraction:
    if ret.returncode == 0:
        os.remove(archivePath)
    # Incorrect/No password passed:
    elif ret.returncode == 2:
        folderDir, n = archivePath[archivePath.rfind('\\') + 1:], "01"
        if os.path.isdir(dest):
            rmtree(dest)
        while os.path.exists(fr"{DL}\{n}-PASS-{folderDir}"):
            n = f"0{int(n) + 1}"[-2:]
        os.rename(archivePath,
                  fr"{DL}\{n}-PASS-{folderDir}")


def folderManifest() -> None:
    # Retrive file number
    if os.path.isdir(DLN):
        with open(fr"{DLN}\Else\0000 - LOG", 'r') as f:
            fileNum = [int(f.read())]
    else:
        fileNum = [0]
        os.mkdir(DLN)
        os.mkdir(fr"{DLN}\Else")
        with open(fr"{DLN}\Else\0000 - LOG", 'w') as f:
            f.write("0")

    folders, archives = [], []
    toExtract, parts = set(), set()
    for f in os.listdir(DL):
        # Folder Collection
        if os.path.isdir(fr"{DL}\{f}" and f != "New"):
            folders.append((os.path.getctime(fr"{DL}\{f}"), f))

        # Archive Collection
        ext = os.path.splitext(f)
        if ext[1].lower() == ".part":
            parts.add(ext[0])
        elif ext[1].lower() in (".zip", ".7z", ".rar", ".cbz"):
            toExtract.add(f)

    for partFile in parts:
        start = partFile.find('.')
        end   = partFile[start+1:].find('.')
        check = f"{partFile[:start]}{partFile[start + 1 + end:]}"

        if check in toExtract:
            toExtract.remove(check)

    # Retain old ctime and extract archive
    for i, f in enumerate(toExtract):
        ext = os.path.splitext(f)
        expected, ctime = ext[0], os.path.getctime(fr"{DL}\{f}")
        if os.path.isdir(fr"{DL}\{expected}"):
            expected = f"{i}_{ctime}"
            os.rename(fr"{DL}\{f}",
                      fr"{DL}\{expected}{ext[1]}")

        archives.append((ctime, expected))
        zipExtractor(fr"{DL}\{archives[-1][1]}{ext[1]}")

    folders.extend(archives)
    folders.sort(key=lambda x: x[0])

    # Recurse
    for fTuple in folders:
        curFolderPath = fr"{DL}\{fTuple[1]}"
        if not os.path.isdir(curFolderPath):
            continue
        recurse(curFolderPath, fileNum)

    # No moved files, remove empty new folder
    if len(os.listdir(DLN)) == 1 and len(os.listdir(fr"{DLN}\Else")) == 1:
        rmtree(fr"{DLN}")
    # Write file number to log file
    else:
        with open(fr"{DLN}\Else\0000 - LOG", 'w') as f:
            f.write(str(fileNum[0]))


if __name__ == "__main__": folderManifest()