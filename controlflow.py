age = 10
if age < 18:
    print("your not an adult ")

elif age >= 18 and age <= 65: 
    print("your an adult")   
else:
    print("our a senior citizen ")

#loops
#loops (for, while)
#for loop

# lakes = ["Victoria", "Chala", "Nakuru", "Bogoria", "Naivasha", "Turkana", "Baringo", "Magadi", "Jipe", "Ellmentaita", "Logipi", "Rudolf"]
# for lake in lakes:
#     print(lake)


#while loop, executes code as long as a certAIN CONDITION IS TRUE
lakes = ["Victoria", "Chala", "Nakuru", "Bogoria", "Naivasha", "Turkana", "Baringo", "Magadi", "Jipe", "Ellmentaita", "Logipi", "Rudolf"]
count = 0
while count < len(lakes):
    print(lakes[count])
    count = count + 1

