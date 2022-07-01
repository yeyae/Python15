#리스트 요소 삽입(insert)
from re import A


a = [1, 2, 3]
a.insert(0, 4)
a.insert(3, 5)
#리스트 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a
#리스트 요소 끄집어내기(pop)
a = [1, 2, 3]
a.pop()
a
a = [1, 2, 3]
a.pop()
a
#리스트에 포함된 요소 x의 개수 세기(count)
a = [1, 2, 3, 1]
a.count(1)
#리스트 확장(extend)
a = [1, 2, 3]
a.extend([4, 5])
a
b = [6, 7]
a.extend(b)
a