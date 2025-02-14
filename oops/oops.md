# Object-Oriented Programming (OOP) Concepts

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. OOP involves four main principles: **Encapsulation**, **Inheritance**, **Polymorphism**, and **Abstraction**. Below, we'll explain each of these concepts with code examples from **Python**, **Java**, and **VB.NET**.

---

## 1. Encapsulation

Encapsulation is the concept of restricting access to certain details of an object's internal state. It is typically achieved using **private** or **protected** attributes and provides **getters** and **setters** for controlled access.

### Python Example:
In Python, we use **getter** and **setter** methods to manage access to attributes.

```python
class Person:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age    # Protected attribute

    @property
    def name(self):
        return self._name  # Getter

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value  # Setter

    @property
    def age(self):
        return self._age  # Getter

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value  # Setter

# Example usage
person = Person("Alice", 30)
print(person.name)  # Calls the getter
person.name = "Bob"  # Calls the setter
```
### Java Example:
In Java, we achieve **encapsulation** using **private fields** and **public getter** and **setter methods**.

```java
public class Person {
    private String name;  // Private attribute
    private int age;      // Private attribute

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;  // Getter
    }

    public void setName(String name) {
        if (name == null || name.isEmpty()) {
            System.out.println("Name cannot be null or empty");
            return;
        }
        this.name = name;  // Setter
    }

    public int getAge() {
        return age;  // Getter
    }

    public void setAge(int age) {
        if (age < 0) {
            System.out.println("Age cannot be negative");
            return;
        }
        this.age = age;  // Setter
    }
}
```

### VB.NET example: 
In VB.NET, we use **Private fields** and **Public Properties** to control access to data.
``` vbnet
Public Class Person
    Private _name As String  ' Private attribute
    Private _age As Integer  ' Private attribute

    Public Sub New(name As String, age As Integer)
        _name = name
        _age = age
    End Sub

    Public Property Name As String
        Get
            Return _name  ' Getter
        End Get
        Set(value As String)
            If String.IsNullOrEmpty(value) Then
                Console.WriteLine("Name cannot be null or empty.")
                Exit Sub
            End If
            _name = value  ' Setter
        End Set
    End Property

    Public Property Age As Integer
        Get
            Return _age  ' Getter
        End Get
        Set(value As Integer)
            If value < 0 Then
                Console.WriteLine("Age cannot be negative.")
                Exit Sub
            End If
            _age = value  ' Setter
        End Set
    End Property
End Class
```

### Key Takeaways:
* Encapsulation is about restricting direct access to an object's internal data and providing controlled access through methods (getters and setters).
* In all three languages, we define private attributes and use getters/setters to access and modify them safely.


## 2. Inheritance
Inheritance allows a class to inherit attributes and methods from another class. This promotes code reusability and establishes a relationship between different classes.

#### Python Examples: 
In Python, we can define a subclass that inherits from a base class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")  # Override the speak method

# Example usage
dog = Dog()
dog.speak()  # Calls the overridden method in Dog
```

### Java Example: 
In Java, inheritance is achieved using the extends keyword.

```java
class Animal {
    public void speak() {
        System.out.println("Animal speaks");
    }
}

class Dog extends Animal {
    @Override
    public void speak() {
        System.out.println("Dog barks");  // Override the speak method
    }
}
```
### VB.NET Example:
In VB.NET, we use the Inherits keyword for inheritance.

```vbnet
Public Class Animal
    Public Sub Speak()
        Console.WriteLine("Animal speaks")
    End Sub
End Class

Public Class Dog
    Inherits Animal

    Public Sub Speak()
        Console.WriteLine("Dog barks")  ' Override the Speak method
    End Sub
End Class
```

### Key Takeaways:
* Inheritance allows a class to inherit methods and properties from another class, enabling code reuse.
* In Python, Java, and VB.NET, we can override inherited methods to provide specific behavior for subclasses.

## 3. Polymorphism
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It also allows for methods to behave differently based on the object that is calling them.

### Python Example:

In Python, polymorphism can be demonstrated by overriding methods in derived classes.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")  # Override the speak method

class Cat(Animal):
    def speak(self):
        print("Cat meows")  # Override the speak method

# Example usage
animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()  # Polymorphism in action
```
### Java Example:
Polymorphism is achieved in Java by using method overriding.

```java
class Animal {
    public void speak() {
        System.out.println("Animal speaks");
    }
}

class Dog extends Animal {
    @Override
    public void speak() {
        System.out.println("Dog barks");
    }
}

class Cat extends Animal {
    @Override
    public void speak() {
        System.out.println("Cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal[] animals = { new Dog(), new Cat() };
        for (Animal animal : animals) {
            animal.speak();  // Polymorphism
        }
    }
}
```

### VB.NET Example:
In VB.NET, polymorphism is implemented through method overriding.

```vbnet
Public Class Animal
    Public Overridable Sub Speak()
        Console.WriteLine("Animal speaks")
    End Sub
End Class

Public Class Dog
    Inherits Animal
    Public Overrides Sub Speak()
        Console.WriteLine("Dog barks")
    End Sub
End Class

Public Class Cat
    Inherits Animal
    Public Overrides Sub Speak()
        Console.WriteLine("Cat meows")
    End Sub
End Class

Public Sub Main()
    Dim animals As Animal() = {New Dog(), New Cat()}
    For Each animal As Animal In animals
        animal.Speak()  ' Polymorphism
    Next
End Sub
```
### Key Takeaways:
* Polymorphism allows different classes to implement methods with the same name but different behavior.
* In Python, Java, and VB.NET, polymorphism is achieved through method overriding, allowing the same interface to behave differently based on the object type.


## 4. Abstraction
Abstraction hides the complexity of the implementation and only exposes the essential features of an object. This can be achieved through abstract classes or interfaces.

### Python Example:
In Python, we use abstract base classes (ABC) to define abstract methods.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass  # Abstract method

class Dog(Animal):
    def speak(self):
        print("Dog barks")  # Implement the abstract method

# Example usage
dog = Dog()
dog.speak()
```
### Java Example:
In Java, abstract classes or interfaces are used for abstraction.

```java
abstract class Animal {
    abstract void speak();  // Abstract method
}

class Dog extends Animal {
    @Override
    void speak() {
        System.out.println("Dog barks");
    }
}
```
### VB.NET Example:
In VB.NET, abstract classes are used to achieve abstraction.

```vbnet
Public MustInherit Class Animal
    Public MustOverride Sub Speak()  ' Abstract method
End Class

Public Class Dog
    Inherits Animal

    Public Overrides Sub Speak()
        Console.WriteLine("Dog barks")
    End Sub
End Class
```
### Key Takeaways:
* Abstraction allows us to define methods in a class that have no implementation, leaving the responsibility of providing specific implementations to subclasses.
* Python, Java, and VB.NET support abstraction through abstract classes or interfaces.
