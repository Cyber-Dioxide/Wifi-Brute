import os

try:
    from colorama import Style, Fore

except ModuleNotFoundError:
    os.system("pip install colorama")
import random

all_col= [Style.BRIGHT+Fore.RED,Style.BRIGHT+Fore.CYAN,Style.BRIGHT+Fore.LIGHTCYAN_EX, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)

lg = Style.BRIGHT+Fore.LIGHTGREEN_EX
g = Style.BRIGHT+Fore.GREEN
lc = Style.BRIGHT+Fore.LIGHTCYAN_EX
c = Style.BRIGHT+Fore.CYAN
ly =  Style.BRIGHT+Fore.LIGHTYELLOW_EX
y = Style.BRIGHT+Fore.YELLOW
r = Style.BRIGHT+Fore.RED
lr = Style.BRIGHT+Fore.LIGHTRED_EX