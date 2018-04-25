print("Enter the list range:")
# Get the range value from the user and stored it to list_range
list_range = input()
# store your list under mylist
mylist = []
print("Enter the list value:")
# for entering list value one by one
for i in range(int(list_range)):

    # Get list values from user

    list = input()
    # sore the value in mylist using "append"
    mylist.append(list)

print("The original lists are:",mylist)
# calculating min, max and sum of values
print("Min value in list:",min(mylist))
print("max value in list:",max(mylist))








