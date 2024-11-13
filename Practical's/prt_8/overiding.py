class A :
    def hello(self):
        return "Good Morning!"
class B(A):
    def hello(self):
        return super().hello() + "Good Night!"

a =B()
print(a.hello())
