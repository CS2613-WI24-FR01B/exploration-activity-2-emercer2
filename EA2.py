import colorama 
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

def printTextColOp():
    print("Please chose a number from the following list:")
    print(Fore.BLACK + Back.WHITE + "1 - black")
    print(Fore.RED + "2 - red")
    print(Fore.GREEN + "3 - green")
    print(Fore.YELLOW + "4 - yellow")
    print(Fore.BLUE + "5 - blue")
    print(Fore.MAGENTA + "6 - magenta")
    print(Fore.CYAN + "7 - cyan")
    print(Fore.WHITE + "8 - white")

def printBackColOp():
    print("Please chose a number from the following list:")
    print(Back.BLACK + "1 - black")
    print(Back.RED + "2 - red")
    print(Back.GREEN + "3 - green")
    print(Back.YELLOW + "4 - yellow")
    print(Back.BLUE + "5 - blue")
    print(Back.MAGENTA + "6 - magenta")
    print(Back.CYAN + "7 - cyan")
    print(Back.WHITE + Fore.BLACK + "8 - white")

def printStyleOp():
    print("Please chose a number from the following list:")
    print(Style.DIM + "1 - dim")
    print(Style.NORMAL + "2 - normal")
    print(Style.BRIGHT + "3 - bright")

def setErrorText():
    print("Enter error text colour:")
    printTextColOp()
    errortxt = input('')
    
    match errortxt:
        case "1":
            return Fore.BLACK
        case "2":
            return Fore.RED
        case "3":
            return Fore.GREEN
        case "4":
            return Fore.YELLOW
        case "5":
            return Fore.BLUE
        case "6":
            return Fore.MAGENTA
        case "7":
            return Fore.CYAN
        case "8":
            return Fore.WHITE
        case _:
            setErrorText()

def setErrorBack():
    print("Enter error background colour:")
    printBackColOp()
    errorback = input('')

    match errorback:
        case "1":
            return Back.BLACK
        case "2":
            return Back.RED
        case "3":
            return Back.GREEN
        case "4":
            return Back.YELLOW
        case "5":
            return Back.BLUE
        case "6":
            return Back.MAGENTA
        case "7":
            return Back.CYAN
        case "8":
            return Back.WHITE
        case _:
            setErrorBack()

def setSuccessText():
    print("Enter success text colour:")
    printTextColOp()
    succtxt = input('')

    match succtxt:
        case "1":
            return Fore.BLACK
        case "2":
            return Fore.RED
        case "3":
            return Fore.GREEN
        case "4":
            return Fore.YELLOW
        case "5":
            return Fore.BLUE
        case "6":
            return Fore.MAGENTA
        case "7":
            return Fore.CYAN
        case "8":
            return Fore.WHITE
        case _:
            setSuccessText()

def setSuccessBack():
    print("Enter success background colour:")
    printBackColOp()
    succback = input('')

    match succback:
        case "1":
            return Back.BLACK
        case "2":
            return Back.RED
        case "3":
            return Back.GREEN
        case "4":
            return Back.YELLOW
        case "5":
            return Back.BLUE
        case "6":
            return Back.MAGENTA
        case "7":
            return Back.CYAN
        case "8":
            return Back.WHITE
        case _:
            setErrorBack()

def setStyle():
    print("Enter style:")
    printStyleOp()
    style = input('')

    match style:
        case "1":
            return Style.DIM
        case "2":
            return Style.NORMAL
        case "3":
            return Style.BRIGHT
        case _:
            setErrorBack()

style = setStyle()    
et = setErrorText()
eb = setErrorBack()
st = setSuccessText()
sb = setSuccessBack()


file = input('Enter file name (Enter Q to Quit): ')
while not(file == "Q"):
    try:
        f1 = open(file, "r")
    except:
        print(style + et + eb + "Error: cannot open " + file)
        print()
    else:
        print(style + st + sb + str(file) + " sucessfully read:")
        print(style + st + f1.read()) 
        print()
        f1.close()

    file = input('Enter file name (Enter Q to Quit): ')





