#Basic 
"""
Polynomial -> first degree: linear ; second degree: quadratic ; third degree: cubic 
Root -> square root 
exponential function , power of 2 
logarithms function 
"""
#list comprehension 
letter = [i for i in range(20) if i %2 == 0]

#map, filter and lambda 
nums = [1,2,3,4,5,6,7]
sum_up = map(lambda a: a*2, nums) 
filter_odd = filter(lambda x: x %2 ==0, range(20))
list(map(len,['word','apple','orange']))
list(map(sum,zip([1,2,3],[4,5,6])))

import functools
fact = functools.reduce(lambda a,b: a+b, [0,1,2,3,4])

from fractions import gcd
common_divider = functools.reduce(gcd,[20,34,10,29])

#iter 
x = iter(['apple','banana','cherry'])
print(next(x))

#reverse and sorted 
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
alpha_sort = sorted(alph)

#math  
x = round(5.2344,2)
x = pow(2,3)
x, y = divmod(22,4) #x dividia

import math 
x = math.ceil(100.72) #101
x = math.ceil(100.12) #101
x = math.floor(100.12) #100

x= math.sqrt(100) #10

nums = [2,3,2,5,6,7,12,23,55]
def meanFun(x):
    mean = float(sum(x))/len(x)
    mean_rounded = round(mean,2)
    return (mean_rounded)

def median(x):
    x.sort()
    if len(x)%2 == 0:
        median = (x[len(x)//2]+x[len(x)//2-1])//2 
    else:
        median = x[len(x)//2]
    return median 

def mode(x):
    count_num = collections.Counter(x)
    return max(count_num, key=count_num.get)

def std(x):
    mean = sum(x)/len(x)
    sd_i = []
    for i in x:
        sd_i.append(math.pow((i-m),2))
    sd = math.sqrt(sum(sd_i)/len(x))
    sd_rounded = round(sd,1)
    return sd_rounded 

    

###############################################################################
#Python Data Strcture  
"""
Python: List, Tuple, Set, Dictionary 
"""
#STRING METHOD
string = "binaryTree"
string.count("r") #return 2 

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
x  = txt.find("love",1,10)
x = txt.index("apples" )
x = txt.replace("apples", "bananas",2)

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
txt = "apple#banana#cherry#orange"
x = txt.split("#")

#LIST
array = list(range(5))
array1 = [1,2,3,4,5,6,7,8,9]
array[2] = 19
array.insert(2,2) #at specific position 
array.append(0) #at the end of it 
del array[2]
3 in array 
array.index(4)

l_1 = [1,2,2,3,3,44,5]
l_2=['a','f','g','h']
l_1.sort()
l_1.reverse()
l_1.count(2)
l_1.extend(l_2)


#tuples -> unmutable  
tup = (1,2,3,4,5)
tup1 = ('a','b','c')
tup.append('a')

#set 
num_unique = {1,2,3,3,4,5}
char_unique = set(['a','a','f','s'])
char_unique.add('d')
char_unique.add('g') #add at the begining 
char_unique.discard('d') #remove the one 
char1_unique = {'a','r','g'}
union_char = char_unique | char1_unique 
inter_char = char_unique & char1_unique
diff_char = char_unique - char1_unique

#dictionary 
diction = {'name':'catherine','age':7,'profession':'data science'}
diction.keys()
diction.items()
diction.values()

mydict = {'A':4,'B':10,'C':0,'D':87}
max_key = max(mydict, key=mydict.get)

for key in list(diction.keys()):''
    if key == 'name':
        del diction[key]
        diction[key] = "new name"

list1 = ['rose','lily','tulip','Daisy']
list2 =['red','white','pink','yellow']
dict_flower = {key:val for key, val in zip(list1,list2)}
dict_flower.update({'lily':'red'})

for key in dict_flower:
    print(key)
    print(key,'->',dict_flower[key])

for i,key in dict_flower.items():
    dict_flower[i] = key+'s'
    print(i,'->',dict_flower[i])


#matrix 
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
T.insert(2,[0,5,4,2])
import numpy as np 
m = np.array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m = np.reshape(m,(7,5))
m = np.append(m,[['New',12,3,4,5]],0)
#0->row, 1->column
m = np.insert(m,[5],[[0],[0],[0],[0],[0],[0],[0],[0]],1)
m = insert(m,[5],[[1],[2],[3],[4],[5],[6],[7]],1)


#Broadcasting a array !important 


############################################################################################
#advanced sort 
my_list=[-6,-5,-4,1,2,3]
s_li = sorted(my_list, key=square, reverse=True)

def square(x):
    return x**x

#ramdom number 
import random 
value = random.random()
value = random.randint(1,10)

greedings = ['Hi','Hello','Hey','Howdy']
greed = random.choice(greedings)
print('{}, Catherine'.format(greed))

colors = ['Red','Black','Yellow']
results = random.choices(colors, k=10, weights=[18,2,2])
print(results)

deck = list(range(1,53))
random.shuffle(deck)
hand = random.sample(deck, k=5)
print(deck)


#Formating 
#advanced formating 
dictionary = {'name':'catherine', 'gender':'female', 'age':30}
print("My name is {name}, I am a {age} years old {gender}".format(**dictionary))
sentence = f"My name is {dictionary['name']} and I am a {dictionary['age']} years old {dictionary['gender']}"
print(sentence)

my_list = ['hello', 10, 20]
print('{0[0]}, I want to add up {0[1]} and {0[2]}'.format(my_list))

pi = 3.1415926585
print('Pi is equal to {:.3f}'.format(pi))
print('1M is equal to {:,.2f}'.format(1000**2))


#Duck type and checking 
class Duck:
    def quack(self):
        print('Quack, quack!')

    def fly(self):
        print("Flap, flap!")

class Person:
    def quack(self):
        print('I\'m quacking like a duck')
    
    def fly(self):
        print("I'am flapping my arm")

def quack_and_fly(things):
    try:
        things.quack()
        things.fly()
        things.bark()
    except AttributeError as e:
        print(e)

    print()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

my_list=[1,2,3,4,5,6]

try:
    print(my_list[5])
except IndexError:
    print('index out of range ')


#Generator 
def square_numer(nums):
    for i in nums:
        yield (i**2)

my_nums = square_numer([1,2,3,4,5,6])

for num in my_nums:
    print(num)


#unit test 
import unittest 
def test_funciton():
    assert sum([1,2,3])==5, "should be 6 "


class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sum([1,2,3]),6)
    def test1(self):
        self.assertTrue(4+5 == 9, "The result is False")

#multi thread
import threading 
from queue import Queue

def testThread(num):
    print(num)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=testThread, args=(i,))
        t.start()

import multiprocessing
def spawn(num):
    print("test!",num)

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=spawn,args =(i,))
        p.start()


# 1. transpose of a matrix
matrix = [[1,2,3,4],[4,5,6,7]]
transp_matrix = [[row[i] for row in matrix]for i in range(len(matrix[0])) ]


####################################################################################################









