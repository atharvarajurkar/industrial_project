import pandas as pd
import numpy as np
from src.formulae import Product_Formula


def join_racks(racks_list):
    joined_rack = racks_list[0]

    for i in range(1, len(racks_list)):
        joined_rack = np.concatenate((joined_rack, racks_list[i]), axis=1)

    return joined_rack



def get_rack_limit_for_runners(products):
    sum_of_totes = products["totes"].sum()

    products["limit"] = 0

    for i in range(products.shape[0]):
        percent = (products.iloc[i]["totes"] * 100) / sum_of_totes
        # products.iloc[i]["limit"] = round(percent * 16 / 100)
        index = products.iloc[i].name
        products["limit"][index] = round(percent * 16 / 100)

    remaining_racks = 16 - products["limit"].sum()
    index = products.iloc[products.shape[0] - 1].name
    products["limit"][index] += remaining_racks

    return products


def fill_rack(product_name, rack, product_totes):
    count = product_totes
    for i in range(rack.shape[0]):
        for j in range(rack.shape[1]):
            rack[i][j] = product_name
            count -= 1
            if count == 0:
                break
        if count == 0:
            break

    return rack


def fill_runners_rack(runners_rack_limits):
    rack_list = []
    for i in range(runners_rack_limits.shape[0]):
        product_name = runners_rack_limits.iloc[i]["product"]
        product_totes = runners_rack_limits.iloc[i]["totes"]
        product_limit = runners_rack_limits.iloc[i]["limit"]

        rack = np.empty((5, int(product_limit)), dtype=object)
        rack[rack == None] = ""
        rack = fill_rack("Prod_" + str(int(product_name)), rack, product_totes)
        rack_list.append(rack)

    return rack_list


excel = pd.read_excel("../test.xlsx")

for product_index in range(excel.shape[0]):
    product_name = excel["product"][product_index]
    product_sales = excel["sales"][product_index]

    product_enum = Product_Formula["Prod_" + str(product_name)]
    totes = product_enum.value["totes_formula"](product_sales)
    excel["totes"][product_index] = round(totes)

excel = excel.sort_values(by="totes", ascending=False)

runners = excel[0:3]
repeaters = excel[3:11]
strangers = excel[11:16]

runners_rack_limits = get_rack_limit_for_runners(runners)
runners_rack_list = fill_runners_rack(runners_rack_limits)

joined_runners_rack = join_racks(runners_rack_list)
runners_rack_list_df = pd.DataFrame(joined_runners_rack)

excel.to_excel("../test.xlsx", index=False)
runners_rack_list_df.to_excel("../output.xlsx", index=False)
print(1)
