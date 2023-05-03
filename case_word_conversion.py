def Case_Word(Word):
    new = ""
     
    for i in range(0, len(Word)):
        if Word[i].islower():
            new += Word[i].upper()
        elif Word[i].isupper():
            new += Word[i].lower()

        else:
            new += Word[i]
    print("String after case conversion : " +new)

Case_Word("babababablacksheep")

