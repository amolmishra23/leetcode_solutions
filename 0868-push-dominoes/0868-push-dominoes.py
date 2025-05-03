class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d= list(dominoes)

        q = deque([(x,i) for i, x in enumerate(d) if x!="."])
        print(q)
        
        while q:
            curr, i = q.popleft()

            if curr == "L" and i>0 and d[i-1]==".":
                # making the next domino tilt
                d[i-1]="L"
                # this step is important, because we keep making the domino fall
                q.append(("L", i-1))
            elif curr == "R":
                if i<len(d)-1 and d[i+1]==".":
                    if i<len(d)-2 and d[i+2]=="L":
                        # because the right and left are balancing each other, we remove the left tilt
                        q.popleft()
                    else:
                        # making the next domino tilt
                        d[i+1] = "R"
                        # this step is important, because we keep making the domino fall
                        q.append(("R", i+1))

        return "".join(d)
            