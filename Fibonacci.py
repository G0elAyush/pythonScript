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
if __name__=='__main__':
    objFibonacci = Fibonacci()
    objFibonacci.calculateSum(-1)
    objFibonacci.calculateSum(0)
    objFibonacci.calculateSum(1)
    objFibonacci.calculateSum(2)
    objFibonacci.calculateSum(3)
    objFibonacci.calculateSum(4)
    objFibonacci.calculateSum(5)
    
