class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()

        occ = {c:i for i,c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < occ[stack[-1]]:
                    seen.discard(stack.pop()) 
                seen.add(c)
                stack.append(c)
        return ''.join(stack)
