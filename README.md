This assignment belong to DataCamp. This is just for educational purpose only.

Project Title : Spectrum Shades LLC
Spectrum Shades LLC is a prominent supplier of concrete color solutions, offering a wide range of pigments and coloring systems used in various concrete applications, including decorative concrete, precast concrete, and concrete pavers. The company prides itself on delivering high-quality colorants that meet the unique needs of its diverse clientele, including contractors, architects, and construction companies.
</br></br>
The company has recently observed a growing number of customer complaints regarding inconsistent color quality in their products. The discrepancies have led to a decline in customer satisfaction and a potential increase in product returns.
By identifying and mitigating the factors causing color variations, the company can enhance product reliability, reduce customer complaints, and minimize return rates.
</br></br>
You are part of the data analysis team tasked with providing actionable insights to help Spectrum Shades LLC address the issues of inconsistent color quality and improve customer satisfaction.

# Task 1

Before you can start any analysis, you need to confirm that the data is accurate and reflects what you expect to see. 

It is known that there are some issues with the `production_data` table, and the data team have provided the following data description. 

Write a query to ensure the data matches the description provided, including identifying and cleaning all invalid values. You must match all column names and description criteria.
</br>

- You should start with the data in the file "production_data.csv".
- Your output should be a DataFrame named clean_data.
- All column names and values should match the table below.
</br>

| Column Name             | Criteria                                                                                         |
|--------------------------|--------------------------------------------------------------------------------------------------|
| batch_id | Discrete. Identifier for each batch. Missing values are not possible. |
| production_date | Date. Date when the batch was produced.|
| raw_material_supplier | Categorical. Supplier of the raw materials. (1='national_supplier', 2='international_supplier'). <br> Missing values should be replaced with 'national_supplier'.|
| pigment_type           | Nominal. Type of pigment used. ['type_a', 'type_b', 'type_c']. <br> Missing values should be replaced with 'other'. |
| pigment_quantity       | Continuous. Amount of pigment added (in kilograms) (Range: 1 - 100). <br> Missing values should be replaced with median. |
| mixing_time           | Continuous. Duration of the mixing process (in minutes). <br> Missing values should be replaced with mean, rounded to 2 decimal places. |
| mixing_speed          | Categorical. Speed of the mixing process represented as categories: 'Low', 'Medium', 'High'.</br> Missing values should be replaced with 'Not Specified'. |
| product_quality_score | Continuous. Overall quality score of the final product (rating on a scale of 1 to 10). <br> Missing values should be replaced with mean, rounded to 2 decimal places. |

# Task 2

You want to understand how the supplier type and quantity of materials affect the final product attributes.

Calculate the average `product_quality_score` and `pigment_quantity` grouped by `raw_material_supplier`.

- You should start with the data in the file 'production_data.csv'. 
- Your output should be a DataFrame named aggregated_data.
- It should include the three columns: `raw_material_supplier`, `avg_product_quality_score`, and `avg_pigment_quantity`.
- Your answers should be rounded to 2 decimal places.

# Task 3

To get more insight into the factors behind product quality, you want to filter the data to see an average product quality score for a specified set of results.

Identify the average `product_quality_score` for batches with a `raw_material_supplier` of 2 and a `pigment_quantity` greater than 35 kg.

Write a query to return the average `avg_product_quality_score` for these filtered batches. Use the original production data table, not the output of Task 2.

- You should start with the data in the file 'production_data.csv'. 
- Your output should be a DataFrame named pigment_data.
- It should consist of a 1-row DataFrame with 3 columns: `raw_material_supplier`, `pigment_quantity`, and `avg_product_quality_score`.
- Your answers should be rounded to 2 decimal places where appropriate.


# Task 4

In order to proceed with further analysis later, you need to analyze how various factors relate to product quality. Start by calculating the mean and standard deviation for the following columns: `pigment_quantity`, and `product_quality_score`. </br> These statistics will help in understanding the central tendency and variability of the data related to product quality.
</br> </br >
Next, calculate the Pearson correlation coefficient between the following variables: `pigment_quantity`, and `product_quality_score`.
</br>
These correlation coefficients will provide insights into the strength and direction of the relationships between the factors and overall product quality.


- You should start with the data in the file 'production_data.csv'.
- Calculate the mean and standard deviation for the columns pigment_quantity and product_quality_score as: `product_quality_score_mean`, `product_quality_score_sd`, `pigment_quantity_mean`, `pigment_quantity_sd`.
- Calculate the Pearson correlation coefficient between pigment_quantity and product_quality_score as: `corr_coef`
- Your output should be a DataFrame named product_quality.
- It should include the columns: `product_quality_score_mean`, `product_quality_score_sd`, `pigment_quantity_mean`, `pigment_quantity_sd`, `corr_coef`.
- Ensure that your answers are rounded to 2 decimal places.
