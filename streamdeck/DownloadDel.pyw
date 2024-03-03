from send2trash import send2trash
import os


def main() -> None:
    DL  = r"E:\PC\Downloads"
    DLL = [f for f in os.listdir(DL) if os.path.splitext(f)[1].lower() not in (".ini", '')]
    DLL.sort(key=lambda x: os.path.getctime(fr"{DL}\{x}"), reverse=True)
    while DLL:
        recent = DLL.pop(0)
        if recent == "New": continue
        break
    else:
        return
    send2trash(fr"{DL}\{recent}")


if __name__ == "__main__": main()