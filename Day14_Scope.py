class Difference:
    def __init__(self, a):
        self.__elements = a
        
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        results = []
        arr = list(set(self.__elements))
        l1 = len(arr)
        
        if l1 ==1: 
            return 
        for i in range(l1):
            if i == l1 -1:
                self.maximumDifference = max(results)
                return
            for j in range(i+1, l1):
                results.append(abs(arr[i]-arr[j]))



# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
