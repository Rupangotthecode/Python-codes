#alphabet checker
def checker(s,c):
    counter=0
    for letter in s:
        if letter in c:
            counter+=1
    if(counter>0):
        print(c,"=>",counter)
sentence=input("Enter a sentence:")
for letter in 'abcdefghijklmnopqrstuvwxyz':
    checker(sentence.lower(),letter)