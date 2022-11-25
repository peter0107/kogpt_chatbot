import numpy as np
import torch

indices=torch.tensor([[[  387,  9036,  9018],
         [  387,  8702,  8811],
         [35381,     1, 24437],
         [  397,   399,   400],
         [ 9265,  9873,  9091]]])

array=indices.numpy()

#print(array[0][0][0])

#print(array[0][1][0])

print("arr: ",array)
array=array.swapaxes(1,2)
print("changed: ",array)
print(array[0][0])
print(array[0][1])
print(array[0][2])
print(torch.tensor(array[0][0]))
