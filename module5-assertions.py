"""
raising exceptions yourself
assertions are assumptions in our program that should always be true
"""

def calculate_inverse(number):
    assert (number != 0), 'Got 0 as a number!' # after assert you put one or more conditions in round brackets. These are conditions that must be true for it to work right. If not true then it will show an error message
    return 1/number
    
calculate_inverse(0)    

#can also use assertions to: debug/test your code or for documenting your ode