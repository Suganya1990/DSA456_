# Part A: Analyze the listed member functions of the SortedTable (40%)

### 1. def insert(self, key, value):\
__Functionality__
       This function cheks if a key already exists using search(), then resizes the table and when it hits its max size will double the size of the table. Then it inserts the new record and finally sorts the list using bublle sort. 

__Time Complexity__: __O(n2)__
\* Search Functionality is O(n). 
\* Resizes and copy O(n)
\* Bubble Sort after insert O(n^2)


### 2. def modify(self, key, value):
__Functionality__ 
This function searches for the key linearly and updates the value if found

__Time Compleixity__: __O(n)__ 
This means if n= 100 then the function may have to check every item before finding the key or concluding its not in the list. This can be improved by using binary serach


### 3. def remove(self, key):
__Functionality__ 
Find the key then removes the record, and finally shifts proceeding elements left. 

__Time Compleixity__: __O(n)__
Both search and shift are O(n). This is because the search goes through every single record to find the key once found it has to then shift the proceeding records by one. In the worst case scenario the record is found first record o(1), but then has to shift all the proeeding records by one to the left which will be o(n) and if n = 100 it would be 100 moves down. 
The Search portion can be improved through binary search. 


### 4. def search(self, key):
__Functionality__ 
The search functionality searches linearly for a matching key 

__Time Compleixity__: __O(n)__ The list comes sorter but the function has to go through every single record and look for the key. This can be improved using binary search which can improve the time complexity to __O(log n)__

### 5. def capacity(self):
__Functionality__ 
This returns the current capacity of the table 

__Time Compleixity__: __O(1)__ This just returns the size of the table, and requires a one time excecution always and thus O(1)

### 6. def __len__(self):
__Functionality__ 
When this function is called it will iterate through the entire table and count all the records. 


__Time Compleixity__: __O(n)__
Since it has to count every single record the time complexity is __O(n)__. This can be improved by having a counter variable to keep track of number of insertions and will update when an element is removed or inserted. This will minimize the need to count and will give a time compelxity of O(1).
       


