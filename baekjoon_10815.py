# 숫자카드
from sys import stdin

N = int(stdin.readline())
Ncard = set(map(int,stdin.readline().split()))
M = int(stdin.readline())
Mcard = list(map(int,stdin.readline().split()))

for i in Mcard:
	if i in Ncard:
		print(1, end=" ")
	else:
		print(0, end=" ")

