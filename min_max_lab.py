"""
Max and Min Number Lab Written by Kevin Oyowe
October 11, 2016
"""
def find_max_min(input):
  # This function returns the minimum and maximum number in a list
  # If the min and max are equal, it returns the number of elements in the list
  resultingList = []
  max_num = max(input)
  min_num = min(input)
  if min_num == max_num:
    num_of_elements = len(input)
    resultingList.append(num_of_elements)
  else:
    resultingList.append(min_num)
    resultingList.append(max_num)
  return resultingList