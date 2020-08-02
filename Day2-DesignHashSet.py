"""
Design a HashSet without using any built-in hash table libraries.
To be specific, your design should include these functions:
add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
"""


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_hash = []

    def add(self, key: int) -> None:
        """
        Function to add item to hash set
        :param key: item
        """
        if key not in self.my_hash:
            self.my_hash.append(key)
            print("--{} inserted in hashset".format(key))
            return
        print("--{} in hashset".format(key))

    def remove(self, key: int) -> None:
        """
        Function to remove item from hash set
        :param key: item
        """
        if key not in self.my_hash:
            print("--{} not in hashset".format(key))
            return False
        else:
            self.my_hash.remove(key)
            print("--{} removed from hashset".format(key))


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.my_hash:
            return True
        else:
            return False

def main():
    obj = MyHashSet()
    obj.add(1)
    obj.add(2)
    print(obj.contains(1))
    print(obj.contains(3))
    obj.add(2)
    print(obj.contains(2))
    obj.remove(2)
    print(obj.contains(2))

if __name__ == '__main__':
    main()