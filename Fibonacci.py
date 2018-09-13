class Fibonacci:
    def calculateSum(self,n):
        if n < 0:            
            return print("Incorrect input")
        if n ==0:
            return print(0)
        if n ==1:
            return print(0)
        if n == 2:            
            return print(1)
        a=0
        b=1
        sum = a+b
        for i in range(2,n):
            c = a+b
            sum = sum+c
            a=b
            b=c
        return print(sum)
    
    def genFibbonacciSeries(self,n):
        a=[0,1]
        if n== 1:
            return a[:1]
        if n == 2:
            return a
        for i in range(2,n):
            a.append(a[i-2] + a[i-1])
        print(a)
        return a
    def getFibonacciSum(self,n):
        if n <1:
            return print("Incorrect input")
        if n== 1:
            return 0
        a=self.genFibbonacciSeries(n)
        sum = 2*a[n-1] + a[n-2] -1
        print(sum)
        
if __name__=='__main__':
    objFibonacci = Fibonacci()
    objFibonacci.calculateSum(-1)
    objFibonacci.getFibonacciSum(-1)
    objFibonacci.calculateSum(0)
    objFibonacci.calculateSum(1)
    objFibonacci.getFibonacciSum(1)
    objFibonacci.calculateSum(2)
    objFibonacci.getFibonacciSum(2)
    objFibonacci.calculateSum(3)
    objFibonacci.getFibonacciSum(3)
    objFibonacci.calculateSum(4)
    objFibonacci.getFibonacciSum(4)
    objFibonacci.calculateSum(8)
    objFibonacci.getFibonacciSum(8)
    objFibonacci.getFibonacciSum(0)
    
    
