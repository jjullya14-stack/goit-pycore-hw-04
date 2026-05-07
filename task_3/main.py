import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def show_directory_structure(path, indent=""):
    directory = Path(path)

    for item in directory.iterdir():
        if item.is_dir():
            print(indent + Fore.BLUE + f"📂 {item.name}")
            show_directory_structure(item, indent + "    ")
        else:
            print(indent + Fore.GREEN + f"📄 {item.name}")


def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії.")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + "Вказаний шлях не існує.")
        return

    if not path.is_dir():
        print(Fore.RED + "Вказаний шлях не є директорією.")
        return

    print(Fore.YELLOW + f"Структура директорії: {path}")
    show_directory_structure(path)


if __name__ == "__main__":
    main()