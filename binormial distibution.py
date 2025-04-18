n = int(input('정수 범위 내에서 시행횟수를 입력해주세요'))   #시행횟수
p = float(input('실수 범위 내에서 성공확률를 입력해주세요')) #성공확률
def fact(n): #팩토리얼 계산
    nFact = 1
    for i in range(n, 0, -1):
        nFact *= i
    return nFact


print("시행횟수=",n, "성공확률=",p)

r = 0  #X 변수 역할(조건)
for r in range(0, n+1):
    combine = fact(n)/(fact(r)*fact(n-1)) #조합
    results = combine*p**r*(1-p)**(n-r) #조합 * p^x * q^(n-x) q는 실패 확률
    print("X=",r, f"P={results:.7f}")
print(f"E(X)={n * p}")          #이항분포의 기댓값
print(f"Var(X)={n*p*(1-p)}")    #이항분포의 분산