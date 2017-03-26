import numpy as np
import pandas as pd

class Dataset_manipulations(object):

    '''Проанализировать массив данных при помощи языка Python
    (допускается и рекомендуется использование дополнительных библиотек):
    вычисление среднего, максимального/минимального значений, медианы,
    моды числовых значений как для всего массива в целом,
    так и для каждого типа контента (столбец Type) в отдельности.
    Найти самый популярный объект в выборке, объяснить почему.
    Решение предоставить в виде .py/.ipynb файла на github.'''

    def __init__(self, file_path, df, column_name, info_column):
        self.file_path = file_path
        self.df = df
        self.column_name = column_name
        self.info_column = info_column

    def csv_to_DataFrame(file_path):
        return pd.read_csv(file_path, ';')

    def df_describe(df):
        return df.describe()

    def column_unique_elements(df, column_name):
        return df[column_name].unique()

    def column_unique_elements_info(df, column_name, info_column):
        list_of_elements = Dataset_manipulations.column_unique_elements(df, column_name)
        info_column_sums = []
        for i in list_of_elements:
            info_column_sums.append(np.sum(df[df[column_name] == i][info_column]))
        return dict(zip(list_of_elements, info_column_sums))

dataset_Facebook_df = Dataset_manipulations.csv_to_DataFrame(r"dataset_Facebook.csv")
dataset_Facebook_overview = Dataset_manipulations.df_describe(dataset_Facebook_df)
dataset_Facebook_Type_column_values = Dataset_manipulations.column_unique_elements(dataset_Facebook_df, "Type")
dataset_Facebook_likes_per_Type = Dataset_manipulations.column_unique_elements_info(dataset_Facebook_df, "Type", "like")

print(dataset_Facebook_df)
print(dataset_Facebook_overview)
print(dataset_Facebook_Type_column_values)
print(dataset_Facebook_likes_per_Type)

    
