# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 00:58:39 2019

@author: omkar.kadam
"""

lstele = [1,7]
lstele = list(set(lstele))
lstele.sort(reverse=True)

def srtele(lstele):
    if len(lstele) > 1:
        return(lstele[1])
    elif len(lstele) !=0:
        return lstele[0]
    else:
        return

secondele = srtele(lstele)
