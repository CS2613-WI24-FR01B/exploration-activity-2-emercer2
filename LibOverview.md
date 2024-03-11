# Library Overview - Colorama
## 1. Which package/library did you select? 
For exploration activity 2 I chose the python library [Colorama](https://pypi.org/project/colorama/).

## 2. What is the package/library?
In linux and IOS systems you can color terminal text in python using [ANSI](https://saturncloud.io/blog/how-to-print-colored-text-to-the-terminal/) escape sequences. ANSI escape sequences which use a combination of numbers to set a variaty of different terminal text styles which look like this: '''\033\[30m'''. By adding an ANSI escape sequence to a print statement on Linux and IOS the terminal text is then appropriately styled. Windows systems do not allow the same functionality so easily.<br><br>

Colorama allows Windows users easy access to various terminal text styles that are already present in IOS and Linux systems without affecting the program being run on other systems. Using this library text can be changed in three different ways in a clean easy to use format. The three different ways text can be changed with this library include style, text colour, and background colour. With a variety of two different functioning styles and 8 colours, many text styling combinations are now possible for terminal output. <br><br>

All of these styling options can be accessed through the three variables provided in the Colorama library or ANSI escape sequences. These three variables are Fore, Back, and Style. Fore decides what the text colour will be, Back determines the text background colour, and Style decides the overall text style. All three variables have a reset option as well as the style options they offer.<br><br>

## 3. What are the functionalities of the package/library? **
### • Snippets of code and examples of output should be given here.
To import the mentioned variables your import statement should be formatted like so:<br>

'''import colorama 
from colorama import Back, Fore, Style'''<br>

To use this library you must first initalize with with '''init()''' or '''just_fix_windows_console()''' like so:<br>
'''colorama.init()'''<br>
or<br>
'''colorama.just_fix_windows_console()'''<br>

After this all variables and ANSI escape sequences should style terminal text if applied in a print statements. This will allow you to use ANSI escape sequences or libary variables to style, as the program will call the correct Win32 commands to replicate the results on a Windows machine. To apply a styles simply format the print statement like so:<br><br>

'''print(Fore.GREEN + "hello World" + Style.RESET_ALL)'''<br>

This would return "Hello World" in green text. Where 'Fore.GREEN' is chosing the colour of the text and '''Style.RESET_ALL''' is removing all styling including the text colour. ANSI escape sequences can be applied in a similar mannar using the '''+''' in a print statement. If you want all styling to be removed after each print statement I suggest using the '''init(autoreset=true)''' to initialize Colorama, which will reset the text styling after each print statement.

The styles offered in Colorama variables include:
    - dim (currently non-functioning, appears as normal)
    - normal
    - bright<br>
![Image of background style selection screen](styleChoice.png)
The code used to produce this list:
'''print("Please chose a number from the following list:")
print(Style.DIM + "1 - dim")
print(Style.NORMAL + "2 - normal")
print(Style.BRIGHT + "3 - bright")'''<br>

The colours offered in Colorama variables for text and backgrounds include:
    - Black
    - Red 
    - Green
    - Yellow
    - Blue
    - Magenta
    - Cyan
    - White<br>
![Image of text colour selection screen for success message](textColorChoice.png)<br>
The code used to produce this list:
'''print("Please chose a number from the following list:")
print(Fore.BLACK + Back.WHITE + "1 - black")
print(Fore.RED + "2 - red")
print(Fore.GREEN + "3 - green")
print(Fore.YELLOW + "4 - yellow")
print(Fore.BLUE + "5 - blue")
print(Fore.MAGENTA + "6 - magenta")
print(Fore.CYAN + "7 - cyan")
print(Fore.WHITE + "8 - white")'''<br>
![Image of background colour selection screen for success message](BackColorChoice.png)<br>
The code used to produce this list:
'''print("Please chose a number from the following list:")
print(Back.BLACK + "1 - black")
print(Back.RED + "2 - red")
print(Back.GREEN + "3 - green")
print(Back.YELLOW + "4 - yellow")
print(Back.BLUE + "5 - blue")
print(Back.MAGENTA + "6 - magenta")
print(Back.CYAN + "7 - cyan")
print(Back.WHITE + Fore.BLACK + "8 - white")'''<br><br>

## 4. When was it created?
The latest release of [Colorama](https://pypi.org/project/colorama/) (0.4.6) was released October 24th 2022.

## 5. Why did you select this package/library? 
I chose this library because I felt it could be useful to future python projects where I want my terminal output to have extra clarity. Printing errors in bright red would make them much quicker to identify. I did not how to do this before the exploration activity so it was very fun for me to figure out and discover that it is cooked into base Linux and IOS as I do not have much experience with either of those systems.

## 6. How did learning the package/library influence your learning of the language?
Most of my learning was on the differences between different OS systems. Still it was nice to have a self-motivated project in python where I got to experiement with a few different ways to apply color to terminal text. I got to learn a new way to print out text and variables in python, using literals even though I did not use them in the final project.

## 7. How was your overall experience with the package/library?
This library is great for achieving colorful text on Windows terminals and I will most likely be using it in the near future. The only thing to watch out for is some text editors like VSCode can affect how ANSI characters appear int he terminal, and can cause your code to look like it has no affect. This confused at first for some time, turns out VSCode has a setting to disable and enable ANSI. So just take that as a warning before playing with the library to avoid frustration. 

