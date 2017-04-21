#!/usr/bin/env python3
import random
import sys
import csv
import operator
from operator import itemgetter


def number1(reader):

        akey = input("please give me appellation: ").upper()#
        d = dict()
        for row in reader:
            d[row[0]] = (row[1],row[2])

            if akey == row[0]:
                print(",".join(d[row[0]]))

            menu = 1



def number2():
    akey = input("Please give me akey: ") #add new artist
    definition = input("Please give me definition: ")
    source = input("Please give me source: ")
    dictwrite = open("dict.csv", "a") # create file to write in the end line
    complete = [akey + ", " + definition + ", " + source + "\n"]
    print(complete) # test
    dictwrite.writelines(complete) #save
    dictwrite.close()
    again = input("What do you want again main menu please insert menu or same menu(1) insert whatever: ").lower()
    if again == "menu":#again
        main()
    else:
        number1()


def number3(reader):
    d = dict()
    for row in reader:
        d[row[0]] = (row[1],row[2])
        #print(d[row[0]])
        sorted_lst = sorted(d, key=str.lower)
    print(", ".join(sorted_lst))
    menu = True


def number4(reader):
    d = dict()
    akey = input("Please put first letter: ").upper()
    if len(akey) == 1 and akey.isalpha():
        for row in reader:
            d[row[0]] = (row[1],row[2])
            if any(akey in row[0] in col for col in row):
                print(row[0]+":"+",".join(d[row[0]]))
    else:
        print("Wrong many letter, please again first letter: ")
        number4(reader)


def main():
    menu = True

    while menu == True:
        menus = ('''Dictionary for a little programmer:
        1) search explanation by appellation
        2) add new definition
        3) show all appellations alphabetically
        4) show available definitions by first letter of appellation
        0) exit''')
        print(menus)
        csvfile = open("dict.csv", "r")   # open cvs and setup csv.reader settings
        csvfile.seek
        upper_stream = (line.upper() for line in csvfile) # Create upper letter
        reader = csv.reader(upper_stream, delimiter=",")
        menu = int(input("please insert number: "))

        if menu == 1:
            number1(reader)
        elif menu == 2:
            number2(reader)
        elif menu == 3:
            number3(reader)
        elif menu == 4:
            number4(reader)
        elif menu == 0:
            sys.exit()

        return reader
main()
