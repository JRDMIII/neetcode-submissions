class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for s in strs:
            result.append(str(len(s)))
            result.append('#')
            result.append(s)

        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # read string until we see a hashtag and that is our number
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            i = j + 1
            j = i + length
            res.append(s[i:j])

            i = j

        return res