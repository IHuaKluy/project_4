# Write your answer to Task 1 here
import pandas as pd
data = pd.read_csv("production_data.csv",parse_dates=["production_date"])
# print(data.info())

data["raw_material_supplier"] = data["raw_material_supplier"].map({1 : "national_supplier",2 : "international_supplier"})
data["raw_material_supplier"] = data["raw_material_supplier"].fillna("national_supplier")
data["raw_material_supplier"] = data["raw_material_supplier"].astype("category")

data["mixing_speed"] = data["mixing_speed"].replace("-","Not Specified")
data["mixing_speed"] = data["mixing_speed"].fillna("Not Specified")
data["mixing_speed"] = data["mixing_speed"].astype("category")

data["pigment_type"] = data["pigment_type"].replace("Type_C","type_c")
data["mixing_speed"] = data["mixing_speed"].fillna("other")

data["pigment_quantity"] = data["pigment_quantity"].fillna(data["pigment_quantity"].median()).round(2)

data["mixing_time"] = data["mixing_time"].fillna(data["mixing_time"].mean()).round(2)

data["product_quality_score"] = data["product_quality_score"].fillna(data["product_quality_score"].mean()).round(2)

"""
Just for Testing
# print(data["raw_material_supplier"].value_counts()) 
# print(data["mixing_speed"].value_counts())
# print(data["pigment_type"].value_counts())
# print(data["production_date"].value_counts())

# print(data["mixing_time"].sort_values())
# print(data["product_quality_score"].sort_values())
# print(data["pigment_quantity"].sort_values())

"""
# print(data.info())

clean_data = data
print(clean_data)
