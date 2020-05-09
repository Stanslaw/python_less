class Capital():
    _instance = None

    # @staticmethod
    def inst(name):
        if not Capital._instance:
            Capital._instance = name
        # print(Capital._instance)
        return Capital._instance

    #single call check
    def __init__(self, name):
        Capital.inst(name)
        print("Constructor called!")

    def name(self):
        return Capital._instance


a = Capital("Aht")
b = Capital("Lvov")

print(a.name())
print(b.name())

