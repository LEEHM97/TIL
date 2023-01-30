import sys
imput = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

for i in m_list:
    if binary_search(n_list, i, 0, len(n_list)) != None:
        print('yes')
    else:
        print('no')