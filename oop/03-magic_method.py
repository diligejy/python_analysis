"""
# namespace : 개체를 구분할 수 있는 범위
# __dict__ : 네임스페이스를 확인할 수 있음
# dir() : 네임스페이스의 key값을 확인할 수 있음
# __doc__ : class의 주석을 확인
# __class__ : 어떤 클래스로 만들어진 인스턴스인지 확인
"""


class Robot:

    """
    [Robot Class]
    Author : 송진영
    Role : blahblah
    """

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

    @staticmethod
    def this_is_robot_class():
        print("yes!!")

    def __str__(self):
        return f"{self.name} robot!!"
    
    def __call__(self):
        print("call!")
        return f"{self.name} call!"


siri = Robot("siri", 301341351)
jarvis = Robot("jarvis", 2324212127)
bixby = Robot("bixby", 12418083)
bixby2 = Robot("bixby2", 12418083)

print(Robot.__dict__)
print(siri.__dict__)
print(jarvis.__dict__)

print(siri.population)
siri.how_many()

print(dir(siri))
print(dir(Robot))
print(Robot.__doc__)
print(siri.__class__)

print(Robot.this_is_robot_class())
print(jarvis.this_is_robot_class())


print(siri.__str__)
print(siri)
print(siri.__str__())
print(siri())