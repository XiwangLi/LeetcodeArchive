class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ''
        if numerator / denominator < 0: 
            res += '-'
        if numerator % denominator ==0: 
            return str(numerator / denominator)
        
        numerator=abs(numerator)
        denominator=abs(denominator)
        
        res += str(numerator/denominator)
        res += "."
        numerator %= denominator
        i=len(res)
        res_hash = {}
        while numerator != 0:
            if numerator not in res_hash.keys():
                res_hash[numerator] = i  #if the value has not appeared, then add it to the hash table
            else:
                i = res_hash[numerator]  # there is a cycle
                res = res[:i] + "(" + res[i:] + ")"
                return res
            numerator = numerator * 10
            res += str(numerator / denominator) 
            numerator %= denominator
            i += 1
        return res
        
model = Solution()
print model.fractionToDecimal(2, 3)