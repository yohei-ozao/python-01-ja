from tabulate import tabulate
import sys
import math

#表示するメッセージの定義
welcometitle = "Welcome to your personal books digital library!"
flag = "=" * (len(welcometitle) + 1)
confirmselection = "You selected: "
addtitlemessage = "Please input the book title: "
addunreadmessage = "Please input read or unread: "
edittitlemessage = "Please input the book title you want to edit: "
searchtitle = "Please input the book title you want to search: "
deletetitle = "Please input the book title you want to delete: "

# 辞書とリストの初期化
bookshelf = []
id = int()
title = str()
read_status = bool(True)

# Print first description
print(flag)
print(welcometitle)
print(flag)

# 関数を定義
#最初の選択画面の表示とユーザー入力を促す
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
            break
            print(selectcomment)
    return usrinput

#本を追加する関数
def addbook(): 
    while True:
        #本を追加するメッセージ
        print(addtitlemessage)
        title = str(input())
        #既読・未読の正しい入力を判断
        while True:
            print(addunreadmessage)
            read_status_str = str(input())
            if read_status_str != "read" and read_status_str != "unread":
                continue
            else:
                if read_status_str == "read":
                    read_status = True
                    break
                elif read_status_str == "unread":
                    read_status = False
                    break

        idxlen = len(bookshelf) + 1

        #bookshelfが空の場合に入力をインデックス0に配置
        if not bookshelf:
            bookdata = {"id":0, "title":title, "status":read_status}
            bookshelf.append(bookdata)
            for row in bookshelf:
                idlist = [row["id"]]
                titlelist =[row["title"]]
        #bookshelfが空でない場合、空いている一番小さいインデックス番号にデータを配置
        elif len(bookshelf) != 0:
            idlist = [i.get("id") for i in bookshelf]
            titlelist = [i.get("title") for i in bookshelf]
            #bookshelf内に同じタイトルがあった場合は再入力を促す
            for id in range(0, idxlen):
                if (title in titlelist):
                    print("There is a book that is the same title as you entered")
                    break
                #bookshelf内に同じタイトルがなかったらデータを配置
                elif (title not in titlelist and id not in idlist):
                    bookdata = {"id":id, "title":title, "status":read_status}
                    bookshelf.insert(id, bookdata)
                    #elif (id in idlist):
                    #        id = id + 1
        print(tabulate(bookshelf))
        #print(bookshelf) #チェック用
        #print("id is: " + str(id)) #チェック用
        #print("idxlen is: " + str(idxlen)) #チェック用
        return bookshelf

#本を編集する関数
def editbook():
    bookdata = {}
    print(edittitlemessage)
    title = str(input())
    list_search = list(filter(lambda item : item["title"] == title, bookshelf))
    bookdata = list_search[0]
    id = bookdata["id"]
    bookshelf.pop(id)
    #本を追加するメッセージ
    print(addtitlemessage)
    title = str(input())
    #既読・未読の正しい入力を判断
    while True:
        print(addunreadmessage)
        read_status_str = str(input())
        if read_status_str != "read" and read_status_str != "unread":
            continue
        else:
            if read_status_str == "read":
                read_status = True
                break
            elif read_status_str == "unread":
                read_status = False
                break
    bookdata = {"id":id, "title":title, "status":read_status}
    bookshelf.insert(id,bookdata)
    print(tabulate(bookshelf))
    #print(bookdata["id"]) #チェック用
    return

#本を検索する関数
def searchbook(): 
    print(searchtitle)
    title = str(input())
    matching_books = [book for book in bookshelf if title in book["title"]]
    print(tabulate(matching_books))
    return

#本を消去する関数
def deletebook(): 
    bookdata = {}
    print(deletetitle)
    title = str(input())
    list_search = list(filter(lambda item : item["title"] == title, bookshelf))
    bookdata = list_search[0]
    id = bookdata["id"]
    delete_item = bookshelf.pop(id)
    print("Delete: " + str(title))
    return

#統計データを見る関数
def libstats(): 
    read_books = [book for book in bookshelf if book['status'] == True]
    unread_books = [book for book in bookshelf if book['status'] == False]
    print("The number of books in this shelf is: " + str(len(bookshelf)))
    print("The number of read books in this shelf is: " + str(len(read_books)))
    print("The number of unread books in this shelf is: " + str(len(unread_books)))
    return

#bookshelf.pyを修了する関数
def exit(): 
    sys.exit()
    return

#ユーザー入力の初期化
usrinput = int()

#操作選択画面を継続的に表示
while (usrinput != 6):
    usrinput = usrops()
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
    