class Solution:
     def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
            deck.sort()
            res = collections.deque()
            res.append(deck.pop())
            while deck:
                res.appendleft(res.pop())
                res.appendleft(deck.pop())
            return list(res)
