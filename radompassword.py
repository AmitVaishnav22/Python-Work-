import random
import string

passlen=12
charValues=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(passlen):
    password+=random.choice(charValues)

print("Your random password is:",password)
