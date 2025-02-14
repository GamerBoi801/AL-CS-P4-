public class Person {
    /**
     * Represents a person with a name and age.  Demonstrates encapsulation
     * using getters and setters to control access to the object's internal state.
     */
    private String name;  // Private attribute: Only accessible within the class
    private int age;      // Private attribute: Only accessible within the class

    /**
     * Constructor for the Person class.  Initializes the name and age.
     * @param name The person's name (String).
     * @param age  The person's age (int).
     */
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    /**
     * Getter method for the 'name' attribute. Provides read-only access
     * to the name.  This promotes encapsulation by preventing direct access
     * to the private 'name' attribute.
     * @return The name of the person (String).
     */
    public String getName() {
        return name;
    }

    /**
     * Setter method for the 'name' attribute.  Allows controlled modification
     * of the name.  It demonstrates input validation to ensure the data
     * remains consistent and valid. This is crucial for maintaining
     * the integrity of the object.
     * @param name The new name to set (String).
     */
    public void setName(String name) {
        if (name == null || name.isEmpty()) { //Example input validation
            System.out.println("Name cannot be null or empty");
            return; // Prevent setting the name if it's invalid
        }
        this.name = name;
    }

    /**
     * Getter method for the 'age' attribute. Provides read-only access to the
     * age.
     * @return The age of the person (int).
     */
    public int getAge() {
        return age;
    }

    /**
     * Setter method for the 'age' attribute.  Allows controlled modification
     * of the age.  It demonstrates input validation to prevent setting
     * a negative age.
     * @param age The new age to set (int).
     */
    public void setAge(int age) {
        if (age < 0) { //Example input validation
            System.out.println("Age cannot be negative");
            return; //Prevent setting if invalid
        }
        this.age = age;
    }

    /**
     * A method to describe the person.  This is a regular method that
     * operates on the object's attributes (name and age) to produce a
     * descriptive string.
     * @return A string describing the person.
     */
    public String describe() {
        return "This person is named " + name + " and is " + age + " years old.";
    }

    public static void main(String[] args) {
        /**
         * Main method to demonstrate the usage of the Person class,
         * getters, setters, and the describe method.
         */
        Person person = new Person("Alice", 30); // Create a Person object

        // Accessing attributes using getters
        System.out.println("Name: " + person.getName()); // Calls getName()
        System.out.println("Age: " + person.getAge());  // Calls getAge()

        // Modifying attributes using setters
        person.setName("Bob");     // Calls setName()
        person.setAge(25);       // Calls setAge()

        // Calling a method
        System.out.println(person.describe()); // Calls describe()

        person.setAge(-5); //Validation prevents it.
        person.setName(null); //Validation prevents it
    }
}
