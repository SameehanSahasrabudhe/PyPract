# Assigment 3 

# Task 1 : Calculate Factorial Using a Function


def factorial(n):
    '''
    This function take a integer as an input and,
    returns the value of factorial of that number.
    
    Arguments:-
    n : Integer input
    '''
    if n < 0:
        print("Number should be positive.")
        return None
    elif n <= 1:
        return 1
    else:
        out = n * factorial(n-1)
        return out


n = int(input('Enter a number : '))
fact = factorial(n)
print("Factorial of ", n, "is", fact)