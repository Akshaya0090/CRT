'''arr = np.array([10,20,30])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
print("even numbers:",np.arange(2,10,2))
print("odd numbers: ", np.arange(1,10,2))'''
import numpy as np
n = int(input ("enter:"))
ele = list(map(int,input().split()))
print("arr elements are:" ,np.array(ele))
