import os
import platform
from scripts import colors
c = colors


logo = f"""
██╗    ██╗██╗      ███████╗██╗            
██║    ██║██║      ██╔════╝██║            
██║ █╗ ██║██║█████╗█████╗  ██║            
██║███╗██║██║╚════╝██╔══╝  ██║            
╚███╔███╔╝██║      ██║     ██║            
 ╚══╝╚══╝ ╚═╝      ╚═╝     ╚═╝            
                                          
██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗  
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
                          {c.c + "Author: "+c.y+"Saad Khan"}                                                                                                                                   
"""
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")


def banner():
    print(c.ran + logo)
    print(c.ran + '-'*63)
    print("|" + "*"* 60 + c.ran + "|")

    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3+c.ran + "|")
    print(c.ran + "\n"+ "|" + "*" * 60+c.ran + "|")

    print(c.ran + '-' * 63)


def banner2():
    print(c.ran + '-'*63)
    print("|" + "*"* 60 + c.ran + "|")

    print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4 + c.ran + "|")
    print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4+c.ran + "|")
    print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3+c.ran + "|")
    print(c.ran + "\n"+ "|" + "*" * 60+c.ran + "|")

    print(c.ran + '-' * 63)

def clear():
    s = platform.platform()
    if "Windows" in s:
        os.system("cls")
    else:
        os.system("clear")
