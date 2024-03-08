[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/RPDAFNpj)
# Exploration Activity 2 Readme - Colorama

## 1. Which package/library does the sample program demonstrate?
In exploration activity 2, I demonstrate features offered by the most recent version of the python library Colorama.

## 2. How does someone run your program?
For this program please ensure your have python installed on your computer before performing the following steps. 
First download the code from [the GitHub repository](https://github.com/CS2613-WI24-FR01B/exploration-activity-2-emercer2).
There are two files to note in this repository, 1.An example text file that can be used to test the program and, 2.The python program. ![Immage of EA2.py python program, and file.txt example file in code editor](filesInEditor.png)
Second to run the python programm you will need to install colorama using pip install in the terminal, 'pip install colorama'. 
After this you can run the program through the terminal using 'python EA2.py'.

## 3. What purpose does your program serve?
This program allows windows users to experiement with coloured text through the terminal. My program asks the users to set the text and background colours they would like for success and error messages. Then the program tries to open a given file and uses the colours specified when printing if the file was successfully opened.

## 4. What would be some sample input/output?
The program will walk you through setting colours for error and success text and background. There are four colours for the user to set, error text, error background, success text, and success background. Each colour has a similar prompt to one of the following:
![Image of text color selection screen for success message](textColorChoice.png)
![Image of background color selection screen for success message](BackColorChoice.png)
[!Note]
The expected input is one of the 8 numbers listed, if input does not match the user will be reprompted.
After all four colours are selected the user will be asked to give a file name.
![Image of program requesting a file name from user](requestFileName.png)

If the file name exists in the directory a success message and the file contents are printed in the appropriate colours.

Otherwise a error message will appear with the appropriate colours applied.
Either way the user will then be asked be asked to enter another file name until they enter "Q" as the file name.

For example, 