from collections import defaultdict
import random

class RandomizedSet:
    dic = defaultdict(bool)

    def __init__(self):
        self.dic = defaultdict(bool)

    def insert(self, val: int) -> bool:
        if not self.dic[val]:
            self.dic[val] = True
            return True
        return False

    def remove(self, val: int) -> bool:
        if self.dic[val]:
            self.dic[val] = False
            return True
        return False

    def getRandom(self) -> int:
        return list(random.choice(list(filter(lambda x: x[1] == True, self.dic.items()))))[0]
