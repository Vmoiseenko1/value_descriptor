class Value:
    def __init__(self):
        self.value = None

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, instance, value):
        if value < 0 or instance.comission < 0:
            raise ValueError('Cannot be negative')
        self.value = value * (1 - instance.comission)

class Account:
    amount = Value()
    def __init__(self, comission):
        self.comission = comission

new_account = Account(0.1)
new_account.amount = 100
print(new_account.amount)