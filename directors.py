from zope.interface import Interface, Attribute, implementer

class CakeDirector():
    _builder = None

    def __init__(self, builder):
        self._builder = builder

    def Build(self):
        self._builder.AddCandiedFruit()
        self._builder.AddBerry()
        self._builder.AddNut()


class CookieDirector():
    _builder = None

    def __init__(self, builder):
        self._builder = builder

    def Build(self):
        self._builder.AddCandiedFruit()
        self._builder.AddBerry()
        self._builder.AddNut()


class CandyDirector():
    _builder = None

    def __init__(self, builder):
        self._builder = builder

    def Build(self):
        self._builder.AddCandiedFruit()
        self._builder.AddBerry()
        self._builder.AddNut()


class ChocolateDirector():
    _builder = None

    def __init__(self, builder):
        self._builder = builder

    def Build(self):
        self._builder.AddCandiedFruit()
        self._builder.AddBerry()
        self._builder.AddNut()


class CupcakeDirector():
    _builder = None

    def __init__(self, builder):
        self._builder = builder

    def Build(self):
        self._builder.AddCandiedFruit()
        self._builder.AddBerry()
        self._builder.AddNut()

