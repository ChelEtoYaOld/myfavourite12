class Papa():
    def about(self):
        print("i am Papa.")
    def about_myself(self):
        print('I am GrandParent.')

class Mama(Papa):
    def about_myself(self):
        print('I am Mama')

class Kid(Mama):
    def __init__(self):
        super().about()
        super().about_myself()
        print('I am Misha')

nick = Kid()