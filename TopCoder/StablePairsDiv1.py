class StablePairsDiv1:
    source ="https://community.topcoder.com/stat?c=problem_statement&pm=14891"
    # n = 0
    # c = 0
    # k = 0
    # def __init__(self, n,c,k):
    #     self.n = n
    #     self.c = c
    #     self.k = k

    def constrain(self,number):
        if(number > 100):
            number = 100
        if(number<1):
            number = 1
        return

    def findMaxStablePairs(self,n,c,k):
        # n = 5, c = 4, k = 2
        self.constrain(n)
        self.constrain(c)
        self.constrain(k)
        one_to_n = range(1,n+1)
        arrays = []
        max_array = []
        stable_array = []
        if n is 1:
            max_array = []
        return max_array