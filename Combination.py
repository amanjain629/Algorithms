mod=1000000007
N=5
R=2
if N<R:
    return 0
if (N-R)<R:
    R=N-R
dp=[0]*(R+1)
dp[0]=1
for i in range(1,N+1):
    for j in range(min(i,R),0,-1):
        dp[j]=(dp[j]+dp[j-1])%mod
return dp[R]
