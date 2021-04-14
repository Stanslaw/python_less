class double_text():
    def __init__(self, a, b, name):
        self.a = a
        self.b = b
        self.name = name

    def __str__(self):
        return f"res {self.name}" + str((self.a, self.b))
    
    def summ(self):
        return self.a + self.b

    def null_first(self):
        self.a = 0


cer = double_text(10, 20, "cer")
cer_2 = double_text(30, 40, "cer_2")

print(cer.a)
print(cer.b)
print(cer)
print(cer.summ())
cer.null_first()
print(cer)
print(cer_2)
print(cer.a)
cer_2.a = cer_2.a - cer.b
print(cer_2)
