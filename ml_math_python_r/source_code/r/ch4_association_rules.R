install.packages('arules')
install.packages('arulesViz')
library(arules)
library(arulesViz)

# Groceries 데이터
library(datasets)
data("Groceries")
Groceries

# 많이 발생하는 아이템 상위 20개 출력
itemFrequencyPlot(Groceries, topN=20, type='absolute')

# 연관 규칙 분석을 위한 Apriori 알고리즘 적용하고 시각화
# 최소 지지도 0.1%, 최소 신뢰도 80%
rules <- apriori(Groceries, parameter = list(supp=0.001, conf = 0.8))
summary(rules)
plot(rules)

# Apriori 알고리즘 결과 필터링하기

# 결과 중 처음 5개만 출력
inspect(rules[1:5])

# 신뢰도 기준으로 내림차순의 패턴들을 rules에 할당
rules <- sort(rules, by='confidence', decreasing = TRUE)
inspect(rules[1:5])
