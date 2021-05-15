from zope.interface import Interface, Attribute, implementer
from builders import CakeBuilder, CookieBuilder, CandyBuilder, ChocolateBuilder, CupcakeBuilder
from directors import CakeDirector, CookieDirector, CandyDirector, ChocolateDirector, CupcakeDirector


_instance = None
def GetInstanse():
    if _instance is None:
        return ConfectionFactory()


class ConfectionFactory(Interface):
    def GetInstance(self):
        """ """
    def BuildCake(self):
        """ """
    def BuildCookie(self):
        """ """
    def BuildCandy(self):
        """ """
    def BuildChocolate(self):
        """ """
    def BuildCupcake(self):
        """ """

@implementer(ConfectionFactory)
class ConfectionFactory(object):
    def BuildCake(self):
        builder = CakeBuilder()
        director = CakeDirector(builder)
        director.Build()
        return builder.GetConfection()

    def BuildCookie(self):
        builder = CookieBuilder()
        director = CookieDirector(builder)
        director.Build()
        return builder.GetConfection()

    def BuildCandy(self):
        builder = CandyBuilder()
        director = CandyDirector(builder)
        director.Build()
        return builder.GetConfection()

    def BuildChocolate(self):
        builder = ChocolateBuilder()
        director = ChocolateDirector(builder)
        director.Build()
        return builder.GetConfection()

    def BuildCupcake(self):
        builder = CupcakeBuilder()
        director = CupcakeDirector(builder)
        director.Build()
        return builder.GetConfection()



def ExecuteTask(factory):
    cake = factory.BuildCake()
    cake.PrintText("I'm tasty cake")
    print("Cake ingredients: " + ','.join(cake.GetAllIngredients()))

    cookie = factory.BuildCookie()
    cookie.PrintText("I'm yummy cookie")
    print("Cookie ingredients: " + ','.join(cookie.GetAllIngredients()))

    candy = factory.BuildCandy()
    candy.PrintText("I'm sweet candy")
    print("Candy ingredients: " + ','.join(candy.GetAllIngredients()))

    chocolate = factory.BuildChocolate()
    chocolate.PrintText("I'm delicious chocolate")
    print("Chocolate ingredients: " + ','.join(chocolate.GetAllIngredients()))

    cupcake = factory.BuildCupcake()
    cupcake.PrintText("I'm appetizing cupcake")
    print("Cupcake ingredients: " + ','.join(cupcake.GetAllIngredients()))


if __name__ == "__main__":
    print("Пашковская Екатерина Анатольевна")
    print("Группа: 8-Т3О-402Б-16")
    print("Лабораторная работа 1\n")

    ExecuteTask(GetInstanse())