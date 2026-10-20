# Last updated: 10/20/2026, 2:18:42 AM
1class ProductOfNumbers:
2
3    def __init__(self):
4        self.arr = []
5        self.last_zero = -1
6    def add(self, num: int) -> None:
7        if num == 0:
8            self.last_zero = len(self.arr)
9            self.arr.append(1)
10
11        elif not self.arr:
12            self.arr.append(num)
13        else:
14            self.arr.append(self.arr[-1] * num)
15
16    def getProduct(self, k: int) -> int:
17        if len(self.arr) - (k) <= self.last_zero:
18            return 0
19        if len(self.arr) == k:
20            return self.arr[-1]
21        return self.arr[-1] // self.arr[-(k + 1)]
22        
23
24
25# Your ProductOfNumbers object will be instantiated and called as such:
26# obj = ProductOfNumbers()
27# obj.add(num)
28# param_2 = obj.getProduct(k)