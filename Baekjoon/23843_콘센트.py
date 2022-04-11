import sys
import heapq

N, M = map(int, input().split())
electronics = list(map(int, sys.stdin.readline().split()))
electronics.sort(reverse=True)
heap = []

for e in electronics:
    if len(heap) < M:  # 콘센트 자리 남아있다면
        heapq.heappush(heap, e)
    else:  # 콘센트 가득 차있음
        out = heapq.heappop(heap)  # 충전 가장 빨리 끝나는놈 뽑고
        heapq.heappush(heap, out + e)  # 그자리에 충전

print(max(heap))

s = "zzjfkkfdfwjfffw"
print(sorted(s, key=s.find))