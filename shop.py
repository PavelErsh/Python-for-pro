from datetime import datetime
class Greeter:
    def __init__(self, name, store):
        self.name = name
        self.store = store
    def _day(self):#tace date
        return datetime.now().strftime('%A')

    def _part_of_day(self):
        current_hour = datetime.now().hour
        if current_hour < 12:
            part_of_day = 'утра'
        elif 12 <= current_hour < 17:
            part_of_day = 'дня'
        else:
            part_of_day = 'вечера'
        return part_of_day

    def greet(self):
        print(f'Здравствуйте, меня зовут {self.name}, и добро пожаловать в {self.store}!')
        print(f'Желаем вам приятного {self._part_of_day()} {self._day()}?')
        print('Дарим вам купон на скидку 20 %!')


welcome = Greeter("bishop", "test")
welcome.greet()