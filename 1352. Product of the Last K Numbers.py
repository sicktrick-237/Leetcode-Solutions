import math

class ProductOfNumbers(object):

    def __init__(self):
        self.numList = []
        

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.numList.append(num)
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        return math.prod(self.numList[-k:])
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)