class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five=0 ; ten =0

        for i in bills:
            #iteration of all

            #if it is 5
            if i == 5:
                #add one to five 
                five+=1
            
            #if it is 10
            elif i == 10 :
                #add one to 10 ; remove form 5
                if five:
                    five-=1
                    ten+=1
                #if no change of 5 rs
                else:
                    return False
            
            #if it is 20
            else:
                #check if we have 5 and 10
                if five and ten:
                    five-=1 
                    ten-=1
                #if it has therr or more 5s
                elif five>=3:
                    five-=3
                #if not then return false
                else:
                    return False
        
        return True