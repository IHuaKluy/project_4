# Write your answer to Task 3 here
clean_data2 = pd.read_csv("production_data.csv",parse_dates=["production_date"])

pigment_data = clean_data2[(clean_data2["pigment_quantity"] > 35) & (clean_data2["raw_material_supplier"] == 2)]
pigment_data = pigment_data.groupby("raw_material_supplier").agg(
    pigment_quantity = ("pigment_quantity","mean"),
    avg_product_quality_score = ("product_quality_score","mean")
)
pigment_data["pigment_quantity"] = round(pigment_data["pigment_quantity"],2)
pigment_data["avg_product_quality_score"] = round(pigment_data["avg_product_quality_score"],2)
pigment_data = pigment_data.reset_index()

print(pigment_data)
