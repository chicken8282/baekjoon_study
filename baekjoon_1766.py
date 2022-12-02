# 문제집
from sys import stdin
import heapq

n,m = map(int,stdin.readline().split())
answer = []
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
result = []

for i in range(m):
	fs, se = map(int,stdin.readline().rstrip().split())
	graph[fs].append(se)
	indegree[se] += 1

for i in range(1, n+1):
	if indegree[i] == 0:
		heapq.heappush(result,i)
while result:
	tmp = heapq.heappop(result)
	answer.append(tmp)
	for i in graph[tmp]:
		indegree[i] -= 1
		if indegree[i] == 0:
			heapq.heappush(result,i)
print(" ".join(map(str,answer)))

# 우선순위 큐
# DFS
# 위상 정렬