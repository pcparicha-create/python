# create class
class IOString():

    # constructor to set default value
    def __init__(self):
        self.str1 = ""

    # function to get input from user
    def get_String(self):
        self.str1 = input("Enter String: ")

    # function to print the string in upper case
    def print_String(self):
        print("Result is :", self.str1.upper())


# Object creation
str1 = IOString()

# Call functions
str1.get_String()
str1.print_String()


# Create class
class Employee:

    # Initializing
    def __init__(self):
        print("Employee created")

    # Calling destructor
    def __del__(self):
        print("Destructor called")


def create_obj():
    print("Making object...")
    obj = Employee()
    print("Function end...")
    return obj


print("Calling create_obj() function...")
obj = create_obj()
print("Program end...")


# create a class
class pair_elements:

    def __init__(self, nums, target):
        # create an empty dictionary
        lookup = {}

        # iterate through the tuple
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i


# take input of data from the user
value = int(input("Enter sum for which you want to make this search: "))
print("Index-Index:", pair_elements([10, 20, 20, 30, 40], value))

