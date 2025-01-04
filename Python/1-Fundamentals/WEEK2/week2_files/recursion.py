def rfib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return rfib(n-1) + rfib(n-2)


# to run in python shell: python -i recursion.py
# call the function in python shell: rfib(20)
