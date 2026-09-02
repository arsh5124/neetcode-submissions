class Solution:

    def encode(self, strs):
        return ''.join(str(len(s)) + '#' + s for s in strs)

    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i + length])
            i += length

        return res