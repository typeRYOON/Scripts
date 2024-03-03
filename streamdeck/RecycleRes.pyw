from winshell import recycle_bin


def main() -> None:
    rBin = list(recycle_bin())
    if not rBin: return
    r = max(rBin, key=lambda item: item.recycle_date())
    try:   r.undelete()
    except Exception as e: print(e)


if __name__ == "__main__": main()