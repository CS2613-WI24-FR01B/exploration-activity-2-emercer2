import colorama 
from colorama import Back, Fore, Style

colorama.init(convert=True)

def printColOp():
    print("Please chose a number from the following list:")
    print("1 - black")
    print("2 - red")
    print("3 - green")
    print("4 - yellow")
    print("5 - blue")
    print("6 - magenta")
    print("7 - cyan")
    print("8 - white")

def setErrorText():
    print("Enter error text colour:")
    printColOp()
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
    printColOp()
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
    printColOp()
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
    printColOp()
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
    
et = setErrorText()
eb = setErrorBack()
st = setSuccessText()
sb = setSuccessBack()


file = input('Enter file name (Enter Q to Quit): ')
while not(file == "Q"):
    try:
        f1 = open(file, "r")
    except:
        print(et + eb + "Error: cannot open " + file + Style.RESET_ALL + "\n")
    else:
        print(st + sb + str(file) + " sucessfully read:" + Style.RESET_ALL)
        print(st + f1.read() + "\n" + Style.RESET_ALL) 
        f1.close()

    file = input('Enter file name (Enter Q to Quit): ')





