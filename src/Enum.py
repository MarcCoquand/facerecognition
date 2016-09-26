class Enum(set):
    """ Enum is a python 2.7 implementation of a Enum
        provided by http://stackoverflow.com/a/2182437/4689625
    """
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError
