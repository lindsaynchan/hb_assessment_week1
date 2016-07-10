"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """

    odd_numbers_list = []
    #created empty list that will contain the odd numbers of the list
    for item in numbers:
    #iterate through all the numbers in the inputted list of numbers
        if item % 2 != 0:
            odd_numbers_list.append(item)
    #if the number is not even, add the number to the odd_numbers_list
    return odd_numbers_list
    #return the list of odd numbers


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo
    """

    item_index_list = []
    #created an empty list that will contain the item's index number and item name
    for index in range(len(items)):
    #iterate through each index in the list 
        item_index_list.append(str(index)+" "+items[index])
        #add the index number and item assigned to the index number as a string to 
        #the item_index_list
    for item in item_index_list:
        print item
    #iterate and print each string in the item_index_list


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale"],
        ...     ["hummus", "beets", "bagel", "lentils", "kale"]
        ... )
        ['bagel', 'kale']

    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """

    intersection = set(foods1) & set(foods2)
    #finding the intersection between both lists by using sets
    return list(intersection)
    #returning the intersection as a list instead of a set


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """

    every_other_list = []
    #create an empty list that will contain every other number

    for i in range(len(items)):
    #iterate through each index of the list
        if i % 2 == 0:
            every_other_list.append(items[i])
        #if the index is divisible by 2/even, append the number that's assigned to that index
        #to the every_other_list

    print every_other_list
    #print out the every_other_list

def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """

    if n == 0:
        return []
    #if n is 0, return an empty list
    else:
    #if n is not 0
        for i in range(len(items)):
        #iterate through each index of the list
            for i in range(len(items)-1):
            #iterate through all the indexes of the list except the last
                if items[i] > items[i+1]:
                #if the number to the left is larger than the one on the right
                    temp_num = items[i]
                    #assign the left number temporarily to temp_num
                    items[i] = items[i+1]
                    #rebind the left number as the right number
                    items[i+1] = temp_num
                    #rebind the right number as the left number
            #loop through the entire number list to ensure the largest numbers
            #are on the right
        return items[0-n:]
        #print the n amount of largest numbers in the list


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
