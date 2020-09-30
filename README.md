# Randomized-Select-Algorithm
The Randomized Select Algorithm is a sorting algorithm that is used to find the ith ordered statistics (ith smallest element) of array A. It uses the partition function from the Quicksort Algorithm which results in an expected running time of θ(n). The Randomized Select Algorithm has a worst case running time of θ(n2) and an expected θ(n).

This algorithm is used to solve the selection problem which seeks to find the ith ordered statistic in a set A of n distinct numbers, where 1 ≤ i ≤ n.

***Pseudocode:***

- Initial call: RANDOMIZED-SELECT(A,1,A.length,i)

**RANDOMIZED-SELECT(A,p,r,i)**

if p == r
	return A[p]
q = RANDOMIZED-PARTITION(A,p,r)
k=q-p+1
if i == k
	return A[q]
else if i < k
	return RANDOMIZED-SELECT(A,p,q-1,i)
else
	return RANDOMIZED-SELECT(A,q+1,r,i-k)

**RANDOMIZED-PARTITION(A,p,r)**
i = RANADOM(p,r)
exchange A[r] with A[i]
return PARTITION(A,p,r)

**PARTITION(A,p,r)**
x = A[r]
i = p-1
for j = p to r-1
	if A[j] ≤ x
		i=i+1
		exchange A[i] with A[j]
exchange A[i+1] with A[r]
return i+1
