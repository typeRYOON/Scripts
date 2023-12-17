from subprocess import run
import os
"""
desktop.inis are within my folders btw.
Directory structure:
Esrgan:
    Executable:
        realesrgan-ncnn-vulkan.exe
        vcomp140.dll
        vcomp140d.dll
        Models:
            realesrgan-x4plus-anime.param
            realesrgan-x4plus-anime.bin
            ...
    Results:
        Input:
            ...
        Output:
            ...
"""


def esrgan() -> None:
    ePath = r"E:\cmder\utils\Esrgan"
    remove = {"desktop.ini", "Executables", "Results"}
    fileQueue = sorted(list(set(os.listdir(ePath)) - remove))

    # Remove non-image files from esrgan queue:
    for i in range(len(fileQueue) - 1, -1, -1):
        if os.path.splitext(fileQueue[i])[1].lower() not in (".png", ".jpg", ".jpeg"):
            fileQueue.pop(i)
    filesLeft = len(fileQueue)
    if not filesLeft:
        return

    # Retrieve file numbers:
    input_Lst = sorted(list(set(os.listdir(fr"{ePath}\Results\Input")) - remove))
    outputLst = sorted(list(set(os.listdir(fr"{ePath}\Results\Output")) - remove))
    input_Num = 1 if not len(input_Lst) else int(input_Lst[-1][:5]) + 1
    outputNum = 1 if not len(outputLst) else int(outputLst[-1][:5]) + 1
    input_Lst.clear()
    outputLst.clear()

    os.chdir(fr"{ePath}\Executable")
    runEsrgan(fileQueue, ePath, input_Num, outputNum)
    filesLeft -= 1; input_Num += 1; outputNum += 1

    menu = f"{chr(10).join(fileQueue)}\n\nContinue?: "
    while filesLeft and (userChoice := input(menu).lower()) not in ('n', 'e'):
        runEsrgan(fileQueue, ePath, input_Num, outputNum)
        menu = f"{chr(10).join(fileQueue)}\n\nContinue?: "
        filesLeft -= 1; input_Num += 1; outputNum += 1


def runEsrgan(fileQueue: list, ePath: str, input_Num: int, outputNum: int) -> None:
    front = fileQueue.pop(0); ext = os.path.splitext(front)[1]
    os.system("cls")
    command = (r"realesrgan-ncnn-vulkan.exe",
               "-i", fr"{ePath}\{front}",
               "-o", fr"{ePath}\Results\Output\{f'0000{outputNum}'[-5:]}_O{ext}",
               "-n", "realesrgan-x4plus-anime")
    run(command)
    os.system("cls")
    os.rename(fr"{ePath}\{front}",
              fr"{ePath}\Results\Input\{f'0000{input_Num}'[-5:]}_I{ext}")


if __name__ == "__main__":
    try:
        esrgan()
    except Exception as e:
        input(e)
