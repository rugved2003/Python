def string_test(s):
    d={"UPPER_CASE":0, "lower_case":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["lower_case"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["lower_case"])

string_test('BaBa BaBa Black Sheep')