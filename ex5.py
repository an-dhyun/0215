name = input('이름 : ')
kor = int(input('국어 : '))
eng = int(input('영어 : '))
math = int(input('수학 : '))
tot = kor + eng + math
avg = tot / 3
grade = None
if 90 <= avg <= 100: grade = 'A'
elif 80 <= avg < 90 : grade = 'B'
elif 70 <= avg < 80 : grade = 'C'
elif 60 <= avg < 70 : grade = 'D'
else : grade  = 'F'
print('이름 = %s, 국어 = %d, 영어 = %d, 수학 = %d'%(name, kor, eng, math))
print('총점 = %d, 평균 = %.2f, 평점 = %s'%(tot, avg, grade)) 