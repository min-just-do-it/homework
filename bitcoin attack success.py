import math

q = 0.1
print("q=",q)
def attack(q, z):
    p = 1.0 - q
    lambda_ = z * (q / p)
    total = 1.0
    #사건이 일어날 최대 확률



#푸아송 정리


    for k in range(z + 1): #시그마
        Sum = math.exp(-lambda_)   #e^lambda
        for i in range(1, k + 1):   
            Sum =Sum * lambda_ / i     #e^lambda * lambda/k (1<=k<=z)
        total = total - Sum * (1 - (q / p) ** (z - k))  #q / p^(z - k)

#gpt 도움 받음
    return total

for z in range(11):  # 0부터 10까지
    prob = attack(q, z)
    print("z=",z, f"q= {prob:.7f}")
