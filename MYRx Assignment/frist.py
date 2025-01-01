
# Given a sorted array of positive and negative numbers. You have to Square it and sort it. 
# Input= [-12, -8 , -7, -5, 2, 4, 5, 11, 15] 
# output=  [4, 16, 25, 25, 49, 64, 121, 144, 225] 

Input= [-12, -8 , -7, -5, 2, 4, 5, 11, 15]

sqrNums=[]
for i in Input:
    sqrNums.append(abs(i*i))
sqrNums.sort()
print(sqrNums) # output=  [4, 16, 25, 25, 49, 64, 121, 144, 225] 