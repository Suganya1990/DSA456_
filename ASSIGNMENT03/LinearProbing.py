class LinearProbingTable:
    #Non-tombstone Method
    CONST_CAPACITY = 32
    
    class Entry:                                                                             #Basic Node for record 
        def __init__(self, key, value):                                                     
            self.key = key
            self.value = value
   
    def __init__(self, capacity=CONST_CAPACITY ):
        self.capacity = capacity                                                            # Sets intialize size to 32
        self.table = [None] * self.capacity
        self.size = 0                                                                       # Number of key-value pairs(counter)

    def _hash(self, key):
        return hash(key) % self.capacity                                                    # Used built in python function that mod capacity
    
    def _probe_index(self, key):                                                           
        index = self._hash(key)                                                             #computes initial index in the hash table 
        while True:
            yield index                                                                     #genrates a sequences of indices (one at a time) where the given key could be placed in the hash table
            index = (index + 1) % self.capacity                                             #moves index to next slot and can continue iterating the generator to get the next available index
    
    def _needs_resize(self):
        return self.size/self.capacity > 0.8                                                # Returns Ture if size/capacity > 0.7 or False size/capacity < 0.8
    
    def _resize(self):
        old_table = self.table                                                              # Assigns current table to old_table 
        self.capacity *=2                                                                   # Doubles current size capacity
        self.table = [None] * self.capacity                                                 # Emptys current table 
        self.size = 0                                                                       # Sets current size to 0 

        for entry in old_table:                                                             # Iterates through old table and inserts into objects table 
            if entry: 
                self.insert(entry.key, entry.value)                                         # Uses insert() to entry object

            
    def insert(self, key, value):
        if self._needs_resize():                                                            # Checks if table needs to be resized and resizes 
            self._resize()                                                                  # Doubles the capacity and re-inserts all entries using _resize()

        for index in self._probe_index(key):                                                # Probes for an index where they kay can be inserted
            slot = self.table[index]                                                        # Retrives the current slot in the table at the current index
            if slot is None:                                                                # check if the slot is empty
                self.table[index] = self.Entry(key, value)                                  # Inserts a new entry
                self.size += 1                                                              # Adds one to size (counter)
                return True                                                                 # Confirms the insert was successfull end exits
            elif slot.key == key:                                                           # has the same key then it means a duplicate key is being inserted 
                return False                                                                # Duplicate key and aborts 
        return False                                                                        # If loop finishes without inserting or finding a duplicate it returns false 

    def search(self, key):                                                                  # Finds and returns the value associate with a given key or None if key doesnt exist 
        for index in self._probe_index(key):                                                # Get each index where the key might be found
            slot = self.table[index]                                                        # Accesses the entry stored at the current index
            if slot is None:                                                                # Checks if slot is empty - if slot is empty the key doesnt exist in the table
                return None                                                                 # Stops searching and returns None
            elif slot.key == key:                                                           # Check if slots key matches one searching for 
                return slot.value                                                           # If matches returns value

    def modify(self, key, value):                                                           # Updates the value of an existing key | True = successfull Flase = unsucessfull
        for index in self._probe_index(key):                                                # Probes the table for a matching key
            slot = self.table[index]                                                        # Gets the slot at that index
            if slot is None:                                                                # If empty returns false
                return False    
            elif slot.key == key:                                                           # If key found update the value and return True
                slot.value = value
                return True
        return False                                                                        # If loop ends without finding the key return False 

    def remove(self, key):                                                                  # Remove key from the hash table         
        for index in self._probe_index(key):                                                # Probes the table for a matching key
            slot = self.table[index]                                                        # Retrives the element at the current index
            if slot is None:                                                                # If slot is empty return False 
                return False
            elif slot.key == key:                                                           # Check if the slot.key is the same as the key that needs to be removed
                self.table[index] = None                                                    # Remove the key value pair 
                self.size -= 1                                                              # reduce size (counter) by 1 
                self._rehash_cluster(index)                                                 # Re-insert the remaing elements properly into table after deletion 
                return True                                                                 
        return False                                

    def _rehash_cluster(self, start_index):                                                 # Rehash items after a deletion to prevent probe chain breakage.
 
        index = (start_index + 1) % self.capacity                                           # Starts 1 index after the removed index 
        while self.table[index] is not None:                                                # Continues looping until it hits a truly empty slot 
            entry = self.table[index]                                                       # Temporarily stores the current entry to re-insert it 
            self.table[index] = None                                                        # Removes the entry fro the current index 
            self.size -= 1                                                                  # Decrements size manaully 
            self.insert(entry.key, entry.value)                                             # Re-inserts the entry using normal insert() logic 
            index = (index + 1) % self.capacity                                             # Moves to the next index

    def __len__(self):                                                                      
        return self.size

    def capacity(self):                                                                      # Returns capacity of table 
        return self.capacity