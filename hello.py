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

# def addNumbers(fNum,lNum):
#     sumNum = fNum + lNum
#     return sumNum

# string = addNumbers(1,4)
# print(string)

# #sys

# print('What is your name?')

# namez = sys.stdin.readline()

# print("hello ", namez)

# def answer(plaintext):
#     brailleDict = {
#     " ": "000000",
#     "a": "100000",
#     "b": "110000",
#     "c": "100100",
#     "d": "100110",
#     "e": "100010",
#     "f": "110100",
#     "g": "110110",
#     "h": "110010",
#     "i": "010100",
#     "j": "010110",
#     "k": "101000",
#     "l": "111000",
#     "m": "101100",
#     "n": "101110",
#     "o": "101010",
#     "p": "111100",
#     "q": "111110",
#     "r": "111010",
#     "s": "011100",
#     "t": "011110",
#     "u": "101001",
#     "v": "111001",
#     "w": "010111",
#     "x": "101101",
#     "y": "101111",
#     "z": "101011"
# }
    
#     outputArray = []
#     plaintextArray = list(plaintext)
    
#     for letter in plaintextArray:
#         if letter.lower() != letter:
#             outputArray.append("000001"+brailleDict[letter.lower()])
#         else:
#             outputArray.append(brailleDict[letter])
#     return ''.join(outputArray)
        
# print(answer('aba A a'))
# | 7
# | 4 8
# | 2 5 9
# | 1 3 6 10

# def yTable(y):
#     result = [1]
#     i = 1
#     while(i <= y):
#         if i == 1:
#             result.append(2)
#         else:
#             result.append(i+result[i-1])
#         i += 1
#     return result[len(result)-1]

# yTable(10)

# def xTable(x):
#     result = [1]
#     i = 2
#     while(i <= x):
#         if i == 2:
#             result.append(3)
#         else:
#             result.append(i+result[i-2])
#         i += 1
#     return result[len(result)-1]

# xTable(5)

# def answer(x, y):
#     xArr = [1]
#     i = 2
#     while(i <= x):
#         if i == 2:
#             xArr.append(3)
#         else:
#             xArr.append(i+xArr[i-2])
#         i += 1
#     xResult = xArr[len(xArr)-1]

#     finalResult = []
#     j = x
#     y = y+j-2
#     while(j <= y):
#         if len(finalResult)==0:
#             finalResult.append(j + xResult)
#         else:
#             finalResult.append(j+finalResult[j-(x+1)])
#         j+=1
#     return str(finalResult[len(finalResult)-1])
    
# print(answer(12345,67890))


#solution = (x*y)*2
# def answer(s):
#   a=0
#   for i, char in enumerate(s):
#         if char == '>':
#           a+= str(s).count("<",i,len(s))
#   return a*2


# print(2, answer('>----<'))
# print(6, answer('>--<-->--<'))
# print(2, answer('<-->--<-->>'))


def answer(M, F):
    M = int(M)
    F = int(F)
    cycle = 0

    while M != F:
        if(M > F):
            cycle += M/F
            M %= F
            if (M == 0):
                cycle -= 1
                M = F
        else:
            cycle += F/M
            F %= M
            if (F == 0):
                F = M
                cycle -= 1

    if(M != 1):
        return 'impossible'

    return str(cycle)

print(answer(2,4))