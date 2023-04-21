import enum


def product_200_totes_formula(sales):
    return sales/3300


def product_275_totes_formula(sales):
    return sales/3500


def product_300_totes_formula(sales):
    return sales/2000


def product_315_totes_formula(sales):
    return sales/3300


def product_325_totes_formula(sales):
    return sales/3500


def product_340_totes_formula(sales):
    return sales/2000


def product_360_totes_formula(sales):
    return sales/2000


def product_400_totes_formula(sales):
    return sales/3300


def product_410_totes_formula(sales):
    return sales/3500


def product_425_totes_formula(sales):
    return sales/2000


def product_475_totes_formula(sales):
    return sales/2000


def product_500_totes_formula(sales):
    return sales/3500


def product_525_totes_formula(sales):
    return sales/2000


def product_575_totes_formula(sales):
    return sales/2000


def product_615_totes_formula(sales):
    return sales/2000


def product_650_totes_formula(sales):
    return sales/2000


class Product_Formula(enum.Enum):
    Prod_200 = {"name": 200, "totes_formula": product_200_totes_formula}
    Prod_275 = {"name": 275, "totes_formula": product_275_totes_formula}
    Prod_300 = {"name": 300, "totes_formula": product_300_totes_formula}
    Prod_315 = {"name": 315, "totes_formula": product_315_totes_formula}
    Prod_325 = {"name": 325, "totes_formula": product_325_totes_formula}
    Prod_340 = {"name": 340, "totes_formula": product_340_totes_formula}
    Prod_360 = {"name": 360, "totes_formula": product_360_totes_formula}
    Prod_400 = {"name": 400, "totes_formula": product_400_totes_formula}
    Prod_410 = {"name": 410, "totes_formula": product_410_totes_formula}
    Prod_425 = {"name": 425, "totes_formula": product_425_totes_formula}
    Prod_475 = {"name": 475, "totes_formula": product_475_totes_formula}
    Prod_500 = {"name": 500, "totes_formula": product_500_totes_formula}
    Prod_525 = {"name": 525, "totes_formula": product_525_totes_formula}
    Prod_575 = {"name": 575, "totes_formula": product_575_totes_formula}
    Prod_615 = {"name": 615, "totes_formula": product_615_totes_formula}
    Prod_650 = {"name": 650, "totes_formula": product_650_totes_formula}



# print(Product_Formula.Prod_200.value["totes_formula"](1))
# print(Product_Formula.Prod_275.value["totes_formula"](1))
# print(Product_Formula.Prod_300.value["totes_formula"](1))







