# Step 1: Define the Person class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # Method to introduce the person
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I identify as {self.gender}.")
# Step 2: Create an instance of the Person class
person_instance = Person("Darius", 25, "Male")

# Step 3: Call the introduce method to display the person's information
person_instance.introduce()
