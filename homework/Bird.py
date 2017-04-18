class Bird ():
    """ Бвзовый класс б определяющий свойство птиц"""
    count = 0
    def __init__(self, chat):
        self.sound = chat
        Bird.count += 1
        print("Bird number : ", Bird.count)
    def talk(self):
        return"Bird cry out :", self.sound

bird_1 = Bird ("ka ka ka")
print (bird_1.talk())

