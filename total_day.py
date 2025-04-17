year, mon, day = map(int, input('태어난 연월일을 XXXX.XX.XX식으로 입력해주세요 ex)2025.04.25').split('.'))
Ryear, Rmon, Rday = map(int, input('현재 연월일을 입력헤주세요').split('.'))

#현재 날짜와 태어난 날짜 받기



assert  Ryear > 2025 and Rmon >12 and mon > 12 and day > 31 and Rday > 31, '올바른 년도와 월,일을 입력해 주세요'
#잘못된 값을 입력했을 때의 오류 출력


Dday = 0    
for y in range(year +1, Ryear): # year+1 ~ Ryear-1
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        #(100으로 나누어 떨어지지 않고 4로 나누어 떨어지는 년도) 윤년
      Dday = Dday + 366
    else:
      Dday = Dday + 365


#year, Ryear 월,일 계산

mday = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) and mon <=2:
   #윤년이고 2월이나 그이전에 태어났을때
  Dday =  Dday + mday[mon] +1 - day #태어난 달의 남은 일 수
  for i in range(mon+1, 13):
    Dday = Dday + mday[i]
 
else:
  Dday = Dday + mday[mon] - day
  for j in range(mon+1, 13):
    Dday = Dday + mday[j] 

  
if (Ryear % 4 == 0 and Ryear % 100 != 0) or (Ryear % 400 == 0) and Rmon >=2:
  #현재 년도가 윤년인지 그리고 2월이 지났는지
  Dday = Dday + Rday + 1
  for ri in range(0, Rmon):
    Dday = Dday + mday[ri]
  
else: #윤년이 아니거나 2월이 안지났을때
  Dday = Dday + Rday
  for rj in range(0, Rmon):
    Dday = Dday + mday[rj]
  
print("당신이 살아온 날은 총 :", Dday)
# 산날짜 포함