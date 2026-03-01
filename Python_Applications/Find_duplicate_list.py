lst = [2,1,1,6,7,7, 6, 5, 4, 3, 2]

unique= []

for i in lst:
    if i not in unique:
        unique.append(i)
        
print(unique)


lis1 = [7,3,4,7,3,4,8,3,8,2,1,9]

freq={}

for i in lis1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)