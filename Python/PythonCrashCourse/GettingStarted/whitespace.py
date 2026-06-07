#To add a tab to your text, use the combination \t as shown below:
print("Python")
print("\tPython")

#To add a new line in your text, use the combination \n as shown below:
print("Python")
print('Languages:\nPython\nC\nJavaScript')

#Tabs and new lines into a single string:
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Whitespace can be stripped to the left or right of a string:
favorite_language = '  python  '
print(favorite_language.rstrip()) #Removes whitespace to the right of the string
print(favorite_language.lstrip()) #Removes whitespace to the left of the string
print(favorite_language.strip()) #Removes whitespace to the left and right of the string
#This only removes whitespace temporarily. To permanently remove whitespace, you can assign the stripped value back to the variable:
favorite_language = favorite_language.strip()
print(favorite_language)


