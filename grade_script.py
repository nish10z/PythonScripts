##################################################################
# Script that automates grading on the 13.01 assignment in CSC230
#
# Author: Nishant Rodrigues
# Date: 10/25/2014
# Version: 1.0
##################################################################

from xlrd import open_workbook

wb = open_workbook('Exercise 13.01 _ Pointer Types (Responses).xlsx')

for s in wb.sheets():
	print 'Sheet:', s.name
	for row in range(1, s.nrows, 1):
		min = 2 # minimum points is 2
		points = 2.5 # start with minimum points
		for col in range(1, 4):
			if col == 1:
				print str(s.cell(row,col).value).split('@')[0], #print unity id only

			if col == 2:
				right_ans = 'x = y;' #right answer for question 1
				ans_string = str(s.cell(row,col).value) # get answer string
				ans_list = ans_string.split(',') # get all responses
				for ans in ans_list:
					if ans.strip() == right_ans:
						points += 1 # answer is correct, add 1 point
					else:
						points -= 0.5 # answer is incorrect, deduct 0.5 points

			if col == 3:
				right_ans_list = ['x = &3;', '&a = x;' ,'z = &&e;'] # make a list of correct answers
				ans_string = str(s.cell(row, col).value) #right answer for question 2
				ans_list = ans_string.split(',') # get all responses
				for ans in ans_list:
					if ans.strip() in right_ans_list:
						points += 0.5 # answer is correct, add 0.5 points
					else:
						points -= 0.5 # answer is incorrect, deduct 0.5 points

		if points < 2.0:
			print ' '.join(['Points:', str(min)]) # student has less than minimum points so grade is minimum points
		else:
			print ' '.join(['Points:', str(points)]) # student has more than minimum points, so grade is the points they have
	print