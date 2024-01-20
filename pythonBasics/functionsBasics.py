def my_function(country="India"):
    print("Inside default param value function " + country)


my_function("Sweden")
my_function()


def arbitrary_function(*kids):
    print("Inside arbitrary function " + kids[2])


arbitrary_function("Emil", "Tobias", "Linus")


def keyword_function(**kid):
    print("Inside keyword_function " + kid["lname"])


keyword_function(fname="Suresh", lname="Kannan")


def positional_only_function(x, /):  # restricts keyword argument
    print("Inside positional_only_function", x)


positional_only_function(3)


# positional_only_function(x=3)  # restricts keyword argument

def keyword_only_function(*, x):  # allows  keyword-only argument
    print("Inside keyword_only_function", x)


keyword_only_function(x=3)


def keyword_only_function(*, x):  # allows  keyword-only argument
    print("Inside keyword_only_function", x)


keyword_only_function(x=3)


def both_keyword_and_combination_only_function(a, b, /, *, c, d):
    print("Inside both_keyword_and_combination_only_function: ", a + b + c + d)


both_keyword_and_combination_only_function(5, 6, c=7, d=8)

x = lambda a: print("Inside lambda fun", a + 10)
print(x(5))


# return a function
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print("executing lambda function", mydoubler(11))

a = 200
print("before changing global variable a", a)


def func_inside_func():
    print("func_inside_func", a)

    def inner_fun():
        print("inner function")

    inner_fun()


func_inside_func()


def global_var_func():
    global a
    a = 300
    print("Inside Global var func", a)


global_var_func()
print("accessing global variable a", a)
