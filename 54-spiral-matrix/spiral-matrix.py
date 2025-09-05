class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        while len(matrix): #Process would be repeated unless the length of matrix becomes zero.
            try: # Exception handling, in case the pop operation on empty matrix is performed.
                ans+=matrix.pop(0) #Removing Top Row from matrix and inserting into answer list.
                ans+=[i.pop() for i in matrix] #Removing Rightmost Column from matrix and inserting into answer list.
                ans+=matrix.pop()[::-1] #Removing Bottom Row from matrix and inserting into answer list in reverse order.
                ans+=[i.pop(0) for i in matrix][::-1] #Removing Leftmost Column from matrix and inserting into answers list in reverse order.
            except:
                break
        return ans