#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    @staticmethod
    def defangIPaddr(address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".","[.]")
        
        
        
address = "255.100.50.0"
Solution.defangIPaddr(address)

