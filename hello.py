import random
import sys
import os

print("hello world!")

name = "Rick"
# print(name)
'''
5 data types
Numbers, Strings, Lists, Tuples, Dictionaries

Math 7 operators
+ - * / % ** //

PEMDAS Matters
'''
#list can be changed
grocery_list = ['Milk','Eggs','Sugar','Salt','Spices']

# print('first item ', grocery_list[0])

# print(grocery_list[1:3])

other_events = ["Wash Car",'pick up kids']

to_do_list = [other_events, grocery_list]
# print(to_do_list)

grocery_list.append('Onions')
# print(to_do_list)

#tuple cannot be changed
pi_tuple = (3,1,3,4,5,6)
new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

# len(tuple) min(tuple) max(tuple)

#dictionaries can't join dicitionaries together like list

super_villians = {
    'fiddler': 'Isaac Bowin',
    'Captain Cold': "Leonard Snark",
    'Weather Wizard': 'Mark Mardon',
    'Mirror Master': 'Sam Scrudder',
    'Pied Piper': 'Thomas Peterson'
}

# print(super_villians['Captain Cold'])

del super_villians['fiddler']
super_villians['Pied Piper'] = 'Hartley Rathaway'

# print(len(super_villians))
# print(super_villians.get("Pied Piper"))
# print(super_villians.keys())
# print(super_villians.values())
# print(super_villians)

'''
if else statements

'''

age = 30
# if age > 16:
#     print('You are old enough to drive')
#     else:
#     print('You are not old enough to drive')

# if age >= 21:
#     print('You are old enough to drive a tractor trailor')
# elif age >= 16:
#     print("You are old enough to drive a car")
# else:
#     print('you are not old enough to drive')

# if((age >=1) and (age<=18)):
#     print('You get a birthday')
# elif (age == 21) or (age>=65):
#     print("you get a birthday")
# elif not(age == 30):
#     print('you dont get a birthday')
# else:
#     print("you get a party YAY")


# #looping

# for x in range(0, 10):
#     print(x, ' ')
# print('\n')

# for y in grocery_list:
#     print(y)

# num_list=[[1,2,3],[10,20,30],[100,200,300]]

# for x in range(0,3):
#     for y in range(0,3):
#         print(num_list[x][y])


#while loops
# random_num = random.randrange(0,100)

# while(random_num != 15):
#     print(random_num)
#     random_num = random.randrange(0,100)

# i = 0
# while(i <= 20):
#     if (i%2==0):
#         print(i)
#     elif(i == 9):
#         break
#     else:
#         i += 1
#         continue
#     i += 1
#functions reuse and write more readable code

def addNumbers(fNum,lNum):
    sumNum = fNum + lNum
    return sumNum

string = addNumbers(1,4)
print(string)

#sys

print('What is your name?')

namez = sys.stdin.readline()

print("hello ", namez)
