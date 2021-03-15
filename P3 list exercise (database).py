names = []
castes = []
ages = []

n = int(input("How many records you will enter into the database : "))

for i in range(n):

    #   setting positions
    if i == 0:
        position = "1st"
    elif i == 1:
        position = "2nd"
    elif i == 2:
        position = "3rd"

    #   getting values
    name = input("Enter name of the " + position + " person.")
    caste = input("Enter "+ name +"'s caste.")
    age = int(input("Enter "+name+"'s age."))

    #   appending values into the lists
    names.append(name)
    castes.append(caste)
    ages.append(age)


print(names)
print(castes)
print(ages)





