for i in [1,2,3]:
    if i:
        print('pass %d' % i)
        pass
    print("!111")

for i in [4,5,6]:
    if i:
        print('pass %d' % i)
        continue
    print("222222")