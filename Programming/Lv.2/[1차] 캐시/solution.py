# https://school.programmers.co.kr/learn/courses/30/lessons/17680#
class Cache:
    def __init__(self, size):
        self.size = size
        self.space = []
        
    def is_hit(self, city):
        hit = False
        city = city.lower()
        for i, cached in enumerate(self.space):
            if cached['city'] == city:
                hit = True
                self.space[i]['lifetime'] = 0
            else:
                self.space[i]['lifetime'] += 1
        return 1 if hit else 5

    def push(self, city):
        city = city.lower()
        if len(self.space) < self.size:
            self.space.append({
                'city': city,
                'lifetime': 0
            })
        else:
            pick = 0
            pick_index = 0
            for i, cached in enumerate(self.space):
                if cached['lifetime'] > pick:
                    pick_index = i
                    pick = cached['lifetime']
            self.space[pick_index] = {
                'city': city,
                'lifetime': 0
            }
                

def solution(size, cities):
    answer = 0
    cache = Cache(size)
    if size == 0:
        return len(cities) * 5
    for city in cities:
        res = cache.is_hit(city)
        answer += res
        if res == 5:
            cache.push(city)
    return answer