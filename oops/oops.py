class Person:
    """
    Represents a person with a name and age.  Demonstrates encapsulation
    using getters and setters to control access to the object's internal state.
    """
    def __init__(self, name, age):
        """
        Initializes a Person object.

        Args:
            name: The name of the person (string).  This is stored as a
                  protected attribute (by convention), denoted by the underscore.
            age:  The age of the person (integer). Stored as a protected attribute.

        Attributes:
            _name:  (protected) The person's name.  Should be accessed via the
                    getter and setter to maintain encapsulation.
            _age:   (protected) The person's age.  Should be accessed via the
                    getter and setter.
        """
        self._name = name  # Store the name, marked as protected by convention
        self._age = age    # Store the age, marked as protected by convention

    # Getter for name - Uses the @property decorator
    @property
    def name(self):
        """
        Getter method for the 'name' attribute.  This allows controlled
        access to the name.  It's decorated with @property, allowing access
        as if it were a regular attribute (e.g., person.name).

        Returns:
            The name of the person (string).
        """
        return self._name  # Return the underlying protected attribute

    # Setter for name - Uses the @name.setter decorator
    @name.setter
    def name(self, value):
        """
        Setter method for the 'name' attribute.  This allows controlled
        modification of the name.  It's decorated with @name.setter,
        linking it to the name getter property.  It *also* demonstrates
        validation to ensure the integrity of the data.

        Args:
            value: The new name to set (string).

        Raises:
            TypeError: If the provided value is not a string.
        """
        if not isinstance(value, str):
            raise TypeError("Name must be a string") #Example of input validation.
        self._name = value  # Set the underlying protected attribute

    # Getter for age - Uses the @property decorator
    @property
    def age(self):
        """
        Getter method for the 'age' attribute.  Provides controlled access
        to the person's age.

        Returns:
            The age of the person (integer).
        """
        return self._age

    # Setter for age - Uses the @age.setter decorator
    @age.setter
    def age(self, value):
        """
        Setter method for the 'age' attribute. Demonstrates both type and
        value validation.

        Args:
            value: The new age to set (integer).

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("Age must be an integer") #Example of input validation
        if value < 0:
            raise ValueError("Age cannot be negative") #Example of input validation
        self._age = value

    # Method to describe the person - Regular method (no getter/setter)
    def describe(self):
        """
        A method that describes the person using their name and age.  This
        demonstrates a regular method that operates on the object's attributes.

        Returns:
            A string describing the person.
        """
        return f"This person is named {self.name} and is {self.age} years old."

# Example usage
person = Person("Alice", 30)  # Create a Person object

# Accessing attributes using getters - The @property decorator allows attribute-like access.
print(f"Name: {person.name}") # calls the name() getter method
print(f"Age: {person.age}")   # calls the age() getter method

# Modifying attributes using setters - Similarly, @name.setter/@age.setter enable assignment
person.name = "Bob"  # calls the name() setter method
person.age = 25    # calls the age() setter method

# Calling a method
print(person.describe()) # Calls the describe() method

#Demonstration of validation

try:
    person.age = -5 #This will raise a ValueError because of input validation
except ValueError as e:
    print(f"Error: {e}")

try:
    person.name = 123 #This will raise a TypeError because of input validation
except TypeError as e:
    print(f"Error: {e}")
