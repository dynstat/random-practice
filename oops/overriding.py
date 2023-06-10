class Vehicle:
    def __init__(self, v_type, speed) -> None:
        self.type = v_type
        self.speed = speed

    def describe(self):
        print(f"Type is {self.type}\nSpeed is...{self.speed}\n")

    # def __repr__(self) -> str:
    #     return f"Type is {self.type}\nSpeed is {self.speed}\n"

    def __add__(self, other_obj):
        return self.speed + other_obj.speed


if __name__ == "__main__":
    V_1 = Vehicle("Car", 100)
    V_2 = Vehicle("Fast Car", 150)

    V_1.describe()
    V_2.describe()

    print(V_1 + V_2)
