# Strings are immutable
a = "!!!Harry!! !!!!!!!!! Harry"
print(len(a))
print(a)
print(a.upper()) # upper case
print(a.lower()) # lower case
print(a.rstrip("!")) # removes ending !
print(a.replace("Harry", "John")) # replaces the string
print(a.split(" ")) # splits in space part and make its list
blogHeading = "introduction tO jS"
print(blogHeading.capitalize()) # makes capitsl the first letter of eah word

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50))) # alings to center 
print(a.count("Harry")) # counts the no of times harry comes in a

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # only alfabet and numbers
str1 = "Welcome"
print(str1.isalpha()) # only alphabet

str1 = "hello world"
print(str1.islower()) # lowercase true

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())