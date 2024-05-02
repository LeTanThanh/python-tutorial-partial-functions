if __name__ == "__main__":
  # Introduction to Python partial functions

  """
  The following example defines a function that multiplies two arguments:
  """

  def multiply(a, b):
    return a * b

  print(multiply(10, 2))

  """
  Sometimes, you just want to multiply an argument with a specified number e.g: 2.
  To do that, you can reuse the multiply function like this:
  """

  def double(a):
    return multiply(a, 2)

  """
  The double function returns that multiply function.
  It passed the number 2 to the second argument of the multiply function.

  The following shows how to use the double function:
  """

  print(double(10))

  """
  As you can see, the double function reduces the arguments of the multiply function.

  The double function freezes the second argument of the multiply function, which results in a new function with a simpler signature.

  In other words, double function reduces the complexity of the multiply function.

  In Python, the double is called a partial fuction.

  In practice, you use partial fuctions when you want to reduce the number of arguments of a function to simply the function's signature.

  Since you'll create partial functions sometimes, Python provides you with the partial function from the functools standard module to help you define a partial functions more easily.
  """

  # Python partial function from functools module

  """
  functions.partial(fn, /, *args, **kwargs)
  """

  from functools import partial

  def multiply(a, b):
    return a * b

  double = partial(multiply, b = 2)
  print(double(a = 10))
  print(double(a = 10, b = 3))
