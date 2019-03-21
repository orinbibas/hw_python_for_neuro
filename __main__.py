
from hw1_assignment1 import trifeca
from hw1_assignment2 import is_palindrome, check_palindrome
from hw1_assignment3 import compare_subjects_within_student

words = ['aavvdd','aAffkk','ccdekkkkaa','jjiilolloopp']
for word in words:
    trifeca(word)

check_palindrome()

subj1_all_students = [['tom',60,90],['noam',80,90],['tal',100,90],['shai',70,70],['gal']] #history
subj2_all_students = [['tom',70,70],['noam',50,30],['tal',70,90],['shai',90,70],['gal',100,70]] #math
compare_subjects_within_student(subj1_all_students,subj2_all_students)
