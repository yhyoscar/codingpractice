class Solution:
    def wordBreak(self, s, wordDict):
        print(s)
        print(wordDict)
        method = 'memory'
        if method == 'memory':
            start = {i:{} for i in range(len(s)+1)}
            for word in wordDict:
                for i in range(0, len(s)-len(word)+1):
                    if s[i:i+len(word)] == word:
                        start[i][word] = []
            start[len(s)] = {s:[]}
            
            for i in range(len(start)):
                if len(start[i])>0:
                    for x in start[i]:
                        if i+len(x) <= len(s):
                            for y in start[i+len(x)]:
                                start[i+len(x)][y].append( (i, x) )
            
            for x in start:
                print(x, start[x])
            
            sout = []
            if len(start[len(s)]) > 0:
                for x in start[len(s)][s]:
                    self.memory_dfs(start, x[0], x[1], sout, [])
            
            sout = [' '.join(x[::-1]) for x in sout]

            return sout

        
        if method == 'allrec':
            out = []
            loc = []
            self.recur(s, wordDict, out, loc)

            sout = []
            for x in out:
                sout.append('')
                x = x[::-1]
                x.append(len(s))
                for i in range(len(x)-1):
                    sout[-1] += ' '+s[x[i]:x[i+1]]
                sout[-1] = sout[-1][1:]
            return sout

    def memory_dfs(self, start, i, key, out, slist):
        if i == 0:
            out.append(slist+[key])
        else:
            for x in start[i][key]:
                self.memory_dfs(start, x[0], x[1], out, slist+[key])

    
    def recur(self, s, d, out, loc):
        if len(s)==0:
            out.append(list(loc))
            return
        else:
            for x in d:
                i = len(s)-len(x)
                if i>=0:
                    if s[i:] == x:
                        loc.append(i)
                        self.recur(s[:i], d, out, loc)
                        loc.pop()
            return
    
#s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]

#s = "pineapplepenapple"
#wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

print( Solution().wordBreak(s, wordDict) )


