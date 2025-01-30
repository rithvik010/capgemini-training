class example:
    def _init_(self,name):
        print(f"first constructor:hello{name}")
    def _init_(self,age):
        print(f"second constructor:age is {age}")
obj=example(25)
class example:
    def _init_(self,*args):
        if len(args)==1:
            print(f"hello {args[0]}")
        elif len(args)==2:
            print(f"hello{args[0]},you are {args[1]}years old")

obj=example('alice')
obj=example( ' bob',30)