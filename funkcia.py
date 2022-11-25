class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, work):
        return f'I will help you with your {self.work}.' \
               f'Afterwards I will help you with {work}.'

helper = Helper('tests')
print(helper('Math'))
print(helper('Сhemistry'))

def helper(work):
    work_in_memory = work

    def helper(work):
        return f'I will help you with your {work_in_memory}.' \
               f'Afterwards I will help you with {work}.'
    return helper

helper = helper('homework')
print(helper('Biologie'))
print(helper('English'))