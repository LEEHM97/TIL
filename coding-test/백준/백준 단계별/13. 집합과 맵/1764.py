import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_list = []
m_list = []
result = []
cnt = 0

for i in range(n):
    person = input().rstrip()
    n_list.append(person)
    
for _ in range(m):
    person = input().rstrip()
    m_list.append(person)
    
n_list = set(n_list)
m_list = set(m_list)

min_lst = min(n, m)

if min_lst == n:
    for i in n_list:
        if i in m_list:
            cnt += 1
            result.append(i)

else:
    for i in m_list:
        if i in n_list:
            cnt += 1
            result.append(i)
 
result.sort()            

print(cnt)
for i in result:
    print(i)