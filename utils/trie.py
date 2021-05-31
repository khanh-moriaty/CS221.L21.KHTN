import json
        
class Trie:
    
    def __init__(self):
        self.root = {'count': 0}
        
    def add(self, s):
        node = self.root
        for x in s:
            if x not in node:
                node[x] = {'count': 0}
            node = node[x]
        node['count'] += 1
        
    def __getitem__(self, s):
        node = self.root
        for x in s:
            if x not in node:
                return 0
            node = node[x]
        return node['count']
    
    def _import(self, inp_file):
        with open(inp_file) as fi:
            self.root = json.load(fi)
    
    def _export(self, out_file):
        with open(out_file) as fo:
            json.dump(self.root, fo)
            
if __name__ == '__main__':
    trie = Trie()
    trie.add('hello')
    trie.add('hell')
    trie.add('xinchao')
    trie.add('hello')
    print(trie['hello'])