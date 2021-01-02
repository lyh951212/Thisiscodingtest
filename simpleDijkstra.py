import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수 입력받기
n,m = map(int, input().split())
#시작 노드 번호
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[]for _ in range(n+1)]
#방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
#최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선정보를 입력받기
for _ in range(m):
	a,b,c = map(int, input().split())
	#a번 노드에서 b번 노드로 가는 비용이 c이다
	graph[a].append((b,c))

def nearest_neigbor():
	mindist = INF
	minnode = 0

	for node in range(1,n+1):
		if visited[node] == True:
			continue
		if mindist > distance[node]:
			mindist = distance[node]
			minnode = node
	return minnode
		
def dijkstra(start):
	#자기자신까지의 거리는 0이다
	distance[start] = 0
	visited[start] = True

	#시작노드에 인접한 모든 노드의 최단거리 테이블 초기화한다
	for j in graph[start]:
		distance[j[0]] = j[1]

	#시작노드를 제외한 나머지 노드
	for node in range(n-1):
		now = nearest_neigbor()
		visited[now] = True

		for j in  graph[now]:
			if distance[j[0]] > distance[now] + j[1]:
				distance[j[0]] = distance[now] + j[1]
		
dijkstra(1)

