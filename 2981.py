import math

loop = int(input())

# N을 받아준다.
num = []
for _ in range(loop):
    num.append(int(input()))
num.sort()

# M은 인접한 값의 차이들의 공약수
num_d = []
for i in range(1,len(num)):
    num_d.append(num[i]-num[i-1])

# gcd를 구하기 위해 함수 사용 (list를 넣기 위해선 *가 필요)
g = math.gcd(*num_d)

M = [g]
for m in range(2,int(math.sqrt(g))+1):
    if (g % m==0):
        M.append(m)
        M.append(g//m)

M = list(set(M))
M.sort()
print(*M)
