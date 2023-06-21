# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, lit, udf
from pyspark.sql.types import ArrayType, StringType
import itertools

# COMMAND ----------

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

split_udf = udf(lambda s: [x.strip() for x in s.split(',')], ArrayType(StringType()))

# COMMAND ----------

metadata_df = spark.read.csv('dbfs:/FileStore/FileStore/x_meta-1.txt', header=True, inferSchema=True, encoding='iso-8859-1')

# COMMAND ----------

time_fields = metadata_df.filter(metadata_df['TYPE'] == 'TIME').count()
dimension_fields = metadata_df.filter(metadata_df['TYPE'] == 'DIMENSION').count()
data_fields = metadata_df.filter(metadata_df['TYPE'] == 'DATA').count()

# Check if the number of fields in each category is valid
if time_fields != 1:
    raise ValueError("There should be exactly 1 'Time' field.")
if dimension_fields < 1:
    raise ValueError("There should be at least 1 'Dimension' field.")
if data_fields < 1:
    raise ValueError("There should be at least 1 'Data' field.")

# COMMAND ----------

time_members = metadata_df.filter(metadata_df['TYPE'] == 'TIME').select('MEMBERS').first()[0]
dimensions = metadata_df.filter(metadata_df['TYPE'] == 'DIMENSION').select(explode(split_udf(col('MEMBERS'))).alias('DIMENSION')).select('DIMENSION').rdd.flatMap(lambda x: x).collect()
data_members = metadata_df.filter(metadata_df['TYPE'] == 'DATA').select(explode(split_udf(col('MEMBERS'))).alias('DATA')).select('DATA').rdd.flatMap(lambda x: x).collect()
field_names = metadata_df.filter(metadata_df['TYPE'] != 'TIME').select('FIELD').rdd.flatMap(lambda x: x).collect()


# COMMAND ----------

num_rows = 1
for dimension in dimensions:
    num_rows *= len(dimension)

num_columns = len(metadata_df.columns) - 2

# COMMAND ----------

schema = ['#', 'DATA'] + field_names + ['DATA']

# COMMAND ----------

rows = []
row_num = 0
for data_member in data_members:
    for dimension_values in itertools.product(*dimensions):
        row = [row_num + 1, data_member[0]]
        row.extend(dimension_values)

        time_data = []
        for time_member in time_members:
            data = f'{data_member[0]}, {", ".join(dimension_values)}, {time_member}'
            time_data.append(data)

        row.append(', '.join(time_data))
        rows.append(row)
        row_num += 1
