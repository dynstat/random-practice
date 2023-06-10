class Numbers_:
    x = 5

    def __init__(self):
        self.y = 6


a1 = Numbers_()
pass


f = open("filename.txt", "wb")
f.write(b"hello")
f.close()


with open("filename.txt", "wb") as f:
    f.write(b"helliooooo")
