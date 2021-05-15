from zope.interface import Interface, Attribute, implementer

class IBox(Interface):
    """Any text add"""
    def AddText(text):
        """Add text"""

@implementer(IBox)
class Box(object):
    def AddText(text):
        print(text)

class Confection(Interface):
    _box = Attribute("""Box""")
    _ingredients = Attribute("""Ingredients""")
    def PrintText(self, text):
        """ """
    def AddIngredient(self, name):
        """ """
    def GetAllIngredients(self):
        """ """

@implementer(Confection)
class Cake(object):
    def __init__ (self, box):
        self._box = box
        self._ingredients = []

    def PrintText(self, text):
        self._box.AddText(text)

    def AddIngredient(self, name):
        self._ingredients.append(name)

    def GetAllIngredients(self):
        return self._ingredients

@implementer(Confection)
class Cookie(object):
    def __init__ (self, box):
        self._box = box
        self._ingredients = []

    def PrintText(self, text):
        self._box.AddText(text)

    def AddIngredient(self, name):
        self._ingredients.append(name)

    def GetAllIngredients(self):
        return self._ingredients

@implementer(Confection)
class Candy(object):
    def __init__ (self, box):
        self._box = box
        self._ingredients = []

    def PrintText(self, text):
        self._box.AddText(text)

    def AddIngredient(self, name):
        self._ingredients.append(name)

    def GetAllIngredients(self):
        return self._ingredients

@implementer(Confection)
class Chocolate(object):
    def __init__ (self, box):
        self._box = box
        self._ingredients = []

    def PrintText(self, text):
        self._box.AddText(text)

    def AddIngredient(self, name):
        self._ingredients.append(name)

    def GetAllIngredients(self):
        return self._ingredients

@implementer(Confection)
class Cupcake(object):
    def __init__ (self, box):
        self._box = box
        self._ingredients = []

    def PrintText(self, text):
        self._box.AddText(text)

    def AddIngredient(self, name):
        self._ingredients.append(name)

    def GetAllIngredients(self):
        return self._ingredients

