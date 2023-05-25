""""""
"""
1. Check if a list contains an element |fruit = ['pear', 'orange', 'apple', 'grapefruit', 'apple', 'pear']
check 'orange'
if 'orange' in fruit:
    print("True")
else:
    print("False")
========================================================================
2.Find the index of the 1st matching element | 
for ex.fruit = ['pear', 'orange', 'apple', 'grapefruit', 'apple', 'pear']
print(fruit.index('pear'))
========================================================================
3.Remove all elements from a list from 2 methods |   fruit = ['pear', 'orange', 'apple']
fruit.clear()
print(fruit)
#del fruit
========================================================================
4.concatenate two lists from 2 ways.
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1+l2
print(l3)
l1.extend(l2)
print(l1)
========================================================================
5.How to manipulate every element in a list with list comprehension ,
new list with 1 added to every element.
li = [0,25,50,100]
new_list = [i+1 for i in li]
print(l1)
========================================================================
6.Count the occurrence of a specific object in a |
list pets = ['dog','cat','fish','fish','cat']count fish
pets = ['dog','cat','fish','fish','cat']
print(pets.count('fish'))
========================================================================
7.Return the length of a list |  li = ['a', 'b', 'c', 'd', 'e']
li = ['a', 'b', 'c', 'd', 'e']
print(len(li))
========================================================================
8.How to check if an element is not in a list? | li = [1,2,3,4]  check 4 and 5
li = [1,2,3,4]
if 4 in li:
    print('4 is Present')
elif 5 in li:
    print('5 is Present')
else:
    print("not present")
========================================================================
9.Multiply every element in a list by 5 |  a = [10,20,30,40,50]
#for i in a:
 #   i*=5
  #  print(i,end=',')
li = [i*5 for i in a]
print(li)
========================================================================
10.Insert a value at a specific index in an existing list.
li = ['a','b','c','d','e'] at 2nd position 'HERE'
li = ['a','b','c','d','e']
li.insert(1,'HERE')
print(li)
========================================================================
11.Remove elements in a list after a specific index
li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10] i want only first 1 to 10 number
print(li[:10])
========================================================================
12.Remove elements in a list between 2 indices 
li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10] from 13 to 17
li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
#l1 = li[:13]
#l2 = li[16:]
#l3 = l1+l2
#print(l3)
========================================================================
13.Return every 2nd element in a list between 2 indices 
li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10] between 4 to 16.
li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,10]
print(li[3:17:2])
========================================================================
14. Sort a list of integers in ascending order | li = [10,1,9,2,8,3,7,4,6,5]
li = [10,1,9,2,8,3,7,4,6,5]
li.sort()
print(li)
========================================================================
15.Sort a list of integers in descending order | li = [10,1,9,2,8,3,7,4,6,5]
li = [10,1,9,2,8,3,7,4,6,5]
li.sort()
print(li[::-1])
========================================================================
16.Filter even values out of a list with list comprehension | li = [1,2,3,4,5,6,7,8,9,10]
li = [1,2,3,4,5,6,7,8,9,10]
print([i for i in li if i%2==0])
========================================================================
17.Get the first element from each nested list in a list 
li = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
li = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
for i in li:
    print(i[0],end=',')
========================================================================
18.Combine elements in a list into a single string. 
li = ['The','quick','brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
li = ['The','quick','brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
s = ' '.join(li)
print(s)
========================================================================
19.Reverse the order of a list | li = [1,2,3,4,5,6,7,8,9,10]
li = [1,2,3,4,5,6,7,8,9,10]
#l1 = reversed(li)
#print(list(l1))
print(li[::-1])
========================================================================
20.Return the minimum value in a list | li = [10,1,9,2,8,3,7,4,6,5]
li = [10,1,9,2,8,3,7,4,6,5]
print(min(li))
========================================================================
21.Return the sum of values in a list | 
li = [10,1,9,2,8,3,7,4,6,5] with sum function and without sum function
li = [10,1,9,2,8,3,7,4,6,5]
#print("with sum function",sum(li))
c = 0
for i in li:
    c = c+i
print("without sum function",c)
=======================================================================
22.Find the intersection(same element) of 2 lists | li1 = [1,2,3]  ,li2 = [2,3,4]
l1 = set(li1)
l2 = set(li2)
l3 = l1.intersection(l2)
print(list(l3))
======================================================================
23.Flatten a list of lists with a list comprehensions | 
li = [[1,2,3],[4,5,6]] O/P: will be [1, 2, 3, 4, 5, 6]
li = [[1,2,3],[4,5,6]]
l1 = li[0] + li[1]
print(l1)
======================================================================
24.Generate a list of every integer between 2 values. take user input
l1 = list(input("Enter the number:"))
print(l1)
======================================================================
25.Reverse the order of a list using the slice syntax | li = ['a','b',3,4]
li = ['a','b',3,4]
#print(li[::-1])
#print(list(li.__reversed__()))
======================================================================
26. Remove empty strings from the list of strings | list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for value in list1:
    if value == "":
        continue
    print(value,end=",")
##ans2
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
l1 = list(filter(None, list1))
print(l1)
======================================================================
27.Add new item to list after a specified item |list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] 
EXPECTED [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
======================================================================
28.Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
AND # sub list to add sub_list = ["h", "i", "j"]
EXPECTED O/P :['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)
=====================================================================
29.Replace list’s item with new value if found | list1 = [5, 10, 15, 20, 25, 50, 20]  
EXPECTED O/P: [5, 10, 15, 200, 25, 50, 20]
list1 = [5, 10, 15, 20, 25, 50, 20]
list1[3] = 200
print(list1)
=====================================================================
30.Remove all occurrences of a specific item from a list.remove all occurrences of item 20.
list1 = [5, 20, 15, 20, 25, 50, 20]
for i in list1:
    if i==20:
        continue
    print(i,end=",")
======================================================================
31.Combine 2 lists into a dictionary 
name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff'] and animal = ['Cat', 'Dog', 'Fish', 'Goat'] 
USING zip function.
name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
d = dict(zip(name,animal))
print(d)
"""
