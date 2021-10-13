# Sets are used to store multiple items in a single variable.
# A set is a collection which is both unordered and unindexed.
# Sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# # Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# # Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# # Set Items - Data Types

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

# # type of data types 
myset = {"apple", "banana", "cherry"}
print(type(myset))

# # access items 
thisset = {"apple", "banana", "cherry"}
print("apple" in thisset)

# # add items 
thisset = {"apple", "banana", "cherry"}
thisset.add("string")
print(thisset)

# # Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# #  iterables :- Iterable is an object, which one can iterate over
# # The object in the update() method does not have to be a set, it can be any 
# # iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
print(type(thisset))
print(type(mylist))
thisset.update(mylist)
print(thisset)

# # remove items from list

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# # Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# # The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)


# # loops items 
# # you can loops in the set items of the sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)





''' 

 METHOD                                 DESCRIPTION

add()	                         Adds an element to the set
clear()	                         Removes all the elements from the set
copy()       	                 Returns a copy of the set
difference()	                 Returns a set containing the difference 
                                 between two or more sets
difference_update()	             Removes the items in this set that are 
                                 also included in another, specified set
discard()	                     Remove the specified item
intersection()                   Returns a set, that is the intersection of 
                                 two other sets
intersection_update()	         Removes the items in this set that are not present in other,
                                  specified set(s)
isdisjoint()	                 Returns whether two sets have a intersection or not
issubset()	                     Returns whether another set contains this set or not
issuperset()	                 Returns whether this set contains another set or not
pop()	                         Removes an element from the set
remove()	                     Removes the specified element
symmetric_difference()	         Returns a set with the symmetric differences
                                 of two sets
symmetric_difference_update()	 inserts the symmetric differences
                                 from this set and another
union()	                         Return a set containing the union of sets
update()	                     Update the set with the union of this set
                                  and others


 '''

