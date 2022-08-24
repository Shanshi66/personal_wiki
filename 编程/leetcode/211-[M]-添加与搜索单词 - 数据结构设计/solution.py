class WordDictionary:
    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        p = self.tree
        for ch in word:
            p.setdefault(ch, {})
            p = p[ch]
        p['leaf'] = True

    def _search(self, word_dict, word, idx):
        if idx == len(word):
            return 'leaf' in word_dict
        if word[idx] != '.' and word[idx] in word_dict:
            return self._search(word_dict[word[idx]], word, idx+1)
        if word[idx] == '.':
            for key in word_dict:
                if key == 'leaf':
                    continue
                if self._search(word_dict[key], word, idx+1):
                    return True
        return False

    def search(self, word: str) -> bool:
        return self._search(self.tree, word, 0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)