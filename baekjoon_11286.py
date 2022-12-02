# 절댓값 힙
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
			print(heapq.heappop(result)[1])
			# heapq.heappop(배열[인덱스])
	else:
		heapq.heappush(result, (abs(n),n))
		# heapq.heappush(배열, (우선순위, 값))

# java와 비슷하게 절대값은 abs(number)로 구현!