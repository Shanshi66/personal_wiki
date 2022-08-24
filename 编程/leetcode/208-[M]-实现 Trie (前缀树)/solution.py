from asyncio import FastChildWatcher


class Trie:
    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        p = self.tree
        for ch in word:
            p.setdefault(ch, {})
            p = p[ch]
        p['leaf'] = True

    def search(self, word: str) -> bool:
        p = self.tree
        for ch in word:
            if ch not in p:
                return False
            p = p[ch]
        if 'leaf' not in p:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        p = self.tree
        for ch in prefix:
            if ch not in p:
                return False
            p = p[ch]
        return True

if __name__ == '__main__':
    test = Trie()
    
    main()