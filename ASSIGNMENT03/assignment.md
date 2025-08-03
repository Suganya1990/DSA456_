Assignment Completion

For this assignment to be considered complete, you must submit the following:

a completed analysis of functions listed for (part A)
a successful run for part B (green check for part B in actions)


Note: Assignment completion is the minimum requirement for your assignment. It does not mean you will receive full marks.



Assignment Objectives:

In this assignment, you will:

Complete analysis of multiple related functions for a class
Implement hash tables


Restrictions

As this assignment concerns implementing data structures, you cannot use any Python libraries or built-in Python data structures and functions unless otherwise stated.



Overview

In this assignment, you will look at several implementations of a Table. There are three tasks:

Analyze the member functions of the class SortedTable (code for this is provided below). This table is created using a sorted list, but it is not necessarily implemented well. You will analyze the listed functions.
Offer suggestions on how to make the SortedTable more efficient. After analyzing the functions, look at how it is done and come up with some changes that will make the code more efficient
Implement a Hash table
using chaining for collision resolution
using linear probing for collision resolution


Table functions overview

We will explore 3 ways to implement a Table. Each method will have a different internal structure, but the functionality will be the same. A table stores a set of key-value pairs, which are also referred to as records.

The following specification describes an overview of the table's general functionalities, but it does not specify any specifics in terms of implementation. In other words, it explains what it can do but doesn't specify any internal data structures.



       def __init__(self, capacity=32):

The initializer for the table defaults the initial table capacity to 32. It creates a list with capacity elements all initialized to None.



       def insert(self, key, value):

This function adds a new key-value pair to the table. If a record with a matching key already exists in the table, the function does not add the new key-value pair and returns False. Otherwise, the function adds the new key-value pair to the table and returns True. If adding a record will cause the table to be "too small" (defined in each class), the function will grow to accommodate the new record.



       def modify(self, key, value):

This function modifies an existing key-value pair in the table. If no record with a matching key exists in the table, the function does nothing and returns False. Otherwise, it modifies the existing value into the one passed into it and returns True.



       def remove(self, key):

This function removes the key-value pair with the matching key. If no record with a matching key exists in the table, the function does nothing and returns False. Otherwise, the record with the matching key is removed and returns a True.



       def search(self, key):

This function returns the value of the record with the matching key. If no record with a matching key exists in the table, the function returns None.



       def capacity(self):

This function returns the number of spots in the table. This consists of the total spots available in the table.



       def __len__(self):

This function returns the number of Records stored in the table.



Part A: Analyze the listed member functions of the SortedTable (40%)



Analyze the following functions concerning the number of Records stored in the SortedTable

       def insert(self, key, value):

       def modify(self, key, value):

       def remove(self, key):

       def search(self, key):

       def capacity(self):

       def __len__(self):



Note: the code below is not necessarily the best way to write a table using a sorted array. Outside of syntactic constructs, do not use this code for anything... it has a lot of inefficiencies.



class SortedTable:

       # packaging the key-value pair into one object

       class Record:

                def __init__(self, key, value):

                        self.key = key

                        self.value = value

 

 

       def __init__(self, cap=32):

                # this initializes a list of of capacity length with None

                self.the_table = [None for i in range(cap)]

                self.cap = cap

 

 

       def insert(self, key, value):

                if (self.search(key)!=None):

                        return False

 

                if(len(self) == self.cap):

                        # increase the capacity if list is full

                        new_table = [None for i in range(self.cap*2)]

                        for i in range(self.cap):

                                 new_table[i]=self.the_table[i]

                        self.the_table = new_table

                        self.cap *= 2

 

 

                self.the_table[len(self)]=self.Record(key,value)

                size = len(self)

                for i in range (0,size-1):

                        for j in range(0,size-1-i):

                               if(self.the_table[j].key>self.the_table[j+1].key):

                                         tmp=self.the_table[j]

                                        self.the_table[j]=self.the_table[j+1]

                                         self.the_table[j+1]=tmp

                return True

 

       def modify(self, key, value):

                i = 0

                while (i < len(self) and self.the_table[i].key != key):

                        i+=1

                if(i==len(self)):

                        return False

                else:

                        self.the_table[i].value = value

                        return True

 

 

       def remove(self, key):

                i = 0

                size = len(self)

                while (i < size and self.the_table[i].key != key):

                        i+=1

                if(i==size):

                        return False

                while(i+1 < size):

                        self.the_table[i]=self.the_table[i+1]

                        i+=1

                self.the_table[i] = None

                return True

 

       def search(self, key):

                i = 0

                size = len(self)

                while i < size and self.the_table[i].key != key :

                        i+=1

                if i==size:

                        return None

                else:

                        return self.the_table[i].value

 

       def capacity(self):

                return self.cap

 

       def __len__(self):

                i =0

                count = 0

                while(i < len(self.the_table)):

                        if(self.the_table[i]!=None):

                                 count+=1

                        i+=1

                return count



Part B Implementation of ChainingTable OR LinearProbingTable (60%)



Choose either chaining or linear probing. You don’t have to implement both!

When doing this coding portion of the assignment, you can use:

python lists
your assignment 1 linked list
python hash() function - don't write your own


A hash table places records based on a hash value you get from a hash function. We will use the built-in hash function in Python for this part of the assignment. A hash function returns a big number when given something to hash. We will use this function to hash the key of our key-value pair (not the value, just the key).



Example usage:

x = hash("hello world")    # x will be a number with many digits, possibly negative.

cap = 32 

idx = x % cap              # idx is guaranteed to be a value between 0 and 31 inclusive 

                           # because the mod operator guarantees that when you say x % n

                           # the result is always between 0 and n-1 inclusive



You will implement two hash tables for this assignment. One will use linear probing for collision resolution; the other will use chaining. You can use your assignment 1 linked list for the chaining table.



ChainingTable:

A ChainingTable is a hash table which uses chaining as its collision resolution method.



       def __init__(self, capacity=32):

The initializer for the table defaults the initial table capacity to 32. It creates a list with capacity elements all initialized to None.



       def insert(self, key, value):

This function adds a new key-value pair to the table. If a record with a matching key already exists in the table, the function does not add the new key-value pair and returns False. Otherwise, it adds the new key-value pair to the table and returns True. If adding the new record causes the load factor to exceed 1.0, you must grow your table by doubling its capacity.



       def modify(self, key, value):

This function modifies an existing key-value pair in the table. If no record with a matching key exists in the table, the function does nothing and returns False. Otherwise, the function modifies the changes in the existing value into the one passed into the function and returns True.



       def remove(self, key):

This function removes the key-value pair with the matching key. If no record with a matching key exists in the table, the function does nothing and returns False. Otherwise, the record with the matching key is removed and returns a True.



       def search(self, key):

This function returns the value of the record with the matching key. If no record with a matching key exists in the table, the function returns None.



       def capacity(self):

This function returns the number of spots in the table. This consists of spots available on the table.



       def __len__(self):

This function returns the number of Records stored in the table.



LinearProbingTable:

A LinearProbingTable is a hash table which uses linear probing as its collision resolution method. You can either use the tombstone method or the non-tombstone method. The choice is yours.



       def __init__(self, capacity=32):

The initializer for the table defaults the initial table capacity to 32. It creates a list with capacity elements all initialized to None.



       def insert(self, key, value):

This function adds a new key-value pair to the table. If a record with a matching key already exists in the table, the function does not add the new key-value pair and returns False. Otherwise, the function adds the new key-value pair into the table and returns True. If adding the new record causes the load factor to exceed 0.7, you must grow your table by doubling its capacity.



       def modify(self, key, value):

This function modifies an existing key-value pair in the table. If no record with a matching key exists in the table, the function does nothing and returns False. Otherwise, the function modifies the changes in the existing value into the one passed into the function and returns a True.



       def remove(self, key):

This function removes the key-value pair with the matching key. If no record with a matching key exists in the table, the function does nothing and returns False. Otherwise, the record with the matching key is removed and returns True.



       def search(self, key):

This function returns the value of the record with the matching key. If no record with a matching key exists in the table, the function returns None.



       def capacity(self):

This function returns the number of spots in the table. This consists of spots available on the table.



       def __len__(self):

This function returns the number of Records stored in the table.



Submission:

For this assignment to be considered complete, you must submit the following:

the analysis for part A (placed in the md file on GitHub)
a successfully running code for part B (on GitHub)