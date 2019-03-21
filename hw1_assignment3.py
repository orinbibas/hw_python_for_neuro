
def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    for i in range(len(subj1_all_students)) :
        if len(subj1_all_students[i]) == 3 and len(subj2_all_students[i]) == 3 :
            subj1_max= max(subj1_all_students[i][1],subj1_all_students[i][2])
            subj2_max= max(subj2_all_students[i][1],subj2_all_students[i][2])
            if subj1_max > subj2_max :
                print(subj1_all_students[i][0],'History')
            elif subj1_max < subj2_max :
                print(subj1_all_students[i][0],'Math')
            elif subj1_max == subj2_max :
                print(subj1_all_students[i[[0],'both']])

if __name__ == "__main__":
    compare_subjects_within_student(subj1_all_students,subj2_all_students)