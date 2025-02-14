Public Class Person
    ''' <summary>
    ''' Represents a person with a name and age.  Demonstrates encapsulation
    ''' using Properties (Get/Set) to control access to the object's internal state.
    ''' </summary>
    ' Private attributes - Encapsulated data members accessible only within the class.
    Private _name As String
    Private _age As Integer

    ''' <summary>
    ''' Initializes a new instance of the <see cref="Person"/> class.
    ''' </summary>
    ''' <param name="name">The name of the person.</param>
    ''' <param name="age">The age of the person.</param>
    Public Sub New(name As String, age As Integer)
        _name = name 'Assign name
        _age = age  'Assign age
    End Sub

    ''' <summary>
    ''' Gets or sets the name of the person.  Demonstrates a Property with Get and Set
    ''' procedures to control access and modification, enabling validation.
    ''' </summary>
    ''' <value>The name of the person.</value>
    Public Property Name As String
        Get
            ' Get procedure:  Returns the value of the private _name field.
            Return _name
        End Get
        Set(value As String)
            ' Set procedure:  Assigns a new value to the private _name field,
            ' incorporating validation to ensure data integrity.
            If String.IsNullOrEmpty(value) Then  'Perform validation
                Console.WriteLine("Name cannot be null or empty.")
                Exit Sub 'Exit setter if validation fails to prevent invalid input.
            End If
            _name = value 'Assign to field
        End Set
    End Property

    ''' <summary>
    ''' Gets or sets the age of the person. Provides Get and Set
    ''' procedures to control access and modification, allowing validation.
    ''' </summary>
    ''' <value>The age of the person.</value>
    Public Property Age As Integer
        Get
            ' Get procedure:  Returns the value of the private _age field.
            Return _age  'Return the age
        End Get
        Set(value As Integer)
            ' Set procedure:  Assigns a new value to the private _age field,
            ' but only if the provided value is valid.
            If value < 0 Then  ' Example value validation to prevent invalid data.
                Console.WriteLine("Age cannot be negative.")
                Exit Sub 'Exit setter to not set
            End If
            _age = value 'Set age to the backing filed.
        End Set
    End Property
    ''' Returns a string that represents the current object (the person).
    ''' This is a regular method - not a Property Get or Set.  It combines
    ''' the object's attributes to create a descriptive string.
    ''' <returns>A string representation of the person.</returns>

    Public Function Describe() As String
        ' Formats and returns a string describing the person, using the
        ' Name and Age properties (which in turn access the private fields).
        Return "This person is named " & Name & " and is " & Age & " years old."
    End Function

    Public Shared Sub Main()
        ''' <summary>
        ''' Main entry point of the program.  Demonstrates creating a Person
        ''' object, using its Get and Set properties to access/modify data,
        ''' and calling its Describe method.
        ''' </summary>
    
        Dim person As New Person("Alice", 30) 'New object

        ' Accessing attributes using getters (Properties in VB.NET)
        Console.WriteLine("Name: " & person.Name) 'Call the Get Name
        Console.WriteLine("Age: " & person.Age)  'Call the Get Age

        ' Modifying attributes using setters (Properties in VB.NET)
        person.Name = "Bob" 'Call the Set Name
        person.Age = 25   'Call the Set Age

        ' Calling a method
        Console.WriteLine(person.Describe()) 'Call the describe() Method

        person.Age = -5 'Validation prevents it
        person.Name = "" 'Validation prevents it
    End Sub
End Class
