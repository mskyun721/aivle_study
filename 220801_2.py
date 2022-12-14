import pandas as pd

dict = {'Name': ['Gildong', 'Sarang', 'Jiemae', 'Yeoin'],
        'Level': ['Gold', 'Bronze', 'Silver', 'Gold'],
        'Score': [56000, 23000, 44000, 52000]}
df = pd.DataFrame(dict)

print(dict)
print()
print(df)

# csv 불러오기
path = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv'
data = pd.read_csv(path)

print(data)
print()

# head : 상위 n번 개 행 불러오기 / default 5
print(data.head(10))
# tail : 하위 n번 개 행 불러오기 / default 5
print(data.tail(10))

path2 = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/Attrition_simple2.CSV'
# path2 = 'https://raw.githubusercontent.com/DA4BAM/dataset/master/airquality_simple.csv'
data2 = pd.read_csv(path2)

print(data2)
print(data2.head(10))
print(data2.shape)
print()
print(data2.columns)
print()
print(data2.columns.values)
print()
print(list(data2))
print()
print(data2.dtypes)
print()
print(data2.info())
print()
print(data2.describe())
print()
# sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)
print(data2.sort_values(by='MonthlyIncome', ascending=False))
print()
print(data2.sort_values(by=['JobSatisfaction', 'MonthlyIncome'], ascending=[True, False]))
print()
# 정렬 후 index reset
tmp = data2.sort_values(by='MonthlyIncome', ascending=False)
print(tmp.reset_index(drop=True))
print()
print(tmp.reset_index(drop=False))
print()
print(tmp.head(10))
print()
# series
print(data2['MonthlyIncome'])
print()
print(data2[['Age', 'MonthlyIncome']].mean())


### 종합실습
titanic = pd.read_csv('https://raw.githubusercontent.com/DA4BAM/dataset/master/titanic_simple.csv')

print(titanic.head())
print()
print(titanic.shape)
print()
print(titanic.dtypes)
print()
print(titanic.info())
print()
print(titanic.describe())
print()
print(titanic.value_counts('Embarked'))
print()
print(titanic.value_counts('Pclass'))
print()
print(titanic[['Embarked', 'Pclass']].value_counts())
print()
print(titanic[['Age', 'Fare']].max())
print()
print(titanic.sort_values(by='Fare', ascending=False).head(10))

