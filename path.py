import os

dir1 = "source/head"
list = os.listdir(dir1)
number_of_head = len(list)

dir2 = "source/glasses"
list = os.listdir(dir2)
number_of_glasses = len(list)

dir3 = "source/beard"
list = os.listdir(dir3)
number_of_beard = len(list)

dir4 = "source/body"
list = os.listdir(dir4)
number_of_body = len(list)

dir5 = "myChar/"
list = os.listdir(dir5)
number_of_char = len(list)

TOTAL = number_of_body*number_of_beard*number_of_glasses*number_of_head