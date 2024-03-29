import numpy
import random
import math

welcometitle = "Welcome to your personal books digital library!"
flag = "=" * (len(welcometitle) + 1)
confirmselection = "You selected: "
addtitlemessage = "Please input the book title: "
addunreadmessage = "Please input read or unread: "


# Define dict and status
bookshelf = []
bookdata = {}
read_status_data = {}
id = int()
title = str()
read_status = bool(True)

# Print first description
print(flag)
print(welcometitle)
print(flag)

# Define funciton
def usrops():
    while True:
        # User input
        selecitonlist = ("", "1: Add a Book", "2: Edit a Book", "3: Search for Books", "4: Delte a Book", "5: Videw Library Stats", "6: Exit app", )
        lsadd = int(1)
        lsedit = int(2)
        lssearch = int(3)
        lsdelete = int(4)
        lsstats = int(5)
        lsexit = int(6)
        selectcomment = "Please select from 1 to 6"
        print(selecitonlist[lsadd])
        print(selecitonlist[lsedit])
        print(selecitonlist[lssearch])
        print(selecitonlist[lsdelete])
        print(selecitonlist[lsstats])
        print(selecitonlist[lsexit])
        print(selectcomment)

    
        usrinput = input()
        if (usrinput.isdecimal()) and (int(usrinput) >= 1 and int(usrinput) <= 7):
            usrinput = int(usrinput)
            print(confirmselection + selecitonlist[usrinput])
            return usrinput
            break
        print(selectcomment)

def addbook():
    print(addtitlemessage)
    title = str(input())
    while (True):
        print(addunreadmessage)
        read_status = str(input())
        if (read_status == "read" or read_status == "unread"):
            read_status = read_status
            break
    id = int(0)
    #print(bookdata)
    idxlen = len(bookshelf) + 1
    print("id is: " + str(id))
    print("idxlen is: " + str(idxlen))
    for id in range (id, idxlen):
        if (id not in bookdata):
            bookdata[id] = {title:read_status}
            bookshelf.insert(id, bookdata)
            print(bookshelf)
        break
        
    return

def editbook():
    return

def searchbook():
    return

def deletebook():
    return

def libstats():
    return

usrinput = usrops()

while (usrinput != 6):
    if usrinput == 1:
        addbook()
    elif usrinput == 2:
        editbook()
    elif usrinput == 3:
        searchbook()
    elif usrinput == 4:
        deletebook()
    elif usrinput == 5:
        libstats()
    elif usrinput == 6:
        exit()
    usrinput = usrops()