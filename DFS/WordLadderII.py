<<<<<<< HEAD
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        words_list = set(wordList)
        if endWord not in words_list:
            return []
        neighbors, path, paths = collections.defaultdict(list), [beginWord], []
        is_found = self.bfs(set([beginWord]), set([endWord]), neighbors, True, words_list)
        return self.construct_paths(beginWord, endWord, neighbors)
    
    def construct_paths(self, source, dest, neighbors):
        if source == dest: 
            return [[source]]
        return [[source] + path for neighbor in neighbors[source]
                                for path in self.construct_paths(neighbor, dest, neighbors)]

    def add_path(self, neighbors, word, neigh, is_forwd):
        if is_forwd: 
            neighbors[word]  += neigh,
        else:       
            neighbors[neigh] += word,

    def bfs(self,left_lev, right_lev, neighbors, is_forwd, words_set):
        if not left_lev: 
            return False
        if len(left_lev) > len(right_lev):
            return self.bfs(right_lev, left_lev, neighbors, not is_forwd, words_set)
        for word in (left_lev | right_lev):
            words_set.discard(word)
        next_lev, done = set(), False
        while left_lev:
            word = left_lev.pop()
            for c in string.ascii_lowercase:
                for index in range(len(word)):
                    neigh = word[:index] + c + word[index+1:]
                    if neigh in right_lev:
                        done = True
                        self.add_path(neighbors, word, neigh, is_forwd)                
                    if not done and neigh in words_set:
                        next_lev.add(neigh)
                        self.add_path(neighbors, word, neigh, is_forwd)
        return done or self.bfs(next_lev, right_lev, neighbors, is_forwd, words_set)
=======
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        words_list = set(wordList)
        if endWord not in words_list:
            return []
        neighbors, path, paths = collections.defaultdict(list), [beginWord], []
        is_found = self.bfs(set([beginWord]), set([endWord]), neighbors, True, words_list)
        return self.construct_paths(beginWord, endWord, neighbors)
    
    def construct_paths(self, source, dest, neighbors):
        if source == dest: 
            return [[source]]
        return [[source] + path for neighbor in neighbors[source]
                                for path in self.construct_paths(neighbor, dest, neighbors)]

    def add_path(self, neighbors, word, neigh, is_forwd):
        if is_forwd: 
            neighbors[word]  += neigh,
        else:       
            neighbors[neigh] += word,

    def bfs(self,left_lev, right_lev, neighbors, is_forwd, words_set):
        if not left_lev: 
            return False
        if len(left_lev) > len(right_lev):
            return self.bfs(right_lev, left_lev, neighbors, not is_forwd, words_set)
        for word in (left_lev | right_lev):
            words_set.discard(word)
        next_lev, done = set(), False
        while left_lev:
            word = left_lev.pop()
            for c in string.ascii_lowercase:
                for index in range(len(word)):
                    neigh = word[:index] + c + word[index+1:]
                    if neigh in right_lev:
                        done = True
                        self.add_path(neighbors, word, neigh, is_forwd)                
                    if not done and neigh in words_set:
                        next_lev.add(neigh)
                        self.add_path(neighbors, word, neigh, is_forwd)
        return done or self.bfs(next_lev, right_lev, neighbors, is_forwd, words_set)
>>>>>>> 939b0502f1c705121dae8d24aaecb61943ad3e7d
        