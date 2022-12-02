# 여행가자
from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())

road = [stdin.readline().split() for _ in range(n)]
print(road)
city = list(map(str,stdin.readline().split()))
print(city)