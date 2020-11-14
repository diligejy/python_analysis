f <- function(x){
  print(x)
  return(x^2)
}

# 2. x^3 + 3x^2 - 6x - 8 미분하고 그래프 그리기
# 수식을 함수로 표현
f <- function(x) (x^3 + 3 * x^2 - 6 * x - 8)
# curve()함수를 통해 그래프 그리기
curve(f, -5, 4, ylab = "y = f(x)")

# 미분하고 그래프 그리기
g <- function(x){}
body(g) <- D(body(f), 'x')
curve(g, -5, 4, ylab = 'g(x)')

# 3. 함수 integrate()로 적분하기
# x^2 + 1 적분하기
f2 = function(x)(x^2 + 1)
integrate(f2, lower=0, upper = 1)
# g 적분하기
integrate(g, lower = 0, upper = 10)
f(10) - f(0)

# 4. 미적분 응용하기 - 뉴턴랩슨 메서드
# f(x) = 0인 x를 찾기
newton = function(f, tol = 1e-7, x0 = 1, N = 100){
  h = 1e-7;
  i = 1
  x1 = x0;
  p = numeric(N)
  while(i <= N){
    df.dx = (f(x0 + h) - f(x0)) / h
    x1 = (x0 - (f(x0) / df.dx))
    p[i] = x1
    i = i + 1
    if(abs(x1 - x0) < tol) break
    x0 = x1

    }
}