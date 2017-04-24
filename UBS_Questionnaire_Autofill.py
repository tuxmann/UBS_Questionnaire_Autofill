#
#  UBS_Questionnaire_Autofill.py
#
# Copyright 2015 Jason <aztuxmann@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#
#



import time
import os

Donor_Name = []
Gender = 1
DOB = []

def function1():
	print ""

# MAIN

if not os.path.isfile('UBS_Answers.txt'):	# File missing
	UBS_Answers = open('UBS_Answers.txt','w+')	# Create file
	
	while True:
		Donor_Name = raw_input("Enter your First and Last Name: ").split()
		try:
			Donor_Name[1]
		except IndexError:
			print "Last name not entered. Please try again."
		else:
			# Write to text file.
			break
	
	while True:
		Gender = int(raw_input("Enter (1) for Male, (2) for Female: "))	# 1 or 2 only
		print type(Gender)
		print Gender
		if Gender == 1 or Gender == 2:
			print "Good Job!" 
			# Record gender choice and break.
			break
		else:
			print "You goofed!"

	while True:
		print 
		DOB = raw_input("Enter your Date of Birth MM/DD/YYYY: ").split("/")		# Verify the date and then store it.
		
		break
		
else:	# Check existing file for complete answers.
	print "UBS_Answers.txt is in this directory."
	
