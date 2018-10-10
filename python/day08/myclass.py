class A:
    def foo(self):
        print('in A-foo')
    def sing(self):
        print('lalala...')

class B:
    def bar(self):
        print('in B-foo')
    def sing(self):
        print('wow~~~')

class C(B,A):
    pass


if __name__ == '__main__':
    c = C()
    c.foo()
    c.bar()
    c.sing()