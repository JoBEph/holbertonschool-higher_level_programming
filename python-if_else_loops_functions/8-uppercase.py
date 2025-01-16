def uppercase(str):
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            result += chr(ord(x) - 32)
            print("{}".format(result))
        print()
