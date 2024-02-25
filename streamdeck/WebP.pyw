from PIL import Image
import os


def webp() -> None:
    dPath = r"E:\PC\Downloads"
    for file in os.listdir(dPath):
        ext = os.path.splitext(file)
        if ext[1].lower() != ".webp":
            continue
        with Image.open(fr"{dPath}\{file}") as img:
            img.save(fr"{dPath}\{ext[0]}.png", "png")
        os.remove(fr"{dPath}\{file}")


if __name__ == "__main__":
    webp()