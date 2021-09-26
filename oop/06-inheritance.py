"""
[클래스 상속]

1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속

2. 자식 클래스에서 별도 메서드나 속성 추가 가능

3. 메서드 오버라이딩

4. super()

5. python의 모든 클래스는 object 클래스를 상속 : 모든 건 객체

6. MyClass.mro() -> 상속관계를 보여줌

"""


class Robot:

    """
    [Robot Class]
    Author : 송진영
    Role : blahblah
    """

    population = 0

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}")

    def cal_add(self, a, b):
        return a + b

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one")
        else:
            print(f"There are still {Robot.population} robots working.")

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} robots.")

    @staticmethod
    def are_you_robot():
        print("yes!!")

    def __str__(self):
        return f"{self.name} robot!!"

    def __call__(self):
        print("call!")
        return f"{self.name} call!"


class Siri(Robot):
    pass

# 상속받았기 때문에 인스턴스 변수 필요
# siri = Siri()
# print(siri)

siri = Siri("iphone8")
print(siri)
print(siri.are_you_robot())
print(siri.cal_add(17, 19))