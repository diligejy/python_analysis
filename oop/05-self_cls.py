# self는 인스턴스 객체다
# 클래스 안에 있는 self 주소와 만들어진 인스턴스의 주소는 같다
# 즉, self는 인스턴스 그 자체이다



class SelfTest:

    # 클래스 변수
    name = "amamov"

    def __init__(self, x):
        self.x = x

    # 클래스 메서드
    @classmethod
    def func1(cls):
        print(f"cls: {cls}")
        print("func1")

    # 인스턴스 메서드
    def func2(self):
        print(f"self : {self}")
        print("class안의 self 주소 : ", id(self))
        print("func2")

test_obj = SelfTest(17)
test_obj.func2()

SelfTest.func1()
print("인스턴스의 주소: ", id(test_obj))

# 인스턴스에서 classmethod 실행했더니 class 호출
print('---')
test_obj.func1()

# 인스턴스에서 클래스변수 호출했더니 class변수 호출
print('---')
print(test_obj.name)

# 클래스에서 인스턴스 변수, 메서드 호출 가능? -> No
# print(SelfTest.func2())
# print(SelfTest.x)