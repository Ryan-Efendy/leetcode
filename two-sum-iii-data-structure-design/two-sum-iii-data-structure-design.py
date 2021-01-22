from sortedcontainers import SortedList
​
class TwoSum:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = SortedList()
        
​
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.list.add(number)
​
    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        i, j = 0, len(self.list)-1
        while i < j:
            sum = self.list[i] + self.list[j]
            if sum == value: return True
            elif sum > value: j -= 1
            else: i += 1
        return False
​
​
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
