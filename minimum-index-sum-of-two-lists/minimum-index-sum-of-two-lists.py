import itertools   
​
class Solution:
    """         0         1                   2         3
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
               0          1              2             3
    list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
                 0            1                2        3
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
               0     1          2              3             4
    list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
    """
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        for i, item in enumerate(list1):
            d[item] = i
        
        min_index_sum = math.inf
        res = []
        for i, item in enumerate(list2):
            if item in d:
                if d[item] + i == min_index_sum:
                    res.append(item)
                elif d[item] + i < min_index_sum:
                    min_index_sum = d[item] + i
                    res = []
                    res.append(item)
        return res
                    
