# Iterator Example


class range_odd:
    def __init__(self, last):
        self.last = last
        self.initial = 1

    def __iter__(self):
        return self

    # 1,3,5,7,9....
    def __next__(self):
        if self.initial >= self.last:
            raise StopIteration
        if self.initial % 2 != 0:
            self.initial += 1
            return self.initial - 1
        else:
            self.initial += 2
            return self.initial - 1


if __name__ == "__main__":
    r_obj = range_odd(10)  # iterator
    ll = [2, 3, 4, 5]  # iterable
    # iterable does not have a __next__ magic method, so we can not directly apply next on the iterable object.
    # We first have to call __iter__() method that returns an iterator. An iterator can apply any logic, In the case of iterables like list, tuples, etc., the iterator just returns the next items when __next__() method is called.

    # This is what happens in for loop behind the scenes.

    itt = iter(ll)  # returns the iterator object of the list
    itt.__next__()  # return the next item starting from the first one.
    print("debug")
