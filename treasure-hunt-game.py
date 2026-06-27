## print 9 boxes 
## choose 1 box with treasure (randomly)
## give user 3 chances to get that box.
import random
import sys

row1 = ["🎁","🎁","🎁"]
row2 = ["🎁","🎁","🎁"]
row3 = ["🎁","🎁","🎁"]

map = [row1,row2,row3]
print(" ".join(row1))
print(" ".join(row2))
print(" ".join(row3))

computer_choice = random.choice([11,12,13,
                                 21,22,23,
                                 31,32,33])

u_input = input("enter 1st choice: ")
row = int(u_input[0])-1
column = int(u_input[1])-1
if int(u_input) == computer_choice:
    print("congratulations,you won🎉!")
    map[row][column] = '💎'
    print(" ".join(row1))
    print(" ".join(row2))
    print(" ".join(row3))
    sys.exit()
    
# marking user's 1st choice
map[row][column] = '❌'
print(" ".join(row1)) 
print(" ".join(row2))
print(" ".join(row3))


u_input = input("enter 2nd choice: ")
row = int(u_input[0])-1
column = int(u_input[1])-1
if int(u_input) == computer_choice:
    print("congratulation,you won🎉!")
    map[row][column] = '💎'
    print(" ".join(row1))
    print(" ".join(row2))
    print(" ".join(row3))
    sys.exit() 
    
# marking user's 2nd choice
map[row][column] = '❌'
print(" ".join(row1))
print(" ".join(row2))
print(" ".join(row3))


u_input= input("enter 3rd choice: ")
row = int(u_input[0])-1
column = int(u_input[1])-1
if int(u_input) == computer_choice:
    print("congratulations,you won🎉!")
    map[row][column] = '💎'
    print(" ".join(row1))
    print(" ".join(row2))
    print(" ".join(row3))
    sys.exit()
# marking user's 3rd choice
map[row][column] = '❌'
print(" ".join(row1))
print(" ".join(row2))
print(" ".join(row3))


print("game over!")
treasure_row = int(str(computer_choice)[0])-1
treasure_column = int(str(computer_choice)[0])-1
map[treasure_row][treasure_column] = '💎'
print("better luck next time🥲:")
print("treasure was at😄:",computer_choice)

