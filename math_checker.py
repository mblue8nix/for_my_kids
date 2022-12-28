#! /usr/local/bin/python3
'''
mblue
Math-checker is a simple program to check my kids math without giving them the answer
before they get it corrrect. If they fail to answer the correct answer three times the program
will quit and tell them to get help from adult.
'''


kids_name = ""  # you can put kids name as my kid loves seeing his \
                # name on correct answers.


operation = str(input('Type in the math operation \n ie. +, * , /, -: '))


if (operation !='+' and operation !='-' and operation!='*' and operation!='/'):
    print("You need to add an operator like *")

else:

    first_number = int(input('\nType the first number: '))
    second_number = int(input('Type the second number: '))
    print("\n", first_number, operation, second_number, " = ?\n")
    your_answer = int(input('What was your answer: '))

    problem_set = print("\n",first_number, operation, second_number, ":") 

    if operation == '+':
        math_answer = first_number + second_number
        problem_set

    elif operation == '-':
        math_answer = first_number - second_number
        problem_set

    elif operation == '*':
        math_answer = first_number * second_number
        problem_set

    elif operation == '/':
        math_answer = first_number / second_number
        problem_set


    if your_answer == math_answer:
        print("\n The Answer is :", math_answer, "\n Great Job", kids_name, "!\n You get: ***** \n")

    else:
        print("\nYour answer is wrong, try again...\n")
        your_answer = int(input('Enter your new answer: '))

        if your_answer == math_answer:
            print("\nThe answer is:", math_answer, "\nGreat Job, you got it!\n")
        else:
            print("\nNot correct. You have one more try!\n")
            your_answer = int(input('Enter your new answer: '))

            if your_answer == math_answer:
                print("\n The answer is:", math_answer,"\nGreat Job Bud, you got it!\n")
            else:
                print("\n Not correct. It's OK.\n Please get help and then re-enter your \
variables and try again. \n You Got This!")
