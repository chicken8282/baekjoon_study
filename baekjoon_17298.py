# 오큰수
from sys import stdin

n = int(stdin.readline())
A = list(map(int,stdin.readline().rstrip().split()))
answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
	while stack and A[stack[-1]] < A[i]:
		answer[stack.pop()] = A[i]
	stack.append(i)

print(*answer)

# answer = [-1,-1,-1,-1]로 만들어놓고 조건에 부합하는 인덱스는 A[i]로 변형한다.

# 스택
"""
4
3 5 2 7

4
9 5 4 8
"""