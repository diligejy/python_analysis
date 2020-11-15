# 1. 이항 분포 만들고 계산하기
set.seed(0)
x <- rbinom(1000, 10, 0.3) # n = 10, p = 0.3인 이항 분포에서 난수 1,000개 발생
hist(x)

# 평균
mean(x)
# 분산
var(x)

# 2. 포아송 분포를 만들고 히스토그램 그리기
rx = rpois(3000, 2) # 포아송 분포에서 lambda는 2, 난수 3,000개 생성
mean(rx)
var(rx)
hist(rx, probability = TRUE) # y축에 확률 값을 지정한 히스토그램

# 3. 정규 분포 만들고 히스토그램 그리기
rnorm(1, 100, 15) # 평균 100, 편차 16인 정규분포에서 난수 1개 생성
x = rnorm(100) # 표준 정규 분포에서 난수 100개 생성
hist(x, probability = TRUE)
curve(dnorm(x), add = T) # 정규분포 PDF 표현, 곡선 추가

# 4. t 분포 만들고 히스토그램 그리기
x = rt(100, df = 3) # t 분포에서 자유도 3으로 난수 100개 생성
hist(x, probability = TRUE)
curve(dt(x, 3), add = T) # t 분포 PDF 표현, 곡선 추가

# 5. 카이제곱 분포 만들고 히스토그램 그리기
x = rchisq(100, 1) # 자유도 1에서 난수 100개 생성
hist(x, probability = TRUE)
curve(dchisq(x, 1), add=T)

# 6. 정규성 검정하기
x <- rnorm(100, mean=0) # 정규 분포에서 난수 100개 생성성
shapiro.test(x) # 정규성 검정, 정규 분포를 따름름

# 7. 쌍체 t 검정 
x1 <- c(51.4, 52.0, 45.5, 54.5, 52.3, 50.9, 52.7, 50.3, 53.8, 53.1)
x2 <- c(50.1, 51.5, 45.9, 53.1, 51.8, 50.3, 52.0, 49.9, 52.5, 53.0)
t.test(x1, x2, paired = TRUE, conf.level=0.95)

# 8. 카이제곱 검정
freq = c(22, 21, 22, 27, 22, 36) # 주사위를 150번 던졌을 때 눈별로 나온 빈도
probs = c(1, 1, 1, 1, 1, 1) / 6 # 이론적으로 각 눈은 동일한 확률로 나오는 것을 표현
chisq.test(freq, p=probs)
