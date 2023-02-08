import sys
sys.stdin
length = int(input())

for x in range(length):
    arr = list(*map(lambda x,y: (int(x)+int(y) , int(y)*int(x)), *input().rstrip().split()))
    print(*arr, sep=" ")
    pass
