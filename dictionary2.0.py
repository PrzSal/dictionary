#!/usr/bin/env python3
import random
import sys
import csv
import operator
def print_menu():
    menus = ('''Dictionary for a little programmer:
    1) search explanation by appellation
    2) add new definition
    3) show all appellations alphabetically
    4) show available definitions by first letter of appellation
    0) exit''')
    print(menus)
    return menus


def number1(reader):
    akey = input("please give me appellation: ").upper()
    d = {}
    for row in reader:
        d[row[0]] = (row[1],row[2])

        if akey == row[0]:
            print(",".join(d[row[0]]))
            loop = True
    print("Wrong appellation, return to main menu")


def number2(reader, row):
    d = {}
    akey = input("please give me appellation: ").upper()
    for row in reader:
        d[row[0]] = (row[1],row[2])
        print(row[0])
        if akey == row[0]:
            print("I know this appellation")
            number2(reader, row)
    if akey != row[0]:
        definition = input("Please give me definition: ")
        source = input("Please give me source: ")
        dictwrite = open("dict1.csv", "a") # create file to write in the end line
        complete = [akey + ", " + definition + ", " + source + "\n"]
        dictwrite.writelines(complete) #save
        dictwrite.close()
        loop = True
    return row

def number3(reader):
    d = dict()
    for row in reader:
        d[row[0]] = (row[1],row[2])
        sorted_lst = sorted(d, key=str.lower)
    print(", ".join(sorted_lst))
    loop = True


def number4(reader):
    d = dict()
    akey = input("Please put first letter: ").upper()
    if len(akey) == 1 and akey.isalpha():
        for row in reader:
            d[row[0]] = (row[1],row[2])
            if any(akey in row[0] in col for col in row):
                print(row[0]+":"+",".join(d[row[0]]))
                loop = True
    else:
        print("Wrong many letter, please again first letter: ")
        number4(reader)


def main():
    loop =True

    while loop:
        row = []
        csvfile = open("dict1.csv", "r")   # open cvs and setup csv.reader settings
        csvfile.seek
        upper_stream = (line.upper() for line in csvfile) # Create upper letter
        reader = csv.reader(upper_stream, delimiter=",")
        print_menu()
        choice = int(input("Enter your menu[1-4]: "))
        if choice == 1:
            print("menu 1")
            number1(reader)
        elif choice == 2:
            number2(reader, row)
        elif choice == 3:
            number3(reader)
        elif choice == 4:
            number4(reader)
        elif choice == 0:
            sys.exit()
    return reader

main()
