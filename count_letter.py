def count_letter(word,letter):
    for i in word:
        if i == letter:
            print(word.count(letter))
        break
count_letter("BaBa BaBa Black Sheep",'B')