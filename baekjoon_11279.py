# 최대힙
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
			print((-1)*heapq.heappop(result))
	else:
		heapq.heappush(result, (-1)*n)

# 최소힙만 구현하는 heapq에 -1(배열에 가장 뒤)를 적용하면 최대힙이 출력된다.

"""
13
0
1
2
0
0
3
2
1
0
0
0
0
0
"""