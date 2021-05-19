"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already
exists in the HashMap, update the value.

get(key): Returns the value to which the specified key is mapped, or -1 if
this map contains no mapping for the key.

remove(key) : Remove the mapping for the value key if this map contains
the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found)

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""
class ListNode:
    def __init__(self, key, val):
        self.keyval = (key, val)
        self.next = None

class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        print("Putting", key, value)
        if self.head == None:
            self.head = ListNode(key, value)
            print(f'new head {key} {value}')
        else:
            current_node = self.head
            while current_node.next is not None:
                if current_node.keyval[0] == key:
                    current_node.keyval = (key, value)
                    print(f'Updating {key} with {value}')
                    return
                current_node = current_node.next
            print(f'Placing into {key} value {value}')
            current_node.next = ListNode(key, value)


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        print("Getting", key)
        current_node = self.head
        while current_node is not None:
            print(f' checking {current_node.keyval[0]} == {key}')
            if current_node.keyval[0] == key:
                print("  Found", key, current_node.keyval[1])
                return current_node.keyval[1]
            current_node = current_node.next
        print("  Not found", key, "-1")
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        print("Removing", key)
        current_node = self.head
        while current_node is not None:
            print(" checking", current_node.keyval[0], current_node.keyval[1])
            if current_node.keyval[0] == key:
                print("  Replacing", current_node.keyval, "with (-1,-1)")
                current_node.keyval = (-1,-1)
                return
            current_node = current_node.next


obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
obj.get(1)            # returns 1
obj.get(2)            # returns 1
obj.get(3)            # returns -1 (not found)
obj.put(2, 1)         # update the existing value

print("-----")
print(obj.head.keyval)
print(obj.head.next.keyval)
print("-----")

obj.get(2)            # returns 1
obj.remove(2)         # remove the mapping for 2
obj.get(2)            # returns -1 (not found)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
