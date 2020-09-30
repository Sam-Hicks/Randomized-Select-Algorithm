#Randomized-Select Algorithm
#Author: Samuel Hicks
import random

def RANDOMIZED_SELECT(A,p,r,i):
    if p == r:
        return A[p]
    
    q = RANDOMIZED_PARTITION(A,p,r) #q is index of pivot
    k = q-p+1

    if i == k:
        return A[q]
    elif i < k:
        return RANDOMIZED_SELECT(A,p,q-1,i)
    else:
        return RANDOMIZED_SELECT(A,q+1,r,i-k)
    

def PARTITION(A,p,r):
    x = A[r] #Pivot
    i = p-1
    
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def RANDOMIZED_PARTITION(A,p,r):
    i = random.randrange(p,r)
    A[r], A[i-1] = A[i-1], A[r]
    return PARTITION(A,p,r)


n = 20000 #Initial input size
A = [] #Array A
i = (2*n)//3 #ith ordered statistic

for k in range(20000): #Loop for generating 20,000 random numbers in the array A
    rand_num = random.randint(0,32767) #Generate a random number
    A.append(rand_num) #Append the number to the array A

# print(A) #For showing the numbers in the array

print("\nn:",n) #Input size
print("ith ordered statistic:",RANDOMIZED_SELECT(A,0,n-1,i)) #Call to the algorithm