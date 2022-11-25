def raise_to_the_degrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number ** i
        i += 1

result = raise_to_the_degrees(2.5, 10)
print(result)

for _ in result:
   print(_)
print('********')
for _ in result:
    print(_)


def raise_to_the_degrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number ** i
        i += 1

result = raise_to_the_degrees(8.5, 15)
print(result)

for _ in result:
   print(_)
print('********')
for _ in result:
    print(_)
