"""
STEPS:

1.requirements:
    -name of student
    -no:of subjects
    -total marks of each subject

2. calculations
	- total marks obtained by student
	- total marks 
	- calculate total percentage
	- calculate percentage by each subject 
	
"""

## development phase 1:
	# define a main function
	# define calculate_total_marks

#development phase 2:
	# define a function for getting marks from student  --> get_student_marks()
	# add  get_student_marks() calling statement in main function

#development phase 3:
	# define a function for calculating total marks obtained by student  --> calculate_student_total_marks()
	# add calculate_student_total_marks() calling statement in main function

#development phase 4:
	# define a function for calculating percentage  --> calculate_percentage()
	# add calculate_percentage() calling statement in main function

#development phase 5:
	# calculate percentage of mark by each subject
	# define a function for calculating each subject percentage  --> percentage_by_each_subject()
	# add percentage_by_each_subject() calling statement in main function


def calculate_total_marks(total_marks_list):
	sum = 0
	for i in total_marks_list:
		sum += i
	return sum

def get_student_marks(subject_list):
	student_marks_list = []
	for i in subject_list:
		marks = int(input(f"Enter marks for {i}: "))
		student_marks_list.append(marks)
	return student_marks_list

def calculate_student_total_marks(student_marks_list):
	total_marks_of_student = 0
	for i in student_marks_list:
		total_marks_of_student += i
	return total_marks_of_student

def calculate_percentage(sum,total_marks_of_student):
	mark_percentage = (total_marks_of_student/sum)*100
	return mark_percentage

def percentage_by_each_subject(*values):
	subject_percentage_list = []
	for index,subject in enumerate(values[0]):
		subject_percentage = (values[1][index]/values[2][index])*100
		print(f"Percentage of {subject} is {subject_percentage:.2f}%")
				
		
		
def main():
	total_marks_list = []
	subject_list = ["math",'english','arabic']
	name = input("enter the name")
	
	#get total marks of each subject
	for i in subject_list:
		total_mark_by_each_subject =int(input(f"enter the total mark of the subject {i}: "))
		total_marks_list.append(total_mark_by_each_subject)

	sum = calculate_total_marks(total_marks_list)
	student_marks_list = get_student_marks(subject_list)

	
	total_marks_of_student = calculate_student_total_marks(student_marks_list)
	

	mark_percentage = calculate_percentage(sum,total_marks_of_student)
	print("\n")

	print(f"Total percentage is {mark_percentage: .2f} %")

	print("\n")
	percentage_by_each_subject(subject_list,student_marks_list,total_marks_list)

if __name__=="__main__":
	main()