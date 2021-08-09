"""
추상화 : abstraction
불필요한 정보는 숨기고 중요한(필요한) 정보만을 표현함으로써 
공통의 속성, 값이나 행위(methods)를 하나로 묶어 이름을 붙이는 것.
"""


class Robot:

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    def __init__(self, name, code):
        self.name = name
        self.code = code
        Robot.population += 1

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


print(Robot.population)
siri = Robot("siri", 21039788127)
print(Robot.population)

jarvis = Robot("jarvis", 2324212127)
bixby = Robot("bixby", 12418083)
bixby2 = Robot("bixby2", 12418083)

print(siri.name)
print(siri.code)

siri.say_hi()
siri.cal_add(2, 3)

Robot.how_many()
