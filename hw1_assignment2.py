def is_palindrome(str_number):
    """
    Checks if a number as a string is a palindrome, return bullian 
    """
    for i in range(0,len(str_number)):
        rev_number = str_number[::-1]
        if str_number == rev_number:
            return True
        else:
            return False

def check_palindrome():
    """
   Runs through all 6-digit numbers and checks the mentioned conditions.
   The function prints out the numbers that satisfy this condition.

   Note: It should print out the first number (with a palindrome in its last 4 digits),
   not all 4 "versions" of it.
   """
    numbers = range(100000,999999)
    for number in numbers:
        str_number = str(number)
        str_number = str_number[2:]
        if is_palindrome(str_number) == True: #first number has palindrome in its last 4 digits
            plus1_number = number+1
            str_number = str(plus1_number)
            str_number = str_number[1:]
            if is_palindrome(str_number) == True: #2nd number has palindrome in its last 5 digist
                plus2_number = number+2
                str_number = str(plus2_number)
                str_number = str_number[1:5]
                if is_palindrome(str_number) == True: #3rd number has palindrome in its 
                    print(number)
                    plus3_number = number+3
                    str_number = str(plus3_number)
                    if is_palindrome(str_number) == True:
                        print(number)

                        

if __name__ == "__main__":
    check_palindrome()