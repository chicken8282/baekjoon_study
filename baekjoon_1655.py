# 가운데를 말해요

from sys import stdin
import heapq

n = int(stdin.readline())
leftheap = []
rightheap = []
for _ in range(n):
	x = int(stdin.readline())
	if len(leftheap) == len(rightheap):
		heapq.heappush(leftheap,-x)
	else:
		heapq.heappush(rightheap,x)

	if rightheap and rightheap[0] < -leftheap[0]:
		leftvalue = heapq.heappop(leftheap)
		rightvalue = heapq.heappop(rightheap)

		heapq.heappush(leftheap,-rightvalue)
		heapq.heappush(rightheap,-leftvalue)
	print(-leftheap[0])

# leftheap(최대힙), rightheap(최소힙)에 번갈아 x를 입력하고 leftheap의 첫번째 인자가 중앙값이 된다.
# 만약 rightheap[0]이 -leftheap[0]보다 작다면 서로의 첫번째 인자를 바꾼다.