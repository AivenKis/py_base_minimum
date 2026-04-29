# Какую одну строчку требуется закомментировать, чтобы класс ClsB выводил переменную класса ClsZ?

class ClsZ:
    env = 'Class Z: Env'


class ClsA(ClsZ):
    def init(self):
        self.env = 'Class A.init: Env'
    # env = "Class A: Env"

    def cls_env(self):
        self.env = 'Class A.casd: Env'
        print(self.env)


class ClsB(ClsA):

    def init(self):
        super().init()
        print(self.env)


a_cls = ClsA()
a_cls.cls_env()

print("ClsA: " + a_cls.env)
print("ClsB: " + ClsB.env)


