class Puppy:
    n_puppies = 0  # number of created puppies

    # define __new__
    def __new__(cls, *args, **kwargs):
        if cls.n_puppies == 0:
            cls.n_puppies += 10
            return object.__new__(cls, *args, **kwargs)
        return None
