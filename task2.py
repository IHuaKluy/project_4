# Write your answer to Task 2 here
aggregated_data = clean_data.groupby("raw_material_supplier").agg(
    avg_product_quality_score = ("product_quality_score","mean"),
    avg_pigment_quantity = ("pigment_quantity","mean")
)
aggregated_data["avg_product_quality_score"] = round(aggregated_data["avg_product_quality_score"],2)
aggregated_data["avg_pigment_quantity"] = round(aggregated_data["avg_pigment_quantity"],2)
aggregated_data = aggregated_data.reset_index()

print(aggregated_data)
