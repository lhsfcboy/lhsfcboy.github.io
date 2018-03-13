import itertools


class Order():
    count_id = next(itertools.count())


count_id = next(itertools.count(1))

for i in range(990, 999):
    print(count_id)

import itertools


class A(object):
    id_generator = itertools.cycle(range(100,1000)) # first generated is 100
    def __init__(self):
      self.id = next(A.id_generator)
objs = [A(), A(), A(), A(), A(), A(), A()]
for obj in objs:
    print(obj.id)



class B(object):
    id_generator = itertools.count(100) # first generated is 100
    def __init__(self):
      self.id = next(B.id_generator)
objs = [B(), B()]
print(objs[0].id, objs[1].id)

print(f"{1000:03}")