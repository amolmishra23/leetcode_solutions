class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        
        for a in asteroids:
          flag = True
          while stk and a<0 and stk[-1]>0:
            # The new stone has destroyed prev stone
            # and may destory many other stones too.
            # so we continue
            if abs(a)>stk[-1]:
              flag = True
              stk.pop()
              continue
            # the new asteriod itself is destroyed.
            # So we break out
            elif abs(a)<stk[-1]:
              flag=False
              break
            # both the asteroids are destroyed.
            # we break out
            else:
              flag=False
              stk.pop()
              break
          # if we had a bigger asteroid we need to append that to the stack.
          if flag:
            stk.append(a)
            
        return stk
              