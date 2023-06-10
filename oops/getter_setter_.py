class Cat:
    def __init__(self, name, legs=4, tail=True, eyes=2):
        self.name = name
        self.legs = legs
        self._tail = tail
        self.__eyes = eyes

    @property
    def tail(self):
        print(f"Showing the details about cat named {self.name}'s tail = {self._tail}")
        return self._tail

    @tail.setter
    def tail(self, new_tail_val):
        self._tail = new_tail_val
        print(
            f"Changing the details about cat named {self.name}'s tail. New value is {self._tail}"
        )

    def get_eyes_count(self):
        print("getting eyes count")
        return self.__eyes

    def set_eyes_count(self, new_val):
        print("Setting eyes count")
        self.__eyes = new_val
        print("Setting done")
        return new_val

    eyes = property(get_eyes_count, set_eyes_count)

    def display_eyes(self):
        print(f"eyes are {self.__eyes}")


if __name__ == "__main__":
    cat1 = Cat("mumu")
    pass
