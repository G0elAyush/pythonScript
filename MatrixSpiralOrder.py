def spiralOrder(A):
        t=0
        b=len(A)
        if b <= 0:
            return
        l=0
        r=len(A[0])
        if r<= 0:
            return
        dirn='r'

        while t<b and l<r:
            if dirn=='r':
                for i in range(l,r):
                    print (A[t][i])
                t+=1
                dirn='d'
            elif dirn == 'd':
                for i in range(t,b):
                    print (A[i][r-1])
                r -=1
                dirn='l'
            elif dirn=='l':
                for i in range(r-1,l-1,-1):
                    print (A[b-1][i])
                b -=1
                dirn = 'u'
            elif dirn == 'u':
                for i in range(b-1,t-1,-1):
                    print (A[i][l])
                l +=1
                dirn = 'r'
