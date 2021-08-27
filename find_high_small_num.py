# create an empty List
NumList = []

# Take the input from the User
Number = int(input("Enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Enter the Value of %d Element: " % i))
    NumList.append(value)

# Print the List Entered by the User
print("\nList: ", NumList)

smallest = largest = NumList[0]

for j in range(1, Number):
    if(smallest > NumList[j]):
        smallest = NumList[j]
        min_position = j
    if(largest < NumList[j]):
        largest = NumList[j]
        max_position = j

print("The Smallest Element in this List is: ", smallest)
print("The Index position of Smallest Element in this List is: ", min_position)
print("The Largest Element in this List is: ", largest)
print("The Index position of Largest Element in this List is: ", max_position)
