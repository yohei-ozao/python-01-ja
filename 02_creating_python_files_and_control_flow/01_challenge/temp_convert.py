def convert():
    # ここにコードを書いてください
    # temp変数を編集し、ユーザー入力として温度を受け取ります。整数に変換することを忘れないでください
    temp = float(input("Enter the temprature:"))
    unit = str(input("Enter the unit:"))
    if (unit == "f"):
        unitc = str("c")
        tempc = (temp - 32) * 5 / 9
        result = str(tempc) + unitc
        print(result)
        temp = tempc
    elif (unit == "c"):
        unitf = str("f")
        tempf = (temp * 9 / 5) + 32
        result = str(tempf) + unitf
        print(result)
        temp = tempf

    return temp


convert()
