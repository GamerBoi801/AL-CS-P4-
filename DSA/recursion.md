# Understanding Recursion

Recursion is a programming technique where a function calls itself in order to solve a problem. It is commonly used for problems that can be broken down into smaller, similar sub problems. A recursive function typically consists of two main components:

1. **Base Case**: This is the condition under which the recursion terminates. It prevents infinite loops and allows the function to return a result.
2. **General Case**: This is the part of the function where the recursion occurs, breaking down the problem into smaller instances.

## Example: Factorial Function

The factorial of a non-negative integer \( n \) (denoted as \( n! \)) is defined as the product of all positive integers less than or equal to \( n \). The factorial can be defined recursively as follows:

- **Base Case**: 
  - \( 0! = 1 \) (by definition)
  
- **General Case**: 
  - \( n! = n \times (n - 1)! \) for \( n > 0 \)
  
  

### Factorial Function Implementation

Here’s how you can implement a factorial function in Python:

```python
def factorial(n):
    # Base case
    if n == 0:
        return 1
    # General case
    else:
        return n * factorial(n - 1)