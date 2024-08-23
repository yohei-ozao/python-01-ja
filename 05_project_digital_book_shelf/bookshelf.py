from tabulate import tabulate
import sys

# 表示するメッセージの定義
welcometitle = "Welcome to your personal books digital library!"
flag = "=" * (len(welcometitle) + 1)
confirmselection = "You selected: "
addtitlemessage = "Please input the book title: "
addunreadmessage = "Please input read or unread: "
editidmessage = "Please input the book ID you want to edit: "
deleteidmessage = "Please input the book ID you want to delete: "
searchtitlemessage = "Please input the title or part of the title you want to search for: "

# 辞書とリストの初期化
bookshelf = []
id_counter = 0

# Print first description
print(flag)
print(welcometitle)
print(flag)

# 関数を定義
# 最初の選択画面の表示とユーザー入力を促す
def usrops(): 
    while True:
        # User input
        selectionlist = ("", "1: Add a Book", "2: Edit a Book", "3: Search for Books", "4: Delete a Book", "5: View Library Stats", "6: Exit app")
        lsadd = 1
        lsedit = 2
        lssearch = 3
        lsdelete = 4
        lsstats = 5
        lsexit = 6
        selectcomment = "Please select from 1 to 6"
        for i in range(1, len(selectionlist)):
            print(selectionlist[i])
        print(selectcomment)
    
        usrinput = input()
        if usrinput.isdecimal() and 1 <= int(usrinput) <= 6:
            usrinput = int(usrinput)
            print(confirmselection + selectionlist[usrinput])
            break
        else:
            print(selectcomment)
    return usrinput

# 本を追加する関数
def addbook():
    global id_counter
    print(addtitlemessage)
    title = input()
    while True:
        print(addunreadmessage)
        read_status = input()
        if read_status in ["read", "unread"]:
            break
        else:
            print("Please enter 'read' or 'unread'.")
    
    bookdata = {"id": id_counter, "title": title, "status": read_status}
    bookshelf.append(bookdata)
    id_counter += 1
    print(tabulate(bookshelf, headers="keys"))
    return bookshelf

# 本を編集する関数
def editbook():
    print(editidmessage)
    book_id = int(input())
    book = next((item for item in bookshelf if item["id"] == book_id), None)
    if book:
        print(f"Editing book: {book}")
        print(addtitlemessage)
        new_title = input()
        while True:
            print(addunreadmessage)
            new_status = input()
            if new_status in ["read", "unread"]:
                break
            else:
                print("Please enter 'read' or 'unread'.")
        book["title"] = new_title
        book["status"] = new_status
        print("Book updated successfully.")
    else:
        print("Book ID not found.")
    print(tabulate(bookshelf, headers="keys"))
    return bookshelf

# 本を検索する関数
def searchbook():
    print(searchtitlemessage)
    search_term = input().lower()
    result = [book for book in bookshelf if search_term in book["title"].lower()]
    if result:
        print("Search results:")
        print(tabulate(result, headers="keys"))
    else:
        print("No books found.")
    return result

# 本を消去する関数
def deletebook():
    print(deleteidmessage)
    book_id = int(input())
    global bookshelf
    new_bookshelf = [book for book in bookshelf if book["id"] != book_id]
    if len(new_bookshelf) != len(bookshelf):
        bookshelf = new_bookshelf
        print("Book deleted successfully.")
    else:
        print("Book ID not found.")
    print(tabulate(bookshelf, headers="keys"))
    return bookshelf

# 統計データを見る関数
def libstats():
    total_books = len(bookshelf)
    read_books = len([book for book in bookshelf if book["status"] == "read"])
    unread_books = total_books - read_books
    print(f"Total books: {total_books}")
    print(f"Read books: {read_books}")
    print(f"Unread books: {unread_books}")
    return

# bookshelf.pyを終了する関数
def exitapp():
    sys.exit()

# ユーザー入力の初期化
usrinput = int()

# 操作選択画面を継続的に表示
while usrinput != 6:
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
        exitapp()