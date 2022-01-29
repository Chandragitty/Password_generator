import string , random
for i in range(1):
    upletter=string.ascii_uppercase
    print(random.choice(upletter),end="")
for i in range(5):
    letter=string.ascii_lowercase
    print(random.choice(letter),end="")
for i in range(2):
    dig=string.digits
    print(random.choice(dig),end="")
for i in range(2):
    pun=string.punctuation
    print(random.choice(pun),end="")
