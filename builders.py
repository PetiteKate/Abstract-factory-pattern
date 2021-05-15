from zope.interface import Interface, Attribute, implementer
from confections import Box, Cake, Cookie, Candy, Chocolate, Cupcake

class ICakeBuilder(Interface):
    _result = Attribute("""Result""")
    def AddBerry(self):
        """ """
    def AddNut(self):
        """ """
    def AddCandiedFruit(self):
        """ """

class ICookieBuilder(Interface):
    _result = Attribute("""Result""")
    def AddBerry(self):
        """ """
    def AddNut(self):
        """ """
    def AddCandiedFruit(self):
        """ """

class ICandyBuilder(Interface):
    _result = Attribute("""Result""")
    def AddBerry(self):
        """ """
    def AddNut(self):
        """ """
    def AddCandiedFruit(self):
        """ """

class IChocolateBuilder(Interface):
    _result = Attribute("""Result""")
    def AddBerry(self):
        """ """
    def AddNut(self):
        """ """
    def AddCandiedFruit(self):
        """ """


class ICupcakeBuilder(Interface):
    _result = Attribute("""Result""")
    def AddBerry(self):
        """ """
    def AddNut(self):
        """ """
    def AddCandiedFruit(self):
        """ """
@implementer(ICakeBuilder)
class CakeBuilder(object):
    def __init__(self):
        box = Box
        confection = Cake(box)
        self._result = confection

    def AddBerry(self):
        self._result.AddIngredient("Berry")

    def AddNut(self):
        self._result.AddIngredient("Nut")

    def AddCandiedFruit(self):
        self._result.AddIngredient("Candied fruit")

    def GetConfection(self):
        result = self._result
        box = Box
        confection = Cake(box)
        self._result = confection
        return result

@implementer(ICookieBuilder)
class CookieBuilder(object):
    def __init__(self):
        box = Box
        confection = Cookie(box)
        self._result = confection

    def AddBerry(self):
        self._result.AddIngredient("Berry")

    def AddNut(self):
        self._result.AddIngredient("Nut")

    def AddCandiedFruit(self):
        self._result.AddIngredient("Candied fruit")

    def GetConfection(self):
        result = self._result
        box = Box
        confection = Cookie(box)
        self._result = confection
        return result

@implementer(ICandyBuilder)
class CandyBuilder (object):
    def __init__(self):
        box = Box
        confection = Candy(box)
        self._result = confection

    def AddBerry(self):
        self._result.AddIngredient("Berry")

    def AddNut(self):
        self._result.AddIngredient("Nut")

    def AddCandiedFruit(self):
        self._result.AddIngredient("Candied fruit")

    def GetConfection(self):
        result = self._result
        box = Box
        confection = Candy(box)
        self._result = confection
        return result

@implementer(IChocolateBuilder)
class ChocolateBuilder(object):
    def __init__(self):
        box = Box
        confection = Chocolate(box)
        self._result = confection

    def AddBerry(self):
        self._result.AddIngredient("Berry")

    def AddNut(self):
        self._result.AddIngredient("Nut")

    def AddCandiedFruit(self):
        self._result.AddIngredient("Candied fruit")

    def GetConfection(self):
        result = self._result
        box = Box
        confection = Chocolate(box)
        self._result = confection
        return result

@implementer(ICupcakeBuilder)
class CupcakeBuilder(object):
    def __init__(self):
        box = Box
        confection = Cupcake(box)
        self._result = confection

    def AddBerry(self):
        self._result.AddIngredient("Berry")

    def AddNut(self):
        self._result.AddIngredient("Nut")

    def AddCandiedFruit(self):
        self._result.AddIngredient("Candied fruit")

    def GetConfection(self):
        result = self._result
        box = Box
        confection = Cupcake(box)
        self._result = confection
        return result

