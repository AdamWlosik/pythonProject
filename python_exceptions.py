def print_exceptions_tree(current_exception, n=0):
    if n > 1:
        print("   |" * (n - 1), end="")
    if n > 0:
        print("   +---", end="")
    print(current_exception.__name__)
    for sub_exception in current_exception.__subclasses__():
        print_exceptions_tree(sub_exception, n + 1)


print_exceptions_tree(BaseException)
'''BaseException
   +---Exception
    |   +---TypeError'''