"""
Design an Iterator class, which has:
A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
Example:
CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.
iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
"""

from itertools import combinations


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.co = [''.join(_) for _ in list(combinations(characters, r=combinationLength))]

    def next(self) -> str:
        return self.co.pop(0)

    def hasNext(self) -> bool:
        return bool(self.co)


def main():

    # Your CombinationIterator object will be instantiated and called as such:
    characters = "abc"
    combinationLength = 2
    obj = CombinationIterator(characters, combinationLength)
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())


if __name__ == '__main__':
    main()
