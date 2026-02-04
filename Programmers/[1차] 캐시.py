from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for city in cities:
        city = city.lower()
        if (city not in cache):
            answer += 5
            
            if cacheSize>0:
                if cacheSize==len(cache):
                    cache.popleft()
                cache.append(city)
        else:
            answer += 1
            cache.remove(city)
            cache.append(city)
    return answer