# File: Project1.py
# Student: Gaytri Riya Vasal
# UT EID: grv377
# Course Name: CS303E
# 
# Date Created: 10/2/2021
# Date Last Modified: 10/8/2021
# Description of Program: The following program will print the calendar for an entered month in the year of 2022.

def main ():

    # Store and validate user input

    while(True):
        num = input("Enter the number of a month [1..12]: ")
        if (int(num) == 1) or (int(num) == 2) or (int(num) == 3) or (int(num) == 4) or (int(num) == 5) or (int(num) == 6) or (int(num) == 7) or (int(num) == 8) or (int(num) == 9) or (int(num) == 10) or (int(num) == 11) or (int(num) == 12):
            break
        else:
            print("  Month must be between 1 and 12. Try again!")

    print()

    #Assign month based on input

    if (int(num) == 1):
        month = "January"
    elif (int(num) == 2):
        month = "February"
    elif (int(num) == 3):
        month = "March"
    elif (int(num) == 4):
        month = "April"
    elif (int(num) == 5):
        month = "May"
    elif (int(num) == 6):
        month = "June"
    elif (int(num) == 7):
        month = "July"
    elif (int(num) == 8):
        month = "August"
    elif (int(num) == 9):
        month = "September"
    elif (int(num) == 10):
        month = "October"
    elif (int(num) == 11):
        month = "November"
    elif(int(num) == 12):
        month = "December"

    #Print month, year, and days of the week

    print("    ", month, "2022    ")
    print("Su Mo Tu We Th Fr Sa")

    #Reach appropriate start column and set columncounter to starting value

    if(month == "January"):
        print("                  ", end="", sep="")
        columncounter = 6
    elif(month == "February"):
        print("      ", end="")
        columncounter = 2
    elif(month == "March"):
        print("      ", end="")
        columncounter = 2
    elif(month == "April"):
        print("               ", end="")
        columncounter = 5
    elif(month == "May"):
        columncounter = 0
    elif(month == "June"):
        print("         ", end="")
        columncounter = 3
    elif(month == "July"):
        print("               ", end="")
        columncounter = 5
    elif(month == "August"):
        print("   ", end="")
        columncounter = 1
    elif(month == "September"):
        print("            ", end="")
        columncounter = 4
    elif(month == "October"):
        print("                  ", end="")
        columncounter = 6
    elif(month == "November"):
        print("      ", end="")
        columncounter = 2
    elif(month == "December"):
        print("            ", end="")
        columncounter = 4

    #Print [1...M] of each month, where M is the number of days corresponding to the entered month

    if(month == "January"):
        #Start on the first of January
        m = 1
        #Print the dates in the first row
        while(columncounter < 7):
            print(format(m, "2d"), "", end="")
            #Proceed to the next date
            m += 1
            #Keep track of columncounter
            columncounter += 1
        #Print the dates in the following rows
        while(True):
            if(columncounter >= 7 and m <= 31):
                #Reset columncounter to 0 once columncounter reaches 7
                columncounter = 0
                print()
                while(columncounter < 7 and m <= 31):
                    print(format(m, "2d"), "", end="")
                    m += 1
                    columncounter += 1
            #Finish loop once all dates have been printed 
            else:
                break

    if(month == "February"):
        m = 1
        while(columncounter < 7):
            print(format(m, "2d"), "", end="")
            m += 1
            columncounter += 1
        while(True):
            if(columncounter >= 7 and m <= 28):
                columncounter = 0
                print()
                while(columncounter < 7 and m <= 28):
                    print(format(m, "2d"), "", end="")
                    m += 1
                    columncounter += 1
            else:
                break

    if(month == "March"):
        m = 1
        while(columncounter < 7):
            print(format(m, "2d"), "", end="")
            m += 1
            columncounter += 1
        while(True):
            if(columncounter >= 7 and m <= 31):
                columncounter = 0
                print()
                while(columncounter < 7 and m <= 31):
                    print(format(m, "2d"), "", end="")
                    m += 1
                    columncounter += 1
            else:
                break

    if(month == "April"):
        m = 1
        while(columncounter < 7):
            print(format(m, "2d"), "", end="")
            m += 1
            columncounter += 1
        while(True):
            if(columncounter >= 7 and m <= 30):
                columncounter = 0
                print()
                while(columncounter < 7 and m <= 30):
                    print(format(m, "2d"), "", end="")
                    m += 1
                    columncounter += 1
            else:
                break

    if(month == "May"):
        m = 1
        while(columncounter < 7):
            print(format(m, "2d"), "", end="")
            m += 1
            columncounter += 1
        while(True):
            if(columncounter >= 7 and m <= 31):
                columncounter = 0
                print()
                while(columncounter < 7 and m <= 31):
                    print(format(m, "2d"), "", end="")
                    m += 1
                    columncounter += 1
            else:
                break

    if(month == "June"):
        m = 1
        while(columncounter < 7):
            print(format(m, "2d"), "", end="")
            m += 1
            columncounter += 1
        while(True):
            if(columncounter >= 7 and m <= 30):
                columncounter = 0
                print()
                while(columncounter < 7 and m <= 30):
                    print(format(m, "2d"), "", end="")
                    m += 1
                    columncounter += 1
            else:
                break

    if(month == "July"):
        m = 1
        while(columncounter < 7):
            print(format(m, "2d"), "", end="")
            m += 1
            columncounter += 1
        while(True):
            if(columncounter >= 7 and m <= 31):
                columncounter = 0
                print()
                while(columncounter < 7 and m <= 31):
                    print(format(m, "2d"), "", end="")
                    m += 1
                    columncounter += 1
            else:
                break

    if(month == "August"):
        m = 1
        while(columncounter < 7):
            print(format(m, "2d"), "", end="")
            m += 1
            columncounter += 1
        while(True):
            if(columncounter >= 7 and m <= 31):
                columncounter = 0
                print()
                while(columncounter < 7 and m <= 31):
                    print(format(m, "2d"), "", end="")
                    m += 1
                    columncounter += 1
            else:
                break

    if(month == "September"):
        m = 1
        while(columncounter < 7):
            print(format(m, "2d"), "", end="")
            m += 1
            columncounter += 1
        while(True):
            if(columncounter >= 7 and m <= 30):
                columncounter = 0
                print()
                while(columncounter < 7 and m <= 30):
                    print(format(m, "2d"), "", end="")
                    m += 1
                    columncounter += 1
            else:
                break

    if(month == "October"):
        m = 1
        while(columncounter < 7):
            print(format(m, "2d"), "", end="")
            m += 1
            columncounter += 1
        while(True):
            if(columncounter >= 7 and m <= 31):
                columncounter = 0
                print()
                while(columncounter < 7 and m <= 31):
                    print(format(m, "2d"), "", end="")
                    m += 1
                    columncounter += 1
            else:
                break

    if(month == "November"):
        m = 1
        while(columncounter < 7):
            print(format(m, "2d"), "", end="")
            m += 1
            columncounter += 1
        while(True):
            if(columncounter >= 7 and m <= 30):
                columncounter = 0
                print()
                while(columncounter < 7 and m <= 30):
                    print(format(m, "2d"), "", end="")
                    m += 1
                    columncounter += 1
            else:
                break

    if(month == "December"):
        m = 1
        while(columncounter < 7):
            print(format(m, "2d"), "", end="")
            m += 1
            columncounter += 1
        while(True):
            if(columncounter >= 7 and m <= 31):
                columncounter = 0
                print()
                while(columncounter < 7 and m <= 31):
                    print(format(m, "2d"), "", end="")
                    m += 1
                    columncounter += 1
            else:
                break

    print("\n", "\n")

main()

