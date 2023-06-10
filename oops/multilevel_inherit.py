class A:
    def __init__(self, name, age, extra=100):
        print("This is A")
        self.name = name
        self.age = age
        self.category = "A"
        self.extra = extra


class B(A):
    def __init__(self):
        print("This is B")

    pass


class C(B):
    # def __init__(self):
    #     print("This is C")
    pass


class D(C):
    pass


class D_mod(C):
    # def __init__(self):
    #     print("This is D_mod")
    pass


class Child(D_mod):
    def __init__(self, name, age, category):
        print("This is Child")
        A.__init__(self=self, name=name, age=age)
        self.category = category
        B.__init__(self)

    def display(self):
        print(f"category -> {self.category}")


if __name__ == "__main__":
    c1 = Child("xskk", 26, "B")
    c1.display()
    print(f"{c1.extra}")
    print(f"{c1.category}")
    pass
