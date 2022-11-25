'''
my_lst = [1, 'family', 125, 'itstep']

iterator = iter(my_lst)
print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


for elem in iterator:
    print(f'{elem} - ', elem)

class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i
count = Counter(9)

count_1 = Counter(3)
for elem in count:
    print(elem)

print(count.__iter__())
print(count.__next__())
print(count.__next__())
print(count.__next__())
print(count.__next__())
print(count.__next__())
print(count.__next__())
print(count.__next__())
print(count.__next__())
print(count.__next__())

for elem in count:
    print(elem)

# генератори
def raise_to_the_degrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number ** i
        i += 1

result = raise_to_the_degrees(2.5, 10)
print(result)

#for _ in result:
#   print(_)
#print('********')
#for _ in result:
#    print(_)

def raise_to_the_degrees(number):
    i = 0
    while True:
        yield number ** i
        i += 1

result = raise_to_the_degrees(100)
print(result)
for _ in result:
    print(_)


def raise_to_the_degrees(number):
    i = 0
    while True:
        res = number ** i
        yield res
        if res > 100 ** 30:
            return
        i += 1

result = raise_to_the_degrees(100)
'''


# zamykanya funkcii
'''
class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, work):
        return f'I will help you with your {self.work}.' \
               f'Afterwards I will help you with {work}.'

helper = Helper('homework')
print(helper('cleaning'))


def helper(work):
    work_in_memory = work

    def helper(work):
        return f'I will help you with your {work_in_memory}.' \
               f'Afterwards I will help you with {work}.'
    return helper

helper = helper('homework')
print(helper('cleaning'))
print(helper('driving'))
'''

'''
# dekorator
def cheker(function):
    def cheker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f'We have problems {exc}.')
        else:
            print(f'No problems. Result - {result}')
    return cheker

def calculate(expression):
    return eval(expression)

calculate = cheker(calculate)
calculate('3.5+v')
'''

def cheker(*exc_type):
    def cheker(function):
        def cheker(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except (exc_type) as exc:
                print(f'We have problems {exc}')
            else:
                print(f'No problem. Result - {result}')
        return cheker
    return cheker

@cheker(NameError, TypeError, SyntaxError)
def calculate(expression):
    return eval(expression)

while True:
        print(eval(input(">>>")))
calculate()

