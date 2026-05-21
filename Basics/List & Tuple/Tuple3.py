#maximum and minmum K elements in a tuple

t=(1,2,3,5)
k=2
print("original tuple= ",t)
sorted_t=sorted(t)
print("min= ",sorted_t[ :k])
print("max= ",sorted_t[-k: ])