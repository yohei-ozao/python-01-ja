import os


def ls_command(directory):
    # ユーザー入力が「sample」の場合、ディレクトリは「sample」になります
    # 無効なディレクトリパスについて考える必要はありません

    # 「pass」を削除して、ここにコードを書いてください
    import collections
    ext = []
    directory_path = directory
    files = os.listdir(directory_path)
    files = sorted(files)
    # ファイル名から拡張子を取り出し、それをカウントする辞書
    extension_count = {}

    for file in files:
        # '.'で分割し、最後の要素を拡張子とする
        extension = "." + file.split('.')[-1]

        # 辞書に拡張子がまだ存在しない場合は、新たにキーを作成し、カウントを1にする
        if extension not in extension_count:
            extension_count[extension] = 1
        # 辞書に拡張子がすでに存在する場合は、カウントを1増やす
        else:
            extension_count[extension] += 1
    #print(extension_count)
    #print(files) 
    print("Summary in alphabetical order:")
    for key,value in extension_count.items():
        if int(value) == 1:
            print(str(key) + ":" + str(value) + " file")
        elif int(value) >= 2:
            print(str(key) + ":" + str(value) + " files")
    
    return


if __name__ == "__main__":
    directory_path = input("Enter directory path to organize files: ")

    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
    else:
        ls_command(directory_path)
