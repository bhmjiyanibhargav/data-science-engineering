#!/usr/bin/env python
# coding: utf-8
Question 1. Explain why we have to use the Exception class while creating a Custom Exception. Note: Here Exception class refers to the base class for all the exceptions. Answer :In Python, the Exception class is the base class for all built-in exceptions. When we create a custom exception class, we usually inherit from the Exception class to create our own hierarchy of exceptions.

By inheriting from the Exception class, we get access to all the behavior and attributes of the base class, including the ability to define custom constructors, methods, and properties. This can be useful when we want to define more specific error conditions and provide more detailed error messages for our custom exceptions.

In addition, inheriting from the Exception class ensures that our custom exception is compatible with all the built-in exception handling mechanisms in Python. This means that we can catch our custom exception using the same try-except block as we would use for any other built-in exception.

For example, if we define a custom exception class named MyCustomException that inherits from the Exception class, we can catch it using the following code: In summary, by inheriting from the Exception class, we can create custom exceptions that are compatible with Python's exception handling mechanisms, and that provide specific error conditions and messages for our programs.
# In[1]:


try:
    # some code that may raise MyCustomException
except MyCustomException as e:
    # handle the exception here

Question 2 :Write a python program to print Python Exception Hierarchy. Answer ;In this code, we start with the BaseException class, which is the base class for all exceptions in Python. We print the name of this class using the __name__ attribute.

We then define a variable named current_exception and initialize it to the Exception class, which is the base class for all non-system-exiting exceptions. We enter a while loop that continues until the current_exception is equal to the BaseException class.

Inside the loop, we print the name of the current_exception class using the __name__ attribute. We then update current_exception to be the base class of the current exception, which is accessed using the __base__ attribute.

When the loop completes, we will have printed the hierarchy of all non-system-exiting exceptions in Python, from the Exception class down to the BaseException class.
# In[2]:


def print_exception_hierarchy():
    base_exception = BaseException
    print(base_exception.__name__)
    current_exception = Exception
    while current_exception != base_exception:
        print(current_exception.__name__)
        current_exception = current_exception.__base__

print_exception_hierarchy()

Question 3 :What errors are defined in the ArithmeticError class? Explain any two with an example. answer :The ArithmeticError class is a base class for errors that occur during arithmetic operations, such as division by zeroor overflow. Here are two examples of errors that are defined in the ArithmeticError class:

a. ZeroDivisionError: This error occurs when we try to divide a number by zero. Here's an example: In this code, we are trying to divide the value of a by the value of b, which is zero This results in a ZeroDivisionError exception being raised. We are catching the exception in the except block and printing the error message.

b. OverflowError: This error occurs when we perform an arithmetic operation that results in a value that is too large to be represented by the data type. Here's an example In this code, we are trying to calculate the square of a, which is equal to 10 to the power of 1000. This results in a value that is too large to be represented by the data type, and an OverflowError exception is raised. We are catching the exception in the except block and printing the error message.

These are just two examples of errors that are defined in the ArithmeticError class. Other errors in this class include FloatingPointError, FusedMultiplyAdd, RecursionError, and AssertionError, among others.
# In[3]:


"""ZeroDivision Error"""
a = 10
b = 0
try:
    c = a / b
except ZeroDivisionError as e:
    print(f"Error: {e}")

"""OverflowErro"""
a = 10**1000
try:
    b = a * a
except OverflowError as e:
    print(f"Error: {e}")

Question 4 :Why LookupError class is used? Explain with an example KeyError and IndexError. Answer :The LookupError class is a base class for errors that occur when a key or index is not found in a mapping or sequence. It is a subclass of the Exception class.

Two examples of errors that are defined in the LookupError class are KeyError and IndexError. Here's an explanation of each with an example:

a. KeyError: This error occurs when we try to access a dictionary key that does not exist. b. IndexError: This error occurs when we try to access a sequence (e.g. a list, tuple, or string) with an index that is out of range
# In[4]:


"""KeyError"""
my_dict = {'a': 1, 'b': 2, 'c': 3}
try:
    value = my_dict['d']
except KeyError as e:
    print(f"Error: {e}")


"""IndexError"""
my_list = [1, 2, 3]
try:
    value = my_list[3]
except IndexError as e:
    print(f"Error: {e}")

Question 5. Explain ImportError. What is ModuleNotFoundError? Answer :ImportError is a Python exception that is raised when a module or package cannot be imported. This error can occur for several reasons, such as a missing dependency or a typo in the module name. The ImportError class is a subclass of the Exception class.

ModuleNotFoundError is a subclass of ImportError that was introduced in Python 3.6. It is raised when a module or package cannot be found. This error occurs when Python is unable to locate the module in any of the locations specified in the sys.path variable. Prior to Python 3.6, an ImportError exception would be raised instead of ModuleNotFoundErrorQuestion 6. List down some best practices for exception handling in python. Answer:Here are some best practices for exception handling in Python:

Catch the right exceptions: When catching exceptions, it's important to be as specific as possible. Catching a broad exception like Exception can make it difficult to debug issues because it could be caused by any number of things. Instead, catch only the exceptions that you expect to occur in your code.

Use try-except blocks sparingly: While try-except blocks are a powerful tool for handling exceptions, it's important to use them sparingly. In general, you should only use try-except blocks for code that is likely to raise an exception. Code that is not likely to raise an exception should not be included in a try-except block.

Use finally blocks to clean up resources: If your code uses resources like files or network connections, it's important to release those resources when you're done with them. Use a finally block to ensure that the resources are released, even if an exception occurs.

Don't ignore exceptions: It's important to handle exceptions in a meaningful way. Ignoring exceptions and simply printing an error message can make it difficult to diagnose issues. Instead, try to handle the exception in a way that allows the program to recover gracefully.

Use context managers: Context managers (with statements) are a powerful tool for managing resources like files or network connections. They ensure that resources are properly released when you're done with them, even if an exception occurs.

Log exceptions: Logging exceptions can be a helpful way to debug issues in production environments. Instead of printing error messages to the console, use a logging library like logging to log exceptions to a file or a remote server.

Be consistent: When handling exceptions, it's important to be consistent in your approach. Use the same exception handling pattern throughout your codebase to make it easier to understand and maintain.
# In[ ]:




