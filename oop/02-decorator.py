def copyright(func):
    def new_func():
        print("저작권 관련 내용 어쩌고저쩌고")
        func()

    return new_func


@copyright
def smile():
    print("e")


@copyright
def angry():
    print("오우 노")


@copyright
def love():
    print("하트")


smile()
angry()
love()
