while True:
    name = input(" Enter a name? ")
    print(name)
    if name.isalpha():
        print("A name")
        break
    else:
        print("not a name")
