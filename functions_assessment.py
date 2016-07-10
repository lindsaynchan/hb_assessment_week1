"""PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 
"""

def add_tax(item_cost, state_abbr, tax = .05):
#function that takes in the cost of the item, state and the tax is optional, otherwise
#default as 5%
    if state_abbr == "CA":
    #if the state is CA, use .07 as the tax percentage amount and find total cost
        total = item_cost + item_cost * .07
    else:
    #if the state is not CA, use the default tax percentage to find total cost
        total = item_cost + item_cost * tax
    return total
    #return the total cost (which includes item cost and tax)


"""
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

"""

def is_berry(fruit_name):
#function that takes in a name of a fruit
    fruit_name = fruit_name.lower()
    #makes the fruit name lowercase
    if fruit_name == "strawberry":
        return True
    elif fruit_name == "cherry":
        return True
    elif fruit_name == "blackberry":
        return True
    else:
        return False
    #check if fruit_name is strawberry, cherry or blackberry. if it is, return
    #True otherwise return False

def shipping_cost(fruit_name):
#function taht takes in a name of a fruit
    berry_result = is_berry(fruit_name)
    #calls is_berry function and saves the return to a variable
    if berry_result == True:
        return 0
    #if berry_result is True, return 0
    else:
        return 5
    #if berry_result is False, return 5

def is_hometown(town_name):
#function that takes in a town name
    town_name = town_name.lower()
    #making the town name lower case letters
    if town_name == "tiburon":
        return True
    #if the town name provided is tiburon, return True
    else:
        return False
    #if the town name provided is not tiburon, return False

def full_name(first_name, last_name):
#function that takes the first and last name as parameters
    return first_name+" "+last_name
    #returns a string with the full name

def hometown_greeting(town_name, first_name, last_name):
    town = is_hometown(town_name)
    #calls is_hometown and saves the boolean to town variable
    name = full_name(first_name, last_name)
    #calls full_name and saves the full name to name variable
    if town == True:
        return "Hi, "+name+", we're from the same place!"
    #if the town name is the same, return statement
    else:
        return "Hi, "+name+", where are you from?" 
    #if the town name is not the same, return statement


"""

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addone with y = 5. Call again with y = 20. 

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

"""

def increment(x=1):
#function that takes an optional number parameter
    def add(y):
    #function that takes in a number as a parameter
        return x + y
        #returns the result of x plus y
    return add
    #returns the result of function add()

addfive = increment(5)
#assigning increment function to variable addfive
print addfive(5)
#calling add() within the increment(), using the addfive variable
print addfive(20)
#calling add() within the increment(), using the addfive variable

def add_nums(num,num_list):
#function that takes in a number and a list of numbers
    num_list.append(num)
    #add the number to the end of the list of numbers
    return num_list
    #returning list



