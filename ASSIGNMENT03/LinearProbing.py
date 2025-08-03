class LinearProbingTable:
    #Non-tombstone Method
    #Basic Node for record 
    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value
   
    def __init__(self, capacity=32):
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.size = 0 # Number of key-value pairs(counter)

    def _hash(self, key):
        return hash(key) % self.capacity
    
    def _probe_index(self, key):
        index = self._hash(key)
        while True:
            yield index
            index = (index + 1) % self.capacity
    
    def _needs_resize(self):
        return self.size/self.capacity > 0.7
    
    def _resize(self):
        old_table = self.table
        self.capacity *=2
        self.table = [None] * self.capacity
        self.size = 0

        for entry in old_table:
            if entry: 
                self.insert(entry.key, entry.value)
            
    def insert(self, key, value):
        if self._needs_resize():
            self._resize()

        for index in self._probe_index(key):
            slot = self.table[index]
            if slot is None:
                self.table[index] = self.Entry(key, value)
                self.size += 1
                return True
            elif slot.key == key:
                return False  # Duplicate key
        return False

    def search(self, key):
        for index in self._probe_index(key):
            slot = self.table[index]
            if slot is None:
                return None
            elif slot.key == key:
                return slot.value

    def modify(self, key, value):
        for index in self._probe_index(key):
            slot = self.table[index]
            if slot is None:
                return False
            elif slot.key == key:
                slot.value = value
                return True
        return False

    def remove(self, key):
        for index in self._probe_index(key):
            slot = self.table[index]
            if slot is None:
                return False
            elif slot.key == key:
                self.table[index] = None
                self.size -= 1
                self._rehash_cluster(index)
                return True
        return False

    def _rehash_cluster(self, start_index):
        """Rehash items after a deletion to prevent probe chain breakage."""
        index = (start_index + 1) % self.capacity
        while self.table[index] is not None:
            entry = self.table[index]
            self.table[index] = None
            self.size -= 1  # insert() will re-add it and increase size
            self.insert(entry.key, entry.value)
            index = (index + 1) % self.capacity

    def __len__(self):
        return self.size

    def capacity(self):
        return self.capacity