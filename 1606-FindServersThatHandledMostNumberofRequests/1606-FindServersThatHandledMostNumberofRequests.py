# Last updated: 11/11/2026, 1:34:56 AM
1class Solution:
2    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
3
4        # add servers dealing with requests to a heap with arrival[i] + load[i]
5        # maintain a sorted set of servers that are available
6        #
7
8        max_requests = 0
9        max_servers = []
10        count = [0] * k
11        avail_servers = SortedSet()
12        for i in range(k):
13            avail_servers.add(i)
14        server_heap = []
15        for i in range(len(arrival)):
16            z = 0
17            found = False
18            while server_heap and server_heap[0][0] <= arrival[i]:
19                server = heapq.heappop(server_heap)
20                avail_servers.add(server[1])
21            if avail_servers:
22                mod = (i + z) % k
23                idx = avail_servers.bisect_left(mod) % len(avail_servers)
24                server = avail_servers[idx]
25
26                heapq.heappush(server_heap, (arrival[i] + load[i], server))
27                avail_servers.remove(server)
28                count[server] += 1
29                if count[server] > max_requests:
30                    max_requests = count[server]
31                    max_servers = [server]
32
33                elif count[server] == max_requests:
34                    max_servers.append(server)
35 
36                
37
38        return max_servers