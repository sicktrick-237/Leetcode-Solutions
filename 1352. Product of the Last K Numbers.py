# from functools import reduce
#
# class ProductOfNumbers(object):
#
#     def __init__(self):
#         self.numList = []
#         self.productList = []
#
#     def add(self, num):
#         self.numList.append(num)
#         if len(self.numList) > 1:
#             self.productList.append(self.productList[-1] * num)
#         else:
#             self.productList.append(1)
#         print(self.productList)
#
#
#
#     def getProduct(self, k):
#         pass
#         # product = reduce(lambda x,y: x*y, self.numList[-k:])
#         # print(product)
#         # return product
#
# nums = [3,1,2,5,4]
# prodls = [3, 3, 6, 30, ]
# k = 2
#
# obj = ProductOfNumbers()
#
# for each in nums:
#     obj.add(each)
#
# obj.getProduct(k)

prd_tbl = [1, 3, 3, 6, 24]

print(prd_tbl[-1]//prd_tbl[-(2+1)])

print(24//3)