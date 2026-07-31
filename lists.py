#Create an empty list
emptyList = []
print()

# A list of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Use * operator
triples = [1, 2, 3] * 3
print(triples)

#reverse the given list
aList = [100, 200, 300, 400, 500]
aList = aList[::-1]
print(aList, "\n")


# function to check whether
# first and last character of words match
def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of words with first and last character same:", lst)
    return ctr

l= [3,6,2,5,12,11,10,4]

count = match_words(["abc", "cfc", "xyz", "aba", "1221"])
print("Number of words having first and last character same:", count)


print("Original list:", l)

# variable to store the sum of
# the list
count = 0

# Finding the sum
for i in l:
    count += i

# divide the total elements by
# number of elements
avg = count / len(l)

print("Sum =", count)
print("Average =", avg)

# Sorting the elements of the list
l.sort()

# printing the first element
print("Smallest element is:", l[0])

# printing the last element
print("Largest element is:", l[-1])