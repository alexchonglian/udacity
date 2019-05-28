"""
standard way ((AxB)xC)xD
or (AxB)x(CxD)
or Ax(BxC)xD

W of size axb
Y of size bxc
Z = WxY is of size axc
cost = axbxc

For n matrices A1, A2,..., An where Ai is of size mi-1 x mi
Goal: min cost for computing the product of A1, A2,..., An

Represent multiplication as binary tree

create dp table, fill the upper diagonal
c(i,i) = 0
c(i,j) = min{ c(i,l)+c(l+1,j) + mi-1*ml*mj where i ≤ l ≤ j-1 }

dimensions = [50, 20, 1, 10, 100]
              |  /|  /|  /|  /
              | / | / | / | /
              m0  m1  m2  m3
initialize dp table
c[i,i] = 0
+---------------------------+
|0                          |
|        0                  |
|                0          |
|                        0  |
+---------------------------+
dimensions = [50, 20, 1, 10, 100]
c[0,1] = 50*20*1 = 1000
c[1,2] = 20*1*10 = 200
c[2,3] = 1*10*100 = 1000
+---------------------------+
|0    1000                  |
|        0     200          |
|                0    1000  |
|                        0  |
+---------------------------+
dimensions = [50, 20, 1, 10, 100]
c[0,2] = 0 + 200 + 50*20*10 = 10200
      or 1000 + 0 + 50*1*10 = 1500
c[1,3] = 0 + 1000 + 20*1*100 = 3000
      or 1000 + 0 + 20*10*100 = 21000
+---------------------------+
|0    1000    1500          |
|        0     200    3000  |
|                0    1000  |
|                        0  |
+---------------------------+
dimensions = [50, 20, 1, 10, 100]
c[0,3] = 0 + 3000 + 50*20*100 = 103000
    or 1000 + 1000 + 50*1*100 = 7000
    or 1500 + 0 + 50*10*100 = 51500
+---------------------------+
|0    1000    1500    7000  |
|        0     200    3000  |
|                0    1000  |
|                        0  |
+---------------------------+
"""
def cmm0(dims):
    n = len(dims)-1
    dp = [[0]*n for i in range(n)]
    for w in range(1,n): # w = width
        for i in range(n-w): # i = start index, j = end index
            j = i+w
            mincost = min(
                dp[i][l] + dp[l+1][j] + dims[i]*dims[l+1]*dims[j+1]
                for l in range(i, j))
            dp[i][j] = mincost
            #print(w, i, j, mincost)
    for d in dp: print(d)
    return dp[0][-1]

if __name__ == '__main__':
    dimensions = [50, 20, 1, 10, 100]
    print(cmm0(dimensions))





