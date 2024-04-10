from collections import deque
# 파이선 자료 구조
###################################################
#2. 집합(Set) : 중복이 제거됨
 #2-1 형태 및 선언
basket = set()
print(basket)
basket = {}
print(basket)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket2 = {'apple', 'rabbit', 'orange', 'banana'}
print(basket)
print('orange' in basket)

print(basket.add('painapple'))
print(basket.add('painapple'))
print(basket)
print(basket.difference(basket2))
print(basket.pop())
print(basket)
print(basket2)
basket2.remove('rabbit')
print(basket2)
print(basket2.union(basket))
print(basket2)
basket2.update(basket)
print(basket2)
