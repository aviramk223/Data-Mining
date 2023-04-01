# Q1
def my_func(x1,x2,x3):
    if type(x1) == str or type(x2) == str or type(x3) == str:
        return None
    if x1 + x2 + x3 == 0:
        print("Not a number – denominator equals zero")
    elif type(x1) != float or type(x2) != float or type(x3) != float:
        print("Error: parameters should be float")
    else:
        print(((x1 + x2 + x3)*((x3+x2)*x3))/(x1 + x2 + x3))


#Q2
### revword func
def revword(word:str):
    return (word[::-1])
### read file as str
with open(r"C:\\projects\\text.txt", "r") as file:
    data = file.read()

def countword():
    data = open(r"text.text","r")
    count = 1
    for allText in data:
        words_list = allText.split(" ")
        if len(words_list) == 1:
            first_word = words_list[0].lower().strip()
        else:
            for j in words_list:
                word = revword(j).lower().strip()
                if word == first_word:
                    count += 1
    print(count)

countword()



