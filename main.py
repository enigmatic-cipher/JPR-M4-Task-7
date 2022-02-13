"""
Given a number between 1 and 12 as input, print the corresponding month.
Input-> 12
Output-> December
"""

def month_name(num):

  if num == 1:
    print("January")

  elif num == 2:
    print("February")

  elif num == 3:
    print("March")

  elif num == 4:
    print("April")

  elif num == 5:
    print("May")
  
  elif num == 6:
    print("June")

  elif num == 7:
    print("July")

  elif num == 8:
    print("August")

  elif num == 9:
    print("September")
  
  elif num == 10:
    print("October")

  elif num == 11:
    print("November")

  elif num == 12:
    print("December")

num = int(input("Enter Months in Number: "))
month_name(num)

