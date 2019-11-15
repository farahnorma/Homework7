#
# list_quiz.py:
#
#   Starting code for H7-3
#

# Give short one-question quiz on HTT10 (Lists) to user

print('''\nmyList = ['apples', 'oranges', 'bananas', 'bread', 'milk', 'eggs'] 

		if user wants to print:
		['bread', 'milk', 'eggs']
		
		what should user enter in the print statement to splice this?
		i.e fill in the blank 'print(_______)
		''')


answer = str(input("? "))
if answer == "myList[3:]" or answer == "myList[-3:]" or answer == "myList[3:6]":
    print('\nCorrect!')

else:
    print('\nWrong. The correct answer was:'
          'myList[3:], or myList[-3:] or myList[3:6]')

print('''
        The slice operator starts at the first index and ends at
        the second.
        
        If you omit the first index of your slice the slice will
        start from the beginning.
        Likewise if you omit the second index, the slice will
        continue to the end of the list.
        
        The list index starts counting at 0. So in our list of
        items, apples is at index 0 and eggs is at 5.
        
        The slice operator will work until the second index
        minus 1.
        
        So to print the last element of an index, you would set 
        the slice to that index plus 1.
        
        In this case that means to slice eggs, the second index
        must print to 6 even though within the list the index 
        for eggs would be 5.

''')


