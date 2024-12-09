# Converting Iterative Functions to Recursive Functions

This document provides a step-by-step guide on how to convert an iterative function into a recursive function. Understanding this process is essential for improving code readability and leveraging recursion's power in problem-solving.

## Why Convert?

Recursive methods can often be more intuitive and easier to understand than their iterative counterparts. Converting iterative code into recursive functions can help clarify the logic behind the algorithm, making it easier to follow and maintain.

## General Steps for Conversion

### Step 1: Identify the Loop Structure

- **Analyze the Iterative Code**: Understand how the loop operates, including its initialization, condition, and increment/decrement.
- **Identify Local Variables**: Determine which local variables are used in the loop and their roles in accumulating results or controlling flow.

### Step 2: Define Base Case

- **Determine Base Case**: Identify the condition under which the recursion should stop. This usually corresponds to when the loop condition becomes false.
- **Return Value**: Decide what value should be returned when the base case is reached.

### Step 3: Create Recursive Function

- **Function Signature**: Define a new function that takes parameters corresponding to the local variables used in the loop.
- **Recursive Call**: Replace the loop with a recursive call to this new function, adjusting parameters as necessary to reflect how they change with each iteration.

### Step 4: Implement Recursive Logic

- **Modify Parameters**: Ensure that parameters are modified in a way that mimics how local variables were updated in the loop.
- **Combine Results**: If applicable, combine results from recursive calls to produce the final output.

## Example Conversion

### Iterative Example: Finding GCD

#### Iterative Code
```plaintext
int a = 72, b = 20;

while (a != b) {
    if (a > b)
        a -= b;
    else
        b -= a;
}

```

### Recursive function 
```
FUNCTION gcd(a, b) RETURNS INTEGER
    IF a == b THEN
        RETURN a
    ELSE IF a > b THEN
        RETURN gcd(a - b, b)
    ELSE
        RETURN gcd(a, b - a)
END FUNCTION
```