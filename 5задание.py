values = [3,1,2,3,2,1,6]
other = {7,9,5,2}
uniq_values = set(values)
n= len(uniq_values)
print(n)
i = uniq_values & other
y= uniq_values|other
l = uniq_values - other
j = other - uniq_values
print(i,y,l,j)








