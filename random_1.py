import random

chsnce = random.randint(1, 2)
if chsnce == 1:
    print("heads")
else:
    print("tails")

names = input("give me every bodys name , separate by a coma ? ")
names_ = names.split(", ")
print(names_)

payer = random.randint(0, len((names_))-1)
print(names_[payer])

# you can use random.choice() method.
