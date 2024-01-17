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
