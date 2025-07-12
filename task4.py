# Write your answer to Task 4 here
product_quality = pd.read_csv("production_data.csv")
product_quality = clean_data[["pigment_quantity","product_quality_score"]]
product_quality["pigment_quantity_mean"] = round(product_quality["pigment_quantity"].mean(),2)
product_quality["pigment_quantity_sd"] = round(product_quality["pigment_quantity"].std(),2)
product_quality["product_quality_score_mean"] = round(product_quality["product_quality_score"].mean(),2)
product_quality["product_quality_score_sd"] = round(product_quality["product_quality_score"].std(),2)
product_quality["corr_coef"] = round(product_quality["pigment_quantity"].corr(product_quality["product_quality_score"]),2)
product_quality = product_quality.iloc[:,2:7]
print(product_quality)
