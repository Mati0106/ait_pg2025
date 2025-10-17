# Example 1: Simple Class with __init__ and __str__ Methods

class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"


# Create an instance of MyClass
obj = MyClass("Alice")

# Call the __str__ method implicitly
print(obj)


# In this example, __init__ is called when an instance of MyClass is created, and __str__ is called when the object is converted to a string(e.g., with print).

# Example 2: Class with __add__ Method


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


# Create two Point objects
point1 = Point(1, 2)
point2 = Point(3, 4)

# Call the __add__ method implicitly
result = point1 + point2
print(f"Resultant Point: ({result.x}, {result.y})")


# In this example, __add__ enables us to use the + operator with instances of the Point class.

# Example 3: Class with __len__ Method


class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)


# Create an instance of MyList
my_list = MyList([1, 2, 3, 4, 5])

# Call the __len__ method implicitly
length = len(my_list)
print("Length of MyList:", length)


# Here, __len__ allows us to use the len() function with instances of the MyList class.

# Example 4: Class with __getitem__ Method for Indexing
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]


# Create an instance of MyList
my_list = MyList([1, 2, 3, 4, 5])

# Access elements using indexing
print("First element:", my_list[0])
print("Last element:", my_list[-1])


# In this example, __getitem__ allows us to use indexing to access elements of the MyList class.
# Example 5: Class with __iter__ and __next__ Methods for Iteration
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


# Create an instance of MyIterator
my_iterator = MyIterator([1, 2, 3, 4, 5])

# Iterate over the elements using a for loop
for item in my_iterator:
    print(item)


# Here, __iter__ and __next__ enable iteration over instances of the MyIterator class.
#
# Example 6: Class with __contains__ Method for Membership Testing
class MyContainer:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        return item in self.data


# Create an instance of MyContainer
my_container = MyContainer([1, 2, 3, 4, 5])

# Test membership using the 'in' operator
print(3 in my_container)
print(6 in my_container)
# In this example, __contains__ allows us to use the in operator to test membership in instances of the MyContainer class.
