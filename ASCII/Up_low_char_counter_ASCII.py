lf="Hello, Mr.Rogers"
def let_count(x):
    up_count = 0
    low_count = 0
    for letter in x:
        if ord(letter) in range(65,91):
            up_count+=1
        elif ord(letter) in range(97,123):
            low_count+=1
    print("Upper case letters = "+str(up_count))
    print("Lower case letters = "+str(low_count))

let_count(lf)

for x in range(33,63):
    print("{} - {}".format(x,chr(x)))