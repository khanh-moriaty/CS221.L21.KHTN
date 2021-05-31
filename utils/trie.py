import json
from collections import deque
        
class Trie:
    
    def __init__(self):
        self.root = {}
        
    def add(self, s):
        '''
        Add a string into trie.
        '''
        node = self.root
        for x in s:
            if x not in node:
                node[x] = {}
            node = node[x]
        if 'count' not in node:
            node['count'] = 0
        node['count'] += 1
        
    def __getitem__(self, s):
        '''
        Retrieve how many times a string was added.
        '''
        node = self.root
        for x in s:
            if x not in node:
                return 0
            node = node[x]
        if 'count' not in node:
            return 0
        
        return node['count']
    
    def merge(self, t):
        '''
        Merge two trie's, combine their string counts.
        '''
        q = deque()
        q.append((self.root, t.root))
        while len(q) > 0:
            u = q.popleft()
            if 'count' not in u[0]:
                u[0]['count'] = 0
            if 'count' in u[1]:
                u[0]['count'] += u[1]['count']
            for v in u[1]:
                if v == 'count': continue
                if v not in u[0]:
                    u[0][v] = {}
                q.append((u[0][v], u[1][v]))
    
    def _import(self, inp_file):
        with open(inp_file) as fi:
            self.root = json.load(fi)
    
    def _export(self, out_file):
        with open(out_file, 'w') as fo:
            json.dump(self.root, fo)
            
            
if __name__ == '__main__':
    trie1 = Trie()
    trie1.add('hello')
    trie1.add('hell')
    trie1.add('xinchao')
    trie1.add('hello')
    trie2 = Trie()
    trie2.add('heli')
    trie1.merge(trie2)
    print(trie1['heli'])