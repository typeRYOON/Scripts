from os.path import isdir, isfile
from colorama import init
from os import getcwd
CYAN, RESET = "\x1b[38;2;210;255;251m", "\u001b[0m"
SRC = r"E:\PC\Downloads\Pather\\"   # Pather folder path.


class Neko:
    def __init__(s):
        s.FileName = fr"{SRC}dirs.txt"
        s.CHDIR = getcwd()
        s.Dirs = s.readFile()
        s.Menus = dict()
        s.Same = True
        s.EndPage = 1

    def readFile(s) -> list:
        if not isfile(s.FileName): return []
        with open(s.FileName, 'r', encoding="utf-8") as f:
            ret = [tuple(l.strip().split(',')) for l in f]
        return ret

    def writeFile(s) -> None:
        with open(s.FileName, 'w', encoding="utf-8") as f:
            for tup in s.Dirs: f.write(f"{tup[0]},{tup[1]}\n")

    def sortTup(s, t: tuple) -> int:
        return len(t[0])

    def menusCreate(s) -> None:
        Z = [s.Dirs[i:i + 20] for i in range(0, len(s.Dirs), 20)]
        if not len(Z): s.Menus[1] = f"""\033c  \x1b[38;2;0;0;0m\x1b[48;2;253;255;210mPather\Page-1{RESET}

 ▀▀▀▀\n  >> {CYAN}"""
        i = 0
        for page, tupArr in enumerate(Z, start=1):
            target = list()
            target.append(f"\033c  \x1b[38;2;0;0;0m\x1b[48;2;253;255;210mPather\Page-{page}{RESET}\n")
            for tup in tupArr: target.append(f"  {f' {(i := i+1)}'[-2:]}▐ {tup[0]}")
            target.append(f" ▀▀▀▀\n  >> {CYAN}")
            s.Menus[page] = '\n'.join(target)
            s.EndPage = page


def remainsSplit(R: list) -> bool:
    inComma, start, end = False, 0, -1
    remains = R[0]; R.clear()

    if '"' not in remains: R.append(remains)
    for i, chr in enumerate(remains):
        if chr != '"': continue
        if not inComma:
            inComma, start = True, i
        else:
            inComma, end = False, i
            R.append(remains[start+1:end])
    if inComma: return False
    return True


def menu(NEKO: "Neko") -> None:
    NEKO.menusCreate()
    z = 1

    while True:
        Choice = input(NEKO.Menus[z]).strip()

        # Turn page:
        if not len(Choice):
            if (z := z + 1) == NEKO.EndPage + 1: z = 1
            continue

        # Split:
        Remains = None if (i := Choice.find(' ')) == -1 else [Choice[i + 1:]]
        Choice = Choice.lower() if i == -1 else Choice[:i].lower()
        if Remains and not remainsSplit(Remains):
            continue

        # CHDIR Selection:
        if Choice.isdigit() and 20*(z-1) < int(Choice) <= min(20*z, len(NEKO.Dirs)):
            Choice = int(Choice)
            NEKO.CHDIR = NEKO.Dirs[Choice - 1][1]
            break

        # Exit:
        elif Choice == 'e':
            break

        # Retrieve last dir:
        elif Choice == "last":
            with open(fr"{SRC}last.txt", 'r', encoding="utf-8") as f:
                NEKO.CHDIR = f.read()
            break

        # Entry Addition:
        elif Choice == "add" and Remains and len(Remains) == 2:
            if Remains[1].lower() == "cwd": Remains[1] = getcwd()
            if not isdir(Remains[1]): continue
            if Remains[0][-1] != '.': Remains[0] = f"{Remains[0]}."
            if Remains[1].endswith('\\') and Remains[1][-2:] != "\\\\":
                Remains[1] += '\\'

            NEKO.Dirs.append(tuple(Remains))
            NEKO.Dirs.sort(key=NEKO.sortTup, reverse=True)
            NEKO.Same, z = False, 1
            NEKO.menusCreate()
            continue

        # Entry Deletion
        elif Choice == "del" and Remains and Remains[0].isdigit():
            if not (20*(z-1) < int(Remains[0]) <= min(20*z, len(NEKO.Dirs))): continue

            NEKO.Dirs.pop(int(Remains[0]) - 1)
            NEKO.Same, z = False, 1
            NEKO.menusCreate()
            continue

    if not NEKO.Same: NEKO.writeFile()
    with open(fr"{SRC}run.py", 'w', encoding="utf-8") as f:   f.write(f"print(r'{NEKO.CHDIR}')")
    with open(fr"{SRC}last.txt", 'w', encoding="utf-8") as f: f.write(getcwd())


if __name__ == "__main__":
    init()
    menu(Neko())
    print('\033c', end='')
