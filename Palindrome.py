#Palindrome
n=input("Enter your word: ")
rev=(n[::-1])
if rev==n:
    print("The word is palindrome")
else:
    print("The word is not pallindrome") 
