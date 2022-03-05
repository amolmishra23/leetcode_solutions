class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        You begin with all the cards uncovered and taken from a deck, so deck is empty.

        First you sort the deck, those are uncovered cards.
        Then you do the backward process. Take each uncovered card from the end (in descending
        order).
        If cards in the deck, put the bottom card of the deck, at top of the deck. 
        Take the bottom card of the deck, and add it to top of the deck. 
        
        Take the top card of the deck, reveal it, and take it out of the deck.
        Opposite: Take the bottom card of the deck, and add it back to the deck. 
        If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
        Opposite: If cards in the deck, put the bottom card of the deck, at top of the deck. 
        
        Left side is considered as top, and right side is considered as bottom. 
        
        """

        d = collections.deque()
        deck.sort(reverse=True)
        for i in deck:
            if d:
                d.appendleft(d.pop())
            d.appendleft(i)
        return list(d)