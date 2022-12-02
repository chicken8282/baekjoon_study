# 최소힙
from sys import stdin
import heapq

x = int(stdin.readline())
result = []

for _ in range(x):
	n = int(stdin.readline())
	if n == 0:
		if not result:
			print("0")
		else:
			print(heapq.heappop(result))
	else:
		heapq.heappush(result, n)