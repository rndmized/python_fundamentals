
#Funtion will take a string, format it getting rid of spaces and converting all 
# characters to lower case, then it will reverse the string and compare it to
# itself (not reversed) to chek if it matches or not.
def is_palindrome(word):
    formated_word = str.lower(word.replace(" ",""))
    print(formated_word)
    #Using slices to reverse the word(using the step -1)
    reversed_word = formated_word[::-1]
    if formated_word == reversed_word:
        print('"',word,'"', "is a palindrome.")
    else:
        print(word, "is NOT a palindrome.")

#Test sentence/word
is_palindrome("A Santa dog lived as a devil God at NASA")