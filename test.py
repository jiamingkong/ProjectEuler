class myc:
    a = ['a', 'b']

    def f1(self):
        b = myc.a[:]
        b.extend(['c', 'd'])
        return b

    def f2(self):
        b = myc.a[:]
        b.extend(['f','g'])
        return b

cvar = myc()

print(cvar.f1())
print(cvar.f2())
print(cvar.f1())