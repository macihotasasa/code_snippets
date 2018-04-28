lf="Hello Rogers and welcome to our test party friend"
def spin_words(sentence):
    kort = sentence.split(" ")
    ort=list([])
    for x in kort:
        if len(x)>=5:
            x=x[::-1]
            ort.append(x)
        else:
            ort.append(x)
    baba=" ".join(ort)
    return str(baba)


print(spin_words(lf))
