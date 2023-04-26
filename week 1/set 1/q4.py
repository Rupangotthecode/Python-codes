#vowels in a word
word=input("Enter the word: ")
vow=0
vow_percent=0
for letter in word:
    if letter in 'aeiouAEIOU':
        vow+=1
    
vow_percent=(vow/len(word))*100
print("Number of vowels in word=",vow)
print("Vowel percentage={:.2f}".format(vow_percent))