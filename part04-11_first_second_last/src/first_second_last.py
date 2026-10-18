# Write your solution here
# You can test your function by calling it within the following block
def first_word(word1):
    i =0
    while True:
       
        if word1[i] == " ":
        
            break
        i+=1
    return word1[0:i]
def second_word(word):
    i =0
    while True:
        if word[i] == " ":
            break
        i+=1
    j= i+1
    while True:
        if word[j] == " " or word[j] == word[len(word)-1]:
            break
        j+=1
    return word[i+1:j]
def last_word(word):
   i = len(word)-1
   k=i
   while True:
       if word[k]== " ":
           break
       k-=1
   return word[k+1:i+1]

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word("first second"))
    print(last_word(sentence))