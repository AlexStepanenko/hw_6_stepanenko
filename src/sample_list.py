import random

n = 10
random_list = []


# append
print('append')
for i in range(n):
    random_list.append(random.random())

print(random_list)


# extend
print('extend')
random_list.extend([888, 999])
print(random_list)


# insert
print('insert')
random_list.insert(0, 555)
print(random_list)


# remove
print('remove')
random_list.remove(555)
print(random_list)


# pop
print('pop')
print(random_list.pop())


# index
print('index')
print(random_list.index(888))


# count
print('count')
print(random_list.count(10.0))


# sort
print('sort')
random_list.sort()
print(random_list)


# reverse
print('reverse')
random_list.reverse()
print(random_list)


# copy
print('copy')
cp = random_list.copy()
print(f'#{id(cp)}: #{cp}')
print(f'#{id(random_list)}: #{random_list}')


# clear
print('clear')
random_list.clear()
print(random_list)
