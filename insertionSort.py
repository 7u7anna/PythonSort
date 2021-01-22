# Function
def insertionSort(T):
    n=len(T)
    for i in range(n):
        pom=T[k]
        k=i-1
        while k>=0 and T[k]>pom:
           T[k+1]=pom
           i+=1
        T[k+1]=T[k]
        k-=1
     return T

#Example
from random import randint
X = [randint(1,100) for i in range(20)]
print(X)
insertionSort(X)
print(X)
