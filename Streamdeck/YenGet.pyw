from pyperclip import copy, paste
from requests import get as rGet
from sys import argv

def convertToNumber() -> float:
    val = paste().upper().replace(',', '').replace(' ', '')
    val = val.replace('円', '').replace('¥', '').replace("$", '')
    val = val.replace("JPY", '').replace("YEN", '').replace("USD", '')

    if 'K' in val:
        parts = val.split('K')
        if len(parts) == 2 and parts[0].replace('.', '', 1).isdigit() and parts[1] == '':
            return float(parts[0]) * 0x3E8

    elif 'M' in val:
        parts = val.split('M')
        if len(parts) == 2 and parts[0].replace('.', '', 1).isdigit() and parts[1] == '':
            return float(parts[0]) * 0xF4240

    elif val.isdigit() or val.count('.') == 1:
        return float(val)

    return -1.0

def yenGet(vType: str) -> None:
    if (val := convertToNumber()) < 0:
        return

    y = rGet("https://www.google.com/search?client=firefox-b-1-d&q=usd+to+yen").text
    y = float(y[y.index("Japanese Yen") - 7:y.index(" Japanese Yen")])

    copy(f"{(val / y):.2f} USD" if vType == '0' else f"{(val * y):.2f} JPY")

if __name__ == "__main__" and len(argv) == 2:
    yenGet(argv[1])