"""
# namespace : 개체를 구분할 수 있는 범위
# __dict__ : 네임스페이스를 확인할 수 있음
# dir() : 네임스페이스의 key값을 확인할 수 있음
# __doc__ : class의 주석을 확인
# __class__ : 어떤 클래스로 만들어진 인스턴스인지 확인
"""


class Robot:

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


jarvis = Robot("jarvis", 2324212127)
bixby = Robot("bixby", 12418083)
bixby2 = Robot("bixby2", 12418083)

print(Robot.__dict__)
