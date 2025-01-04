print() is a void function because it performs a task, not return a value

int() is a value-returning function

Global Variables:

my_string = "Set in global scope"

def_main():
global my_string
my_string = "Set in local scope"

main()
print(my_string)

lambda arg1, arg2: expression to return

(can only contain one expression)

#This higher-order function has a parameter of a callback function

def a_function(callback)
print(callback(3))

a_function(lambda num: num \*\*2)

Class 1/4/25 Notes:

for i in range(10):
if i % 5 == 0:
continue
elif i % 3 == 0:
break
print(i)

- this would print 1 2 \*
- continue means stay in the loop
- break means end the code

# Falsey values: False, 0, "", undefined
