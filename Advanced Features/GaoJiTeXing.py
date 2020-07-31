# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:50:51 2020

@author: LvGJ
"""
import string
from functools import reduce
def _trim(s):
    start = 0
    end = len(s)-1
    while(start<=end and (s[start] == ' ' or s[end] == ' ')):
        if(s[start] == ' '):
            start += 1
        if(s[end] == ' '):
            end -= 1
    return s[start:end+1]

for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)
    
def findMinAndMax(L):
    return (min(L),max(L))


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() if isinstance(x,str) else x for x in L1]

# generator
def triangles():
    for i in range(0,10):
        if(i == 0):
            yield [1]
        else:
            res = []
            res.append(1)
            for j in range(1,i):
                res.append(pre[j-1] + pre[j])
            res.append(1)
            yield res
            pre = res.copy()
            
            
# map/reduce
def normalize(name):
    res = ''
    if(name[0].islower()):
        res += name[0].upper()
    else:
        res += name[0]
    for i in name[1:]:
        if(i.isupper()):
            res += i.lower()
        else:
            res += i
    return res

def prod(L):
    def helper(a,b):
        return a*b
    return reduce(helper,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
    
# def str2float(s):
#     def helper(a,b)

# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')    
        
#filter
def is_palindrome(n):
    s = str(n)
    left = 0
    right = len(s)-1
    while(right>left):
        if(s[left] == s[right]):
            left+=1
            right-=1
        else:
            return False
    return True

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
    
# sorted
def by_name(t):
    return t[0]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name)
print(L2)






















