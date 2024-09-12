class RandomizedSet:

    def __init__(self):
        self.ran = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.ran:
            self.ran.add(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.ran:
            self.ran.remove(val)
            return True
        else:
            return False

        

    def getRandom(self) -> int:
        return random.choice(list(self.ran))
