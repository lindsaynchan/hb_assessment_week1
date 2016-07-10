"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

    >>> nums = [1, 2]
    >>> add_new_number(5, nums)
    >>> nums
    [1, 2, 5]

    
    """

"""PART ONE"""

def hello_world():
#create a function that doesn't take any parameters
    print "Hello World"
    #prints "Hello World"

def say_hi(name):
#create a function that takes in the parameter name
    print "Hi", name
    #prints "Hi" and the name

def print_product(num1, num2):
#create a function that takes in two numbers as parameters
    return num1 * num2
    #returns the total of the first number times the second

def repeat_string(word, num):
#creates a function that takes in a string and a number
    print word*num
    #returns the string the number of times that was put as the parameter

def print_sign(num):
#creates a function that takes in a number as a parameter
    if num > 0:
    #sees if the number is greater than 0
        print "Higher than 0"
        #returns statement if condition is met
    elif num < 0:
    #sees if the number is less than 0
        print "Lower than 0"
        #returns statement if condition is met
    elif num == 0:
    #sees if the number is 0
        print "Zero"
        #returns statement if condition is met

def is_divisible_by_three(num):
#creates a function that takes in a number as a parameter
    if num % 3 == 0:
        return True
    #if number is divisible by 3, True will be returned
    else:
        return False
    #if number is not divisible by 3, False will be returned

def num_spaces(sentence):
#creates a function that takes in a sentence as one string
    words = sentence.split(" ")
    #splits the string by the spaces
    spaces = len(words) - 1
    #counts the number of words and subtracts 1 to find the number of spaces
    print spaces

def total_meal_price(price, tip_percentage = .15):
#creates a function that takes in the price and optional parameter of tip percentage
    total = float(price) + float(price) * float(tip_percentage)
    #calculates the total of the meal by calculating the tip and adding it to the meal
    return total

def sign_and_parity(num):
#creates a function that takes in a number as a parameter
    information_num = []
    #creating an empty list that will contain the sign and parity of the number
    
    if num % 2 == 0:
        information_num.append("Even")
    #checks if the number is even and will append the statement to information_num
    else:
        information_num.append("Odd")
    #checks if the number is odd and will append the statement to information_num

    if num >= 0:
        information_num.append("Positive")
    #checks if the number is positive and will append the statement to information_num
    else:
        information_num.append("Negative")
    #checks if the number is negative and will append the statement to information_num

    return information_num
    #returns the list that contains the sign and parity of the number

def unpack_sign_and_parity(num):
#creates a function that takes in a number as a parameter
    sign_parity_return = sign_and_parity(num)
    #assigns the output of the sign_and_parity function to a variable
    parity, sign = sign_parity_return
    #unpacks the contents of the list into variables
    return sign_parity_return

"""PART TWO"""

def full_title(name, job = "Engineer"):
#function that takes in a name and a job title as parameters
    return job +" "+ name
    #returns the job and name in a string

def write_letter(name, job, sender_name):
#function that takes in a name, job and the sender's name as parameters
    print "Dear"+" "+job+" "+name+", I think you are amazing! Sincerely, "+sender_name
    #prints a statement containing the parameters

def add_new_number(num,list_nums):
#function that takes in a number and a list of numbers as parameters    
    if list_nums.append(num):
    #add the number to the list
        return list_nums
        #return the entire list

################################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.


# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result.


# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times


# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".


# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.


# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces.


# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.


# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.


################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.

# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print


