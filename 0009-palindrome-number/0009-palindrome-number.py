class Solution:
    def isPalindrome(self, x: int) -> bool:
        #x=1000030001
        str1=str(x)
        #print(str1[0])
        j=len(str1)-1
        #print (str1[j])
        #print (int((len(str1)-1)/2))
        for i in range(0,max(1,int((len(str1)-1)/2)+1)):
            #print(str1[i],str1[j])
            if (str1[i]!=str1[j]):
                return False
            j=j-1
        return True


            
        