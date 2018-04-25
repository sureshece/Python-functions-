# Function for removing the duplicates
def dublicates(dub):
    dub = []
    for each in my_list:
        if each not in dub:
            dub.append(each)
    return dub


# storing the list
print ("Enter 7 numbers with some dublicates")
my_list = []
for list in range(7):
    list = input()
    my_list.append(list)
print("my list", my_list)
# By calling the function named "duplicates" to get the values
print ("With out dublicates:", dublicates(my_list))
