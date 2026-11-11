# Last updated: 11/10/2026, 10:43:50 PM
1class Solution:
2    def minRemoveToMakeValid(self, s: str) -> str:
3        stack = []
4        remove = set()
5
6        for i, c in enumerate(s):
7            if c == '(':
8                stack.append(i)
9            elif c == ')':
10                if stack:
11                    stack.pop()
12                else:
13                    remove.add(i)
14
15        remove.update(stack)
16
17        return ''.join(c for i, c in enumerate(s) if i not in remove)
18        