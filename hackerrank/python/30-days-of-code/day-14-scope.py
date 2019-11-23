class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        length = len(a)
        for i in range(0, length):
            for j in range(i + 1, length):
                difference = abs(a[i] - a[j])
                self.maximumDifference = max(
                    difference, self.maximumDifference)
