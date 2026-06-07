# Last updated: 6/7/2026, 3:13:31 PM
1class Codec:
2
3    def serialize(self, root):
4        result = []
5        
6        def dfs(node):
7            if node is None:
8                result.append('N')
9                return
10            result.append(str(node.val))
11            dfs(node.left)
12            dfs(node.right)
13        
14        dfs(root)
15        return ','.join(result)
16
17
18    def deserialize(self, data):
19        vals = iter(data.split(','))
20        
21        def dfs():
22            val = next(vals)
23            if val == 'N':
24                return None
25            node = TreeNode(int(val))
26            node.left = dfs()
27            node.right = dfs()
28            return node
29        
30        return dfs()