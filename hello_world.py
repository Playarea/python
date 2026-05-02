#print("Hello World")
import string

char = 'W'
message = "Hello World"
print(message)
print("Is W in message : ")
print(char in message)
print("First char is: " + message[0])

for i in range(0,len(message)):
    print(message[i])

print("Another way to print this message:")
for ch in message:
    print(ch)

print("ASCII Letters : " + string.ascii_letters)
print("UPPERCASE : " +  string.ascii_uppercase)
print("lowercase : " +  string.ascii_lowercase)
print("Digits : " + string.digits)
print("Punctuation : " + string.punctuation)

vowel_string = 'aeiouAEIOU'
test_char = 'a'
print( test_char in vowel_string)
print(f" Is char 'a' in vowel_string: + {test_char in vowel_string}")
print(char.isalpha())
print(message.split())



