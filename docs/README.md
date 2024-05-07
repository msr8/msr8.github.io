<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q1) Write all the ways to create a dataframe

<br>

## CODE

```python
import pandas as pd

# From a list of lists
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
df = pd.DataFrame(data)
print('From a list of lists:')
print(df)

# From a dictionary
data = {'a': [1, 4, 7], 'b': [2, 5, 8], 'c': [3, 6, 9]}
df = pd.DataFrame(data)
print('\nFrom a dictionary:')
print(df)

# From a list of dictionaries
data = [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}, {'a': 7, 'b': 8, 'c': 9}]
df = pd.DataFrame(data)
print('\nFrom a list of dictionaries:')
print(df)
```

<br>

## OUTPUT

<br>
From a list of lists:

|   0 |   1 |   2 |
|----:|----:|----:|
|   1 |   2 |   3 |
|   4 |   5 |   6 |
|   7 |   8 |   9 |

From a dictionary:

|   a |   b |   c |
|----:|----:|----:|
|   1 |   2 |   3 |
|   4 |   5 |   6 |
|   7 |   8 |   9 |

From a list of dictionaries:

|   a |   b |   c |
|----:|----:|----:|
|   1 |   2 |   3 |
|   4 |   5 |   6 |
|   7 |   8 |   9 |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q2) Given a dataset, print the following:

1) Records of index 1 & 3
2) Records where age >= 15
3) Records where age >= 12 and gender = Male
4) City and gender of people with age >= 12

<br>

## CODE

```python
import pandas as pd

data = {
    'age':            [10,22,13,21,12,11,17],
    'section':        ['A','B','C','B','B','A','A'],
    'city':           ['Gurgaon','Delhi','Mumbai','Delhi','Mumbai','Delhi','Mumbai'],
    'gender':         ['M','F','F','M','M','M','F'],
    'favorite_color': ['red','black','yellow','pink','black','green','red']   
}
df = pd.DataFrame(data)

print('\n1) Original data:')
print

print('\n2) Records of index 1 & 3')
res_df = df.iloc[ [1,3] , : ]
print(res_df)

print('\n3) Records where age >= 15:')
res_df = df.query('age >= 15')
print(res_df)

print('\n4) Records where age >= 12 and gender = Male:')
res_df = df.query('age >= 12 and gender == "M"')
print(res_df)

print('\n5) City and gender of people with age >= 12:')
df.query('age >= 12')[['city','gender']]
print(res_df)
```

<br>

## OUTPUT

<br>

1) Original data:

|   age | section   | city    | gender   | favorite_color   |
|------:|:----------|:--------|:---------|:-----------------|
|    10 | A         | Gurgaon | M        | red              |
|    22 | B         | Delhi   | F        | black            |
|    13 | C         | Mumbai  | F        | yellow           |
|    21 | B         | Delhi   | M        | pink             |
|    12 | B         | Mumbai  | M        | black            |
|    11 | A         | Delhi   | M        | green            |
|    17 | A         | Mumbai  | F        | red              |

2) Records of index 1 & 3

|   age | section   | city   | gender   | favorite_color   |
|------:|:----------|:-------|:---------|:-----------------|
|    22 | B         | Delhi  | F        | black            |
|    21 | B         | Delhi  | M        | pink             |

3) Records where age >= 15:

|   age | section   | city   | gender   | favorite_color   |
|------:|:----------|:-------|:---------|:-----------------|
|    22 | B         | Delhi  | F        | black            |
|    21 | B         | Delhi  | M        | pink             |
|    17 | A         | Mumbai | F        | red              |

4) Records where age >= 12 and gender = Male:

|   age | section   | city   | gender   | favorite_color   |
|------:|:----------|:-------|:---------|:-----------------|
|    21 | B         | Delhi  | M        | pink             |
|    12 | B         | Mumbai | M        | black            |

5) City and gender of people with age >= 12:

|   age | section   | city   | gender   | favorite_color   |
|------:|:----------|:-------|:---------|:-----------------|
|    21 | B         | Delhi  | M        | pink             |
|    12 | B         | Mumbai | M        | black            |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q3) Create a dataframe to store data of 10 students, with the columns being "Name", "Age", "Semester I marks out of 600", "Semester II marks out of 500", and "Attendance"

1) Display details of students who scored more than 560 marks in sem I
2) Display details of students who scored less than 250 marks in sem II
3) Display details of student who scored minimum marks in sem II
4) Display details of student who scored maximum marks in sem II
5) Display details of students whose attendance is more than 75
6) Display details of students whose attendance is less than 50
7) Insert 2 new records
8) Add a column corresponding to percentage of marks of both semesters
9) Add a new column corresponding to grades:

| Percentage   | Grade |
| ------------ | ----- |
| >=90         | O     |
| >=75 and <90 | A+    |
| >=60 and <75 | A     |
| >=50 and <60 | B+    |
| >=40 and <50 | B     |
| >40          | F     |

<br>

## CODE

```python
import pandas as pd

data = {
    'Name':                         ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Age':                          [20, 21, 20, 22, 23, 20, 21, 22, 20, 21],
    'Semester I marks out of 600':  [213, 31, 57, 406, 417, 45, 217, 200, 588, 319],
    'Semester II marks out of 500': [198, 378, 133, 450, 283, 485, 193, 283, 236, 191],
    'Attendance':                   [76, 26, 53, 32, 50, 67, 92, 62, 44, 85]
}
df = pd.DataFrame(data)

print('\nOriginal data:')
print

print('\n1) Students who scored more than 560 marks in sem I:')
ans = df.query('`Semester I marks out of 600` > 560')
print(ans)

print('\n2) Students who scored less than 250 marks in sem II:')
ans = df.query('`Semester II marks out of 500` < 250')
print(ans)

print('\n3) Student who scored minimum marks in sem II:')
min_marks = min(df['Semester II marks out of 500'])
ans       = df.query('`Semester II marks out of 500` == @min_marks')
print( ans  )

print('\n4) Student who scored maximum marks in sem II:')
ans = df.sort_values(by='Semester II marks out of 500',ascending=False).head(1)
print(ans)

print('\n5) Students whose attendance is more than 75:')
ans = df.query('Attendance > 75')
print(ans)

print('\n6) Students whose attendance is less than 50:')
ans = df.query('Attendance < 50')
print(ans)

print('\n7) Inserted two new records:')
new_data = {
    'Name':                         ['K', 'L'],
    'Age':                          [22,  23],
    'Semester I marks out of 600':  [300, 400],
    'Semester II marks out of 500': [400, 300],
    'Attendance':                   [80,  40]
}
new_df = pd.DataFrame(new_data)
df     = pd.concat([df,new_df], ignore_index=True)
print(index=True)

print('\n8) Added the percentage column:')
df['Percentage'] = (df['Semester I marks out of 600'] + df['Semester II marks out of 500']) / 11
df['Percentage'] = df['Percentage'].apply(lambda x: round(x,2))
print(df)

print('\n9) Added the grade column:')
def get_grade(x: float):
    if   x >= 90: return 'O'
    elif x >= 75: return 'A+'
    elif x >= 60: return 'A'
    elif x >= 50: return 'B+'
    elif x >= 40: return 'B'
    else:         return 'F'
df['Grade'] = df['Percentage'].apply(get_grade)
print(df)
```

<br>

## OUTPUT

<br>

Original data:

| Name   |   Age |   Semester I marks out of 600 |   Semester II marks out of 500 |   Attendance |
|:-------|------:|------------------------------:|-------------------------------:|-------------:|
| A      |    20 |                           213 |                            198 |           76 |
| B      |    21 |                            31 |                            378 |           26 |
| C      |    20 |                            57 |                            133 |           53 |
| D      |    22 |                           406 |                            450 |           32 |
| E      |    23 |                           417 |                            283 |           50 |
| F      |    20 |                            45 |                            485 |           67 |
| G      |    21 |                           217 |                            193 |           92 |
| H      |    22 |                           200 |                            283 |           62 |
| I      |    20 |                           588 |                            236 |           44 |
| J      |    21 |                           319 |                            191 |           85 |

1) Students who scored more than 560 marks in sem I:

|    | Name   |   Age |   Semester I marks out of 600 |   Semester II marks out of 500 |   Attendance |
|---:|:-------|------:|------------------------------:|-------------------------------:|-------------:|
|  8 | I      |    20 |                           588 |                            236 |           44 |

2) Students who scored less than 250 marks in sem II:

|    | Name   |   Age |   Semester I marks out of 600 |   Semester II marks out of 500 |   Attendance |
|---:|:-------|------:|------------------------------:|-------------------------------:|-------------:|
|  0 | A      |    20 |                           213 |                            198 |           76 |
|  2 | C      |    20 |                            57 |                            133 |           53 |
|  6 | G      |    21 |                           217 |                            193 |           92 |
|  8 | I      |    20 |                           588 |                            236 |           44 |
|  9 | J      |    21 |                           319 |                            191 |           85 |

3) Student who scored minimum marks in sem II:

|    | Name   |   Age |   Semester I marks out of 600 |   Semester II marks out of 500 |   Attendance |
|---:|:-------|------:|------------------------------:|-------------------------------:|-------------:|
|  2 | C      |    20 |                            57 |                            133 |           53 |

4) Student who scored maximum marks in sem II:

|    | Name   |   Age |   Semester I marks out of 600 |   Semester II marks out of 500 |   Attendance |
|---:|:-------|------:|------------------------------:|-------------------------------:|-------------:|
|  5 | F      |    20 |                            45 |                            485 |           67 |

5) Students whose attendance is more than 75:

|    | Name   |   Age |   Semester I marks out of 600 |   Semester II marks out of 500 |   Attendance |
|---:|:-------|------:|------------------------------:|-------------------------------:|-------------:|
|  0 | A      |    20 |                           213 |                            198 |           76 |
|  6 | G      |    21 |                           217 |                            193 |           92 |
|  9 | J      |    21 |                           319 |                            191 |           85 |

6) Students whose attendance is less than 50:

|    | Name   |   Age |   Semester I marks out of 600 |   Semester II marks out of 500 |   Attendance |
|---:|:-------|------:|------------------------------:|-------------------------------:|-------------:|
|  1 | B      |    21 |                            31 |                            378 |           26 |
|  3 | D      |    22 |                           406 |                            450 |           32 |
|  8 | I      |    20 |                           588 |                            236 |           44 |

7) Inserted two new records:

|    | Name   |   Age |   Semester I marks out of 600 |   Semester II marks out of 500 |   Attendance |
|---:|:-------|------:|------------------------------:|-------------------------------:|-------------:|
|  0 | A      |    20 |                           213 |                            198 |           76 |
|  1 | B      |    21 |                            31 |                            378 |           26 |
|  2 | C      |    20 |                            57 |                            133 |           53 |
|  3 | D      |    22 |                           406 |                            450 |           32 |
|  4 | E      |    23 |                           417 |                            283 |           50 |
|  5 | F      |    20 |                            45 |                            485 |           67 |
|  6 | G      |    21 |                           217 |                            193 |           92 |
|  7 | H      |    22 |                           200 |                            283 |           62 |
|  8 | I      |    20 |                           588 |                            236 |           44 |
|  9 | J      |    21 |                           319 |                            191 |           85 |
| 10 | K      |    22 |                           300 |                            400 |           80 |
| 11 | L      |    23 |                           400 |                            300 |           40 |

8) Added the percentage column:

| Name   |   Age |   Semester I marks out of 600 |   Semester II marks out of 500 |   Attendance |   Percentage |
|:-------|------:|------------------------------:|-------------------------------:|-------------:|-------------:|
| A      |    20 |                           213 |                            198 |           76 |        37.36 |
| B      |    21 |                            31 |                            378 |           26 |        37.18 |
| C      |    20 |                            57 |                            133 |           53 |        17.27 |
| D      |    22 |                           406 |                            450 |           32 |        77.82 |
| E      |    23 |                           417 |                            283 |           50 |        63.64 |
| F      |    20 |                            45 |                            485 |           67 |        48.18 |
| G      |    21 |                           217 |                            193 |           92 |        37.27 |
| H      |    22 |                           200 |                            283 |           62 |        43.91 |
| I      |    20 |                           588 |                            236 |           44 |        74.91 |
| J      |    21 |                           319 |                            191 |           85 |        46.36 |
| K      |    22 |                           300 |                            400 |           80 |        63.64 |
| L      |    23 |                           400 |                            300 |           40 |        63.64 |

9) Added the grade column:

| Name   |   Age |   Semester I marks out of 600 |   Semester II marks out of 500 |   Attendance |   Percentage | Grade   |
|:-------|------:|------------------------------:|-------------------------------:|-------------:|-------------:|:--------|
| A      |    20 |                           213 |                            198 |           76 |        37.36 | F       |
| B      |    21 |                            31 |                            378 |           26 |        37.18 | F       |
| C      |    20 |                            57 |                            133 |           53 |        17.27 | F       |
| D      |    22 |                           406 |                            450 |           32 |        77.82 | A+      |
| E      |    23 |                           417 |                            283 |           50 |        63.64 | A       |
| F      |    20 |                            45 |                            485 |           67 |        48.18 | B       |
| G      |    21 |                           217 |                            193 |           92 |        37.27 | F       |
| H      |    22 |                           200 |                            283 |           62 |        43.91 | B       |
| I      |    20 |                           588 |                            236 |           44 |        74.91 | A       |
| J      |    21 |                           319 |                            191 |           85 |        46.36 | B       |
| K      |    22 |                           300 |                            400 |           80 |        63.64 | A       |
| L      |    23 |                           400 |                            300 |           40 |        63.64 | A       |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q4) Create a DataFrame based on E-Commerce data and generate mean, mode, and median

<br>

## CODE

```python
import pandas as pd

data = {
    'Order_ID':     ['101', '102', '103', '104', '105'],
    'Price':        [50, 20, 40, 50, 45],
    'Quantity':     [2, 3, 1, 2, 1]
}
df = pd.DataFrame(data)
print('\n1) Original dataframe:')
print(df)

mean_df   = df.mean(numeric_only=True)
mode_df   = df.mode(numeric_only=True)
median_df = df.median(numeric_only=True)

print('\n2) Means: ')
print(mean_df)
print('\n3) Modes: ')
print(mode_df)
print('\n4) Medians: ')
print(median_df)
```

<br>

## OUTPUT

<br>

1) Original dataframe:

|   Order_ID |   Price |   Quantity |
|-----------:|--------:|-----------:|
|        101 |      50 |          2 |
|        102 |      20 |          3 |
|        103 |      40 |          1 |
|        104 |      50 |          2 |
|        105 |      45 |          1 |

2) Means: 

|          |    0 |
|:---------|-----:|
| Price    | 41   |
| Quantity |  1.8 |

3) Modes: 

|    |   Price |   Quantity |
|---:|--------:|-----------:|
|  0 |      50 |          1 |
|  1 |     nan |          2 |

4) Medians: 

|          |   0 |
|:---------|----:|
| Price    |  45 |
| Quantity |   2 |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q5) Write a program to implement pivot() and pivot-table() on a DataFrame

<br>

## CODE

```python
import pandas as pd

data = {
    'Day':         ['Monday', 'Monday', 'Tuesday', 'Tuesday', 'Wednesday', 'Wednesday'],
    'City':        ['Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai'],
    'Temperature': [32, 34, 33, 35, 34, 36],
}
df = pd.DataFrame(data)
print('\n1) Dataframe for pivot(): ')
print(df)

pivot_df = df.pivot(index='Day', columns='City', values='Temperature')
print('\n2) pivot(): ')
print(pivot_df)

data = {
    'Day':         ['Monday', 'Monday', 'Monday', 'Tuesday', 'Tuesday', 'Tuesday'],
    'City':        ['Delhi', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Mumbai'],
    'Temperature': [32, 33, 36, 33, 36, 37],
}
df = pd.DataFrame(data)
print('\n3) Dataframe for pivot_table(): ')
print(df)

pivot_table_df = df.pivot_table(index='Day', columns='City', values='Temperature', aggfunc='count')
print('\n4) pivot_table(): ')
print(pivot_table_df)
```

<br>

## OUTPUT

<br>

1) Dataframe for pivot(): 

| Day       | City   |   Temperature |
|:----------|:-------|--------------:|
| Monday    | Delhi  |            32 |
| Monday    | Mumbai |            34 |
| Tuesday   | Delhi  |            33 |
| Tuesday   | Mumbai |            35 |
| Wednesday | Delhi  |            34 |
| Wednesday | Mumbai |            36 |

2) pivot(): 

| Day       |   Delhi |   Mumbai |
|:----------|--------:|---------:|
| Monday    |      32 |       34 |
| Tuesday   |      33 |       35 |
| Wednesday |      34 |       36 |

3) Dataframe for pivot_table(): 

| Day     | City   |   Temperature |
|:--------|:-------|--------------:|
| Monday  | Delhi  |            32 |
| Monday  | Delhi  |            33 |
| Monday  | Mumbai |            36 |
| Tuesday | Delhi  |            33 |
| Tuesday | Mumbai |            36 |
| Tuesday | Mumbai |            37 |

4) pivot_table(): 

| Day     |   Delhi |   Mumbai |
|:--------|--------:|---------:|
| Monday  |       2 |        1 |
| Tuesday |       1 |        2 |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q6) Write a Program to read a CSV file and create its DataFrame

<br>

## CODE

```python
import pandas as pd

filename = 'data.csv'
print(f'\n1) Contents of {filename}:')
with open(filename) as f:
    print(f.read())

df = pd.read_csv(filename)
print('\n2) Dataframe:')
print(df)
```

<br>

## OUTPUT

<br>

1) Contents of data.csv:
Name,Age,Gender
Ram,16,M
Manish,18,M
Sahil,15,M
Amrit,20,F
Mark,19,M


2) Dataframe:

| Name   |   Age | Gender   |
|:-------|------:|:---------|
| Ram    |    16 | M        |
| Manish |    18 | M        |
| Sahil  |    15 | M        |
| Amrit  |    20 | F        |
| Mark   |    19 | M        |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q7) Consider the DataFrame QtrSales where each row contains the item category, item name and expenditure and group the rows by category, and print the average expenditure per category

<br>

## CODE

```python
import pandas as pd

QtrSales = pd.DataFrame({
    'category':    ['Electronics', 'Electronics', 'Fashion', 'Fashion', 'Electronics', 'Fashion'],
    'item_name':   ['Laptop', 'Headphones', 'T-Shirt', 'Jeans', 'Smartphone', 'Shoes'],
    'expenditure': [1200, 100, 31, 50, 800, 60]
})
print('\n1) Original dataframe:')
print(QtrSales)

grouped = QtrSales.groupby(by='category')['expenditure']
mean_df = grouped.mean()
print('\n2) Average expenditure per category:')
print(mean_df)
```

<br>

## OUTPUT

<br>

1) Original dataframe:

| category    | item_name   |   expenditure |
|:------------|:------------|--------------:|
| Electronics | Laptop      |          1200 |
| Electronics | Headphones  |           100 |
| Fashion     | T-Shirt     |            31 |
| Fashion     | Jeans       |            50 |
| Electronics | Smartphone  |           800 |
| Fashion     | Shoes       |            60 |

2) Average expenditure per category:

| category    |   expenditure |
|:------------|--------------:|
| Electronics |           700 |
| Fashion     |            47 |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q8) Create a DataFrame having age, name, weight of five students. Write a program to display only the weight of first and fourth rows

<br>

## CODE

```python
import pandas as pd

data = {
    'name':   ['John', 'Emma', 'Michael', 'Sophia', 'William'],
    'age':    [20, 21, 22, 20, 23],
    'weight': [70, 65, 75, 68, 72]
}
df = pd.DataFrame(data)
print('\n1) Original dataframe:')
print(df)

weight_df = df.loc[ [0,3] , ['weight'] ]
print('\n2) Weight of the first and fourth rows:')
print(weight_df)
```

<br>

## OUTPUT

<br>

1) Original dataframe:

|    | name    |   age |   weight |
|---:|:--------|------:|---------:|
|  0 | John    |    20 |       70 |
|  1 | Emma    |    21 |       65 |
|  2 | Michael |    22 |       75 |
|  3 | Sophia  |    20 |       68 |
|  4 | William |    23 |       72 |

2) Weight of the first and fourth rows:

|    |   weight |
|---:|---------:|
|  0 |       70 |
|  3 |       68 |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q9) Write a program to create a DataFrame to store weight, age and name of three people. Print the DataFrame and its transpose

<br>

## CODE

```python
import pandas as pd

data = {
    'name':   ['John', 'Emma', 'Michael', 'Sophia', 'William'],
    'age':    [20, 21, 22, 20, 23],
    'weight': [70, 65, 75, 68, 72]
}
df = pd.DataFrame(data)
print('\n1) Original dataframe:')
print(df)

print('\n2) Transpose of the dataframe:')
print(df.T)
```

<br>

## OUTPUT

<br>

1) Original dataframe:

|    | name    |   age |   weight |
|---:|:--------|------:|---------:|
|  0 | John    |    20 |       70 |
|  1 | Emma    |    21 |       65 |
|  2 | Michael |    22 |       75 |
|  3 | Sophia  |    20 |       68 |
|  4 | William |    23 |       72 |

2) Transpose of the dataframe:

|        | 0    | 1    | 2       | 3      | 4       |
|:-------|:-----|:-----|:--------|:-------|:--------|
| name   | John | Emma | Michael | Sophia | William |
| age    | 20   | 21   | 22      | 20     | 23      |
| weight | 70   | 65   | 75      | 68     | 72      |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q10) Create a pandas series from a dictionary of values and an ndarray

<br>

## CODE

```python
import pandas as pd
import numpy as np

data = {
    'Name':   np.array([ 'Ram', 'Manish', 'Sahil', 'Amrit', 'Mark' ]),
    'Age':    np.array([ 16, 18, 15, 20, 19 ]),
    'Gender': np.array([ 'M', 'M', 'M', 'F', 'M' ])
}
df = pd.DataFrame(data)
print('\n1) Dataframe created from a dictionary of values and ndarray:')
print(df)
```

<br>

## OUTPUT

<br>

1) Dataframe created from a dictionary of values and ndarray:

| Name   |   Age | Gender   |
|:-------|------:|:---------|
| Ram    |    16 | M        |
| Manish |    18 | M        |
| Sahil  |    15 | M        |
| Amrit  |    20 | F        |
| Mark   |    19 | M        |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q11) Perform sorting on Series data and DataFrames

<br>

## CODE

```python
import pandas as pd

data = {
    'name':    ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    'year':    [2012, 2012, 2013, 2014, 2014],
    'reports': [4, 24, 31, 2, 3]
}
df        = pd.DataFrame(data)
print('\n1) Original dataframe:')
print(df)

sorted_df = df.sort_values(by='reports', ascending=False)
print('\n2) Sorted dataframe (based on reports) in descending order:')
print(sorted_df)

s = pd.Series([3, 1, 2, 3, 4])
print('\n3) Original series:')
print(s)

s.sort_values(inplace=True)
print('\n4) Sorted series in ascending order:')
print(s)
```

<br>

## OUTPUT

<br>

1) Original dataframe:

| name   |   year |   reports |
|:-------|-------:|----------:|
| Jason  |   2012 |         4 |
| Molly  |   2012 |        24 |
| Tina   |   2013 |        31 |
| Jake   |   2014 |         2 |
| Amy    |   2014 |         3 |

2) Sorted dataframe (based on reports) in descending order:

| name   |   year |   reports |
|:-------|-------:|----------:|
| Tina   |   2013 |        31 |
| Molly  |   2012 |        24 |
| Jason  |   2012 |         4 |
| Amy    |   2014 |         3 |
| Jake   |   2014 |         2 |

3) Original series:

|   0 |
|----:|
|   3 |
|   1 |
|   2 |
|   3 |
|   4 |

4) Sorted series in ascending order:

|   0 |
|----:|
|   1 |
|   2 |
|   3 |
|   3 |
|   4 |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q12) Two Series object, Population stores the details of four metro cities of India and another object AvgIncome stores the total average income reported in four years in these cities. Calculate income per capita for each of these metro cities

<br>

## CODE

```python
import pandas as pd

Population = pd.Series({'Delhi': 20000000, 'Mumbai': 22000000, 'Bangalore': 12000000, 'Kolkata': 15000000})
AvgIncome  = pd.Series({'Delhi': 350000,   'Mumbai': 320000,   'Bangalore': 300000,   'Kolkata': 280000})
print('\n1) Population:')
print(Population)
print('\n2) AvgIncome:')
print(AvgIncome)

income_per_capita = AvgIncome / Population
print("\n3) Income per capita for each metro city:")
print(income_per_capita)
```

<br>

## OUTPUT

<br>

1) Population:

|           |       0 |
|:----------|--------:|
| Delhi     | 2e+07   |
| Mumbai    | 2.2e+07 |
| Bangalore | 1.2e+07 |
| Kolkata   | 1.5e+07 |

2) AvgIncome:

|           |      0 |
|:----------|-------:|
| Delhi     | 350000 |
| Mumbai    | 320000 |
| Bangalore | 300000 |
| Kolkata   | 280000 |

3) Income per capita for each metro city:

|           |         0 |
|:----------|----------:|
| Delhi     | 0.0175    |
| Mumbai    | 0.0145455 |
| Bangalore | 0.025     |
| Kolkata   | 0.0186667 |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q13) Series objects Temp1, Temp2, Temp3, and Temp4 store the temperature of days of week 1, week 2, week 3, week 4. Write a script to:
1) Print average temperature per week
2) Print average temperature of entire month

<br>

## CODE

```python
import pandas as pd

Temp1   = pd.Series([20, 22, 21, 23, 25], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
Temp2   = pd.Series([24, 23, 22, 21, 20], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
Temp3   = pd.Series([22, 23, 24, 25, 26], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
Temp4   = pd.Series([25, 24, 23, 22, 21], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
temp_df = pd.DataFrame({'Week 1': Temp1, 'Week 2': Temp2, 'Week 3': Temp3, 'Week 4': Temp4})
print('\n1) Original data:')
print(temp_df)

mean_df = temp_df.mean()
print("\n2) Average temperature per week:")
print(mean_df)

print("\n3) Average temperature of the entire month: ", temp_df.values.mean())
```

<br>

## OUTPUT

<br>

1) Original data:

|           |   Week 1 |   Week 2 |   Week 3 |   Week 4 |
|:----------|---------:|---------:|---------:|---------:|
| Monday    |       20 |       24 |       22 |       25 |
| Tuesday   |       22 |       23 |       23 |       24 |
| Wednesday |       21 |       22 |       24 |       23 |
| Thursday  |       23 |       21 |       25 |       22 |
| Friday    |       25 |       20 |       26 |       21 |

2) Average temperature per week:

|        |    0 |
|:-------|-----:|
| Week 1 | 22.2 |
| Week 2 | 22   |
| Week 3 | 24   |
| Week 4 | 23   |

3) Average temperature of the entire month:  22.8



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q14) Write a pandas program to convert a series of lists to one series

<br>

## CODE

```python
import pandas as pd

s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']
])
print("\n1) Original Series:")
print(s)

ans = []
for i in s: ans.extend(i)
ret = pd.Series(ans)
print("\n2) Resultant Series:")
print(ret)
```

<br>

## OUTPUT

<br>

1) Original Series:

| 0                         |
|:--------------------------|
| ['Red', 'Green', 'White'] |
| ['Red', 'Black']          |
| ['Yellow']                |

2) Resultant Series:

| 0      |
|:-------|
| Red    |
| Green  |
| White  |
| Red    |
| Black  |
| Yellow |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q15) Write a pandas program to compare elements of two series

<br>

## CODE

```python
import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([4, 0, 3, 7, 4])

print("\n1) Original series':")
print(s1)
print('\n')
print(s2)

print("\n2) Comparing each element one by one:")
for i,j in zip(s1, s2):
    if   i == j: print(f'{i} == {j}')
    elif i > j:  print(f'{i} > {j}')
    else:        print(f'{i} < {j}')
```

<br>

## OUTPUT

<br>

1) Original series':

|   0 |
|----:|
|   1 |
|   2 |
|   3 |
|   4 |
|   5 |



|   0 |
|----:|
|   4 |
|   0 |
|   3 |
|   7 |
|   4 |

2) Comparing each element one by one:
1 < 4
2 > 0
3 == 3
4 < 7
5 > 4



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q16) Write a pandas program to create a subset of a given series based on values and condition

<br>

## CODE

```python
import pandas as pd

s = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print("\n1) Original series:")
print(s)

print("\n2) Subset of elements smaller than 6")
new_s = s[s < 6]
print(new_s)
```

<br>

## OUTPUT

<br>

1) Original series:

|   0 |
|----:|
|   0 |
|   1 |
|   2 |
|   3 |
|   4 |
|   5 |
|   6 |
|   7 |
|   8 |
|   9 |

2) Subset of elements smaller than 6

|   0 |
|----:|
|   0 |
|   1 |
|   2 |
|   3 |
|   4 |
|   5 |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q17) Given the dataset Toyota.csv, do the following operations: 	

1. Upload Toyota.csv in dataframe df.
2. What is the data type of MetColor?
3. How many null values are there in the KM field?
4. Which column has 7 unique values?
5. How many records are there? What is the mean and median of age grouped by FuelType?
6. Replace three, four, five value in Doors column to 3,4,5 respectively
7. Change the datatype of Doors to int64
8. Impute the value of Price with median
9. Replace "????" in HP field with mean
10. Impute blank values in FuelType with Mode.
11. Delete the rows with MetColor and Age as blank
12. Replace “??” value in KM with Mean
13. What is the mean, median and mode of the KM field?
14. Create a new column “Category” based on the value of the column “Age” according to the following table:

| Value | Category |
| :---: | :------: |
| 0-10  | Old      |
| 11-20 | Medium   |
| 20+   | New      |

15. Create Dummy fields for the FuelType column



<br>

## CODE

```python
import pandas as pd


# 1) Upload Toyota.csv in dataframe df
df = pd.read_csv('Toyota.csv')

# 2) What is the data type of MetColor?
metcolor_dtype = df['MetColor'].dtype
print(f'\n2) Datatype of the MetColor column is ', metcolor_dtype)

# 3) How many null value are there in KM field?
num_null = df['KM'].isnull().sum()
print(f'\n3) The KM column has {num_null} null values')

# 4) Which column has 7 unique values?
for col in df.columns:
    if df[col].nunique() == 7:
        print(f'\n4) The {col} column has 7 unique values')
else:
    print('\n4) No column with 7 unique values')

# 5) How many records are there?
print(f'\n5) There are a total of {len(df)} records')

# 6) Replace three, four, five value in Doors column to 3,4,5 respectively.
replace_dict = {'three': 3, 'four': 4, 'five': 5}
df['Doors'] = df['Doors'].replace(replace_dict)

# 7) Change the datatype of Doors to int64
df['Doors'] = df['Doors'].astype('int64')

# 8) Impute the value of Price with median
median_price = df['Price'].median()
df['Price']  = df['Price'].fillna(median_price)

# 9) Replace "????"" in HP field with mean
temp     = df['HP']
temp     = temp[temp != '????']
temp     = temp.astype('int64')
mean_hp  = temp.mean()
df['HP'] = df['HP'].replace('????', mean_hp)

# 10) Impute blank values in FuelType with Mode
mode_fueltype  = df['FuelType'].mode()[0]
df['FuelType'] = df['FuelType'].fillna(mode_fueltype)

# 11) Delete the rows with MetColor and Age as blank
df.dropna(subset=['MetColor', 'Age'], inplace=True)

# 12) Replace ?? value in KM with Mean
temp     = df['KM']
temp     = temp[temp != '??']
temp     = temp.astype('int64')
mean_km  = temp.mean()
df['KM'] = df['KM'].replace('??', mean_km)

# 13) What is the mean, median and mode of KM field
km = df['KM'].astype('int64')
print(f'\n13.1) Mean of KM:   {mean_km}')
print(f'13.2) Median of KM: {km.median()}')
print(f'13.3) Mode of KM:   {km.mode()[0]}')

# 14) Create a new column "Category" based on the value of the column "Age"
def func(val):
    if   val <= 10: return 'New'
    elif val <= 20: return 'Medium'
    else:           return 'Old'
df['Category'] = df['Age'].apply(func)

# 15) Create Dummy fields for FuelType
df = pd.get_dummies(df, columns=['FuelType'])
```

<br>

## OUTPUT

<br>

2) Datatype of the MetColor column is  float64

3) The KM column has 0 null values

4) The Doors column has 7 unique values

4) No column with 7 unique values

5) There are a total of 1436 records

13.1) Mean of KM:   69006.62001696353
13.2) Median of KM: 63875.5
13.3) Mode of KM:   69006



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q18) Write a pandas program to change the order of index of a given series

<br>

## CODE

```python
s = pd.Series(data = [1, 2, 3, 4, 5], index = ['A', 'B', 'C', 'D', 'E'])
print("Original series:")
print(s)

s = s.reindex(index = ['B', 'A', 'C', 'D', 'E'])
print("\nSeries after changing the order of index:")
print(s)
```

<br>

## OUTPUT

<br>
Original series:

|    |   0 |
|:---|----:|
| A  |   1 |
| B  |   2 |
| C  |   3 |
| D  |   4 |
| E  |   5 |

Series after changing the order of index:

|    |   0 |
|:---|----:|
| B  |   2 |
| A  |   1 |
| C  |   3 |
| D  |   4 |
| E  |   5 |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q19) Write a pandas program to get the items of a given series not present in another given series

<br>

## CODE

```python
import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([1, 20, 30, 4, 50])

print("S1:")
print(s1)
print("\nS2:")
print(s2)

print("\nItems of s1 not present in s2:")
ans = s1[~s1.isin(s2)]
print(ans)
```

<br>

## OUTPUT

<br>
S1:

|   0 |
|----:|
|   1 |
|   2 |
|   3 |
|   4 |
|   5 |

S2:

|   0 |
|----:|
|   1 |
|  20 |
|  30 |
|   4 |
|  50 |

Items of s1 not present in s2:

|   0 |
|----:|
|   2 |
|   3 |
|   5 |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q20) Write a pandas program to calculate the frequency counts of each unique value of a given series

<br>

## CODE

```python
import pandas as pd
s = pd.Series([1,1,2,2,2,3,4,4,4,4,4,5,5,5,5,5])
print("Original Series:")
print(s)

print("\nFrequency of each unique value:")
freq = s.value_counts()
print(freq)
```

<br>

## OUTPUT

<br>
Original Series:

|   0 |
|----:|
|   1 |
|   1 |
|   2 |
|   2 |
|   2 |
|   3 |
|   4 |
|   4 |
|   4 |
|   4 |
|   4 |
|   5 |
|   5 |
|   5 |
|   5 |
|   5 |

Frequency of each unique value:

|    |   count |
|---:|--------:|
|  4 |       5 |
|  5 |       5 |
|  2 |       3 |
|  1 |       2 |
|  3 |       1 |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q21) Create a Series and print all the elements that are above 75th percentile

<br>

## CODE

```python
import pandas as pd

s      = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
per_75 = s.quantile(0.75)
ans    = s[s > per_75]

print("\nAll the elements above the 75th percentile are:")
print(ans)
```

<br>

## OUTPUT

<br>

All the elements above the 75th percentile are:

|   0 |
|----:|
|   8 |
|   9 |
|  10 |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q22) Write a program to find the MAD (mean absolute deviation) of all columns in a dataframe

<br>

## CODE

```python
import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 100]
})

ans = pd.Series()
for col in df:
    mean  = df[col].mean()
    diffs = df[col] - mean
    diffs = diffs.abs()
    mad   = diffs.mean()
    ans[col] = mad

print('Original dataframe:')
print(df)
print('\nMADs: ')
print(ans)
```

<br>

## OUTPUT

<br>
Original dataframe:

|   A |   B |
|----:|----:|
|   1 |   6 |
|   2 |   7 |
|   3 |   8 |
|   4 |   9 |
|   5 | 100 |

MADs: 

|    |    0 |
|:---|-----:|
| A  |  1.2 |
| B  | 29.6 |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q23) Create a dataframe based on employee data and generate quartile and variance

<br>

## CODE

```python
import pandas as pd

df = pd.DataFrame({
    'Name':   ['A', 'B', 'C', 'D', 'E'],
    'Salary': [1000, 2000, 3000, 4000, 5000],
    'Age':    [20, 30, 40, 50, 60]
})

quartiles = df.quantile([0.25, 0.5, 0.75], numeric_only=True)
variances = df.var(numeric_only=True)

print('Original dataframe:')
print(df)
print('\nQuartiles:')
print(quartiles)
print('\nVariances:')
print(variances)
```

<br>

## OUTPUT

<br>
Original dataframe:

| Name   |   Salary |   Age |
|:-------|---------:|------:|
| A      |     1000 |    20 |
| B      |     2000 |    30 |
| C      |     3000 |    40 |
| D      |     4000 |    50 |
| E      |     5000 |    60 |

Quartiles:

|      |   Salary |   Age |
|-----:|---------:|------:|
| 0.25 |     2000 |    30 |
| 0.5  |     3000 |    40 |
| 0.75 |     4000 |    50 |

Variances:

|        |         0 |
|:-------|----------:|
| Salary |   2.5e+06 |
| Age    | 250       |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q24) Write a program to implement skewness on random data

<br>

## CODE

```python
# Create a DataFrame
df = pd.DataFrame({
    'normal':  np.random.normal(loc=0, scale=0.1, size=1000),
    'randint': np.random.randint(1, 100, 1000),
    'random':  np.random.random(1000)
})

# Calculate skewness
skew_df = df.skew()
print("Skewness on random data:")
print(skew_df)
```

<br>

## OUTPUT

<br>
Skewness on random data:

|         |          0 |
|:--------|-----------:|
| normal  | -0.0675594 |
| randint |  0.0318323 |
| random  | -0.118303  |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q25) Create a dataframe of any data and compute the kurtosis

<br>

## CODE

```python
# Create a DataFrame
df = pd.DataFrame({
    'normal':  np.random.normal(loc=0, scale=0.1, size=1000),
    'randint': np.random.randint(1, 100, 1000),
    'random':  np.random.random(1000)
})

# Calculate kurtosis
kurt_df = df.kurtosis()
print("Kurtosis:")
print(kurt_df)
```

<br>

## OUTPUT

<br>
Kurtosis:

|         |         0 |
|:--------|----------:|
| normal  | -0.209502 |
| randint | -1.17171  |
| random  | -1.22393  |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q26) Give the code or syntax to perform the following operation on two 2D numpy array array1 and array2 and 1D array array3

1) Add array1 and array2
2) Find sum of array1 elements over a given axis
3) Find product of array2 elements over a given axis
4) Change the dimension of array3 to 2D
5) Transpose the array created in part 4
6) Display 2 rows and the third column of the 2D array
7) Join two 2D arrays along row
8) Convert array2 to a 1D array
9) Split array1 into multiple subarrays

<br>

## CODE

```python
import numpy as np

array1 = np.array([[1,2,3], [4,5,6]])
array2 = np.array([[7,8,9], [10,11,12]])
array3 = np.array([13,14,15,16])

print('Original arrays:')
print('array1: ', array1)
print('array2: ', array2)
print('array3: ', array3)


# 1) Add array1 and array2
new_arr = array1 + array2
print('\n1)', new_arr)

# 2) Find sum of array1 elements over a given axis
new_arr = np.sum(array1, axis=0)
print('\n2)', new_arr)

# 3) Find product of array2 elements over a given axis
new_arr = np.prod(array1, axis=0)
print('\n3)', new_arr)

# 4) Change the dimension of array3 to 2D
new_arr = array3.reshape(2,2)
print('\n4)', new_arr)

# 5) Transpose the array created in part 4
new_arr = new_arr.T
print('\n5)', new_arr)

# 6) Display 2 rows and the third column of the 2D array
new_arr = array1[:2, 2]
print('\n6)', new_arr)

# 7) Join two 2D arrays along row
new_arr = np.concatenate((array1, array2), axis=0)
print('\n7)', new_arr)

# 8) Convert array2 to a 1D array
new_arr = array2.flatten()
print('\n8)', new_arr)

# 9) Split array1 into multiple subarrays
new_arr = np.array_split(array1, 2)
print('\n9)', new_arr)
```

<br>

## OUTPUT

<br>
Original arrays:
array1:  [[1 2 3]
 [4 5 6]]
array2:  [[ 7  8  9]
 [10 11 12]]
array3:  [13 14 15 16]

1) [[ 8 10 12]
 [14 16 18]]

2) [5 7 9]

3) [ 4 10 18]

4) [[13 14]
 [15 16]]

5) [[13 15]
 [14 16]]

6) [3 6]

7) [[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

8) [ 7  8  9 10 11 12]

9) [array([[1, 2, 3]]), array([[4, 5, 6]])]



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q27) Write python code to create the following series:

|     |        |
|-----|--------|
| 101 | Harsh  |
| 102 | Arun   |
| 103 | Ankur  |
| 104 | Harpal |
| 105 | Divya  |
| 106 | Jeet   |


1) Show the details of the first 3 employees using the head method
2) Show the details of the last 3 employees using the tail method
3) Show the details of the first 3 employees without using the head method
4) Show the details of the last 3 employees without using the tail method
5) Show the value of index number 102
6) Show 2nd to 4th records (inclusive)
7) Show the values at indexes 101, 103, and 105
8) Show details of "Arun"

<br>

## CODE

```python
import pandas as pd

s = pd.Series(
    ['Harsh', 'Arun', 'Ankur', 'Harpal', 'Divya', 'Jeet'],
    index=[101, 102, 103, 104, 105, 106]
)


# 1) Show the details of the first 3 employees using the head method
new_df = s.head(3) 
print('\n1)')
print(new_df)

# 2) Show the details of the last 3 employees using the tail method
new_df = s.tail(3)
print('\n2)')
print(new_df)

# 3) Show the details of the first 3 employees without using the head method
new_df = s[:3]
print('\n3)')
print(new_df)

# 4) Show the details of the last 3 employees without using the tail method
new_df = s[-3:]
print('\n4)')
print(new_df)

# 5) Show the value of index number 102
print('\n5)', s[102])

# 6) Show 2nd to 4th records (inclusive)
new_df = s[1:4]
print('\n6)')
print(new_df)

# 7) Show the values at indexes 101, 103, and 105
new_df = s[ [101,103,105] ]
print('\n7)')
print(new_df)

# 8) Show details of "Arun"
new_df = s[s == 'Arun']
print('\n8)')
print(new_df)
```

<br>

## OUTPUT

<br>

1)

|     | 0     |
|----:|:------|
| 101 | Harsh |
| 102 | Arun  |
| 103 | Ankur |

2)

|     | 0      |
|----:|:-------|
| 104 | Harpal |
| 105 | Divya  |
| 106 | Jeet   |

3)

|     | 0     |
|----:|:------|
| 101 | Harsh |
| 102 | Arun  |
| 103 | Ankur |

4)

|     | 0      |
|----:|:-------|
| 104 | Harpal |
| 105 | Divya  |
| 106 | Jeet   |

5) Arun

6)

|     | 0      |
|----:|:-------|
| 102 | Arun   |
| 103 | Ankur  |
| 104 | Harpal |

7)

|     | 0     |
|----:|:------|
| 101 | Harsh |
| 103 | Ankur |
| 105 | Divya |

8)

|     | 0    |
|----:|:-----|
| 102 | Arun |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q28) Create a dataframe for the below given data:

| SNO | Batsman        | Test | ODI  | T20  |
| --- | -------------- | ---- | ---- | ---- |
| 1   | Virat Kohli    | 3543 | 2245 | 1925 |
| 2   | Ajinkya Rehane | 2578 | 2165 | 1853 |
| 3   | Rohit Sharma   | 2280 | 2080 | 1522 |
| 4   | Shikhar Dhawan | 2158 | 1957 | 1020 |
| 5   | Hardik Pandya  | 1879 | 1856 | 980  |

1) Print the batsman name along with runs scored in Test and T20 using column names and dot notation
2) Display the batsman name along with runs scored in the ODI using the loc method
3) Display the batsman details who scored runs:
    - More than 2000 in ODI
    - Less than 2500 in Test
    - More than 1500 in T20
4) Display the columns using the column index number like 0, 2, and 4
5) Display the alternate rows
6) Reindex the dataframe created above with batsman name and delete the data of Hardik Pandya and Shikhar Dhawan by their index from the original dataframe
7) Insert two rows in the dataframe and delete rows whose index is 1 and 4
8) Delete the column Test, and add one more column “total”, ie the total of ODI and T20 runs
9) Rename the column “T20” to “T20I Runs”
10) Print the dataframe without headers

<br>

## CODE

```python
import pandas as pd

data = {
    'SNO':     [1, 2, 3, 4, 5],
    'Batsman': ['Virat Kohli', 'Ajinkya Rehane', 'Rohit Sharma', 'Shikhar Dhawan', 'Hardik Pandya'],
    'Test':    [3543, 2578, 2280, 2158, 1879],
    'ODI':     [2245, 2165, 2080, 1957, 1856],
    'T20':     [1925, 1853, 1522, 1020, 980]
}

df = pd.DataFrame(data)


# 1) Print the batsman name along with runs scored in Test and T20 using column names and dot notation
new_df = pd.DataFrame({'Batsman': df.Batsman, 'Test': df.Test, 'T20': df.T20})
print('\n1)')
print(new_df)

# 2) Display the batsman name along with runs scored in the ODI using the loc method
new_df = df.loc[:, ['Batsman', 'ODI']]
print('\n2)')
print(new_df)

# 3) Display the batsman details who:
# 3.1) scored more than 2000 in ODI
new_df = df.query('ODI > 2000')
print('\n3.1)')
print(new_df)

# 3.2) scored less than 2500 in Test
new_df = df.query('Test < 2500')
print('\n3.2)')
print(new_df)

# 3.3) scored more than 1500 in T20
new_df = df.query('T20 > 1500')
print('\n3.3)')
print(new_df)

# 4) Display the columns using the column index number like 0, 2, and 4
new_df = df.iloc[:, [0,2,4]]
print('\n4)')
print(new_df)

# 5) Display the alternate rows
new_df = df.iloc[::2, :]
print('\n5)')
print(new_df)

# 6) Reindex the dataframe created above with batsman name and delete the data of Hardik Pandya and Shikhar Dhawan by their index from the original dataframe
new_df.index = new_df['Batsman']
new_df = new_df.drop(columns='Batsman')
print('\n6)')
print(new_df)

drop_indices = df.query('Batsman == "Hardik Pandya" or Batsman == "Shikhar Dhawan"').index
new_df = df.drop(index=drop_indices)
print()
print(new_df)

# 7) Insert two rows in the dataframe and delete rows whose index is 1 and 4
to_insert = pd.DataFrame({
    'SNO':     [6, 7],
    'Batsman': ['Rishabh Pant', 'KL Rahul'],
    'Test':    [1500, 1200],
    'ODI':     [1000, 900],
    'T20':     [800, 700]
})
new_df = pd.concat([df, to_insert], ignore_index=True)
new_df.drop(index=[1, 4], inplace=True)
print('\n7)')
print(new_df)

# 8) Delete the column Test, and add one more column "total", ie the total of ODI and T20 runs
new_df          = df.drop(columns='Test')
new_df['total'] = new_df['ODI'] + new_df['T20']
print('\n8)')
print(new_df)

# 9) Rename the column "T20" to "T20I Runs"
new_df = df.rename(columns={'T20': 'T20I Runs'})
print('\n9)')
print(new_df)

# 10) Print the dataframe without headers
print('\n10)')
print(new_df.to_string(header=False, index=False))
```

<br>

## OUTPUT

<br>

1)

| Batsman        |   Test |   T20 |
|:---------------|-------:|------:|
| Virat Kohli    |   3543 |  1925 |
| Ajinkya Rehane |   2578 |  1853 |
| Rohit Sharma   |   2280 |  1522 |
| Shikhar Dhawan |   2158 |  1020 |
| Hardik Pandya  |   1879 |   980 |

2)

| Batsman        |   ODI |
|:---------------|------:|
| Virat Kohli    |  2245 |
| Ajinkya Rehane |  2165 |
| Rohit Sharma   |  2080 |
| Shikhar Dhawan |  1957 |
| Hardik Pandya  |  1856 |

3.1)

|   SNO | Batsman        |   Test |   ODI |   T20 |
|------:|:---------------|-------:|------:|------:|
|     1 | Virat Kohli    |   3543 |  2245 |  1925 |
|     2 | Ajinkya Rehane |   2578 |  2165 |  1853 |
|     3 | Rohit Sharma   |   2280 |  2080 |  1522 |

3.2)

|   SNO | Batsman        |   Test |   ODI |   T20 |
|------:|:---------------|-------:|------:|------:|
|     3 | Rohit Sharma   |   2280 |  2080 |  1522 |
|     4 | Shikhar Dhawan |   2158 |  1957 |  1020 |
|     5 | Hardik Pandya  |   1879 |  1856 |   980 |

3.3)

|   SNO | Batsman        |   Test |   ODI |   T20 |
|------:|:---------------|-------:|------:|------:|
|     1 | Virat Kohli    |   3543 |  2245 |  1925 |
|     2 | Ajinkya Rehane |   2578 |  2165 |  1853 |
|     3 | Rohit Sharma   |   2280 |  2080 |  1522 |

4)

|   SNO |   Test |   T20 |
|------:|-------:|------:|
|     1 |   3543 |  1925 |
|     2 |   2578 |  1853 |
|     3 |   2280 |  1522 |
|     4 |   2158 |  1020 |
|     5 |   1879 |   980 |

5)

|   SNO | Batsman       |   Test |   ODI |   T20 |
|------:|:--------------|-------:|------:|------:|
|     1 | Virat Kohli   |   3543 |  2245 |  1925 |
|     3 | Rohit Sharma  |   2280 |  2080 |  1522 |
|     5 | Hardik Pandya |   1879 |  1856 |   980 |

6)

| Batsman       |   SNO |   Test |   ODI |   T20 |
|:--------------|------:|-------:|------:|------:|
| Virat Kohli   |     1 |   3543 |  2245 |  1925 |
| Rohit Sharma  |     3 |   2280 |  2080 |  1522 |
| Hardik Pandya |     5 |   1879 |  1856 |   980 |


|   SNO | Batsman        |   Test |   ODI |   T20 |
|------:|:---------------|-------:|------:|------:|
|     1 | Virat Kohli    |   3543 |  2245 |  1925 |
|     2 | Ajinkya Rehane |   2578 |  2165 |  1853 |
|     3 | Rohit Sharma   |   2280 |  2080 |  1522 |

7)

|   SNO | Batsman        |   Test |   ODI |   T20 |
|------:|:---------------|-------:|------:|------:|
|     1 | Virat Kohli    |   3543 |  2245 |  1925 |
|     3 | Rohit Sharma   |   2280 |  2080 |  1522 |
|     4 | Shikhar Dhawan |   2158 |  1957 |  1020 |
|     6 | Rishabh Pant   |   1500 |  1000 |   800 |
|     7 | KL Rahul       |   1200 |   900 |   700 |

8)

|   SNO | Batsman        |   ODI |   T20 |   total |
|------:|:---------------|------:|------:|--------:|
|     1 | Virat Kohli    |  2245 |  1925 |    4170 |
|     2 | Ajinkya Rehane |  2165 |  1853 |    4018 |
|     3 | Rohit Sharma   |  2080 |  1522 |    3602 |
|     4 | Shikhar Dhawan |  1957 |  1020 |    2977 |
|     5 | Hardik Pandya  |  1856 |   980 |    2836 |

9)

|   SNO | Batsman        |   Test |   ODI |   T20I Runs |
|------:|:---------------|-------:|------:|------------:|
|     1 | Virat Kohli    |   3543 |  2245 |        1925 |
|     2 | Ajinkya Rehane |   2578 |  2165 |        1853 |
|     3 | Rohit Sharma   |   2280 |  2080 |        1522 |
|     4 | Shikhar Dhawan |   2158 |  1957 |        1020 |
|     5 | Hardik Pandya  |   1879 |  1856 |         980 |

10)
1    Virat Kohli 3543 2245 1925
2 Ajinkya Rehane 2578 2165 1853
3   Rohit Sharma 2280 2080 1522
4 Shikhar Dhawan 2158 1957 1020
5  Hardik Pandya 1879 1856  980



<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q29) Create the following dataframe "Sales" containing year-wise sales figures for five salespersons in INR. Use the years as column labels and the salesperson names as indexes

|             | 2014  |  2015 | 2016  | 2017  |
| ----------- | ----- | ----- | ----- | ----- |
| **Madhu**   | 100.5 | 12000 | 2000  | 50000 |
| **Kusum**   | 150.8 | 18000 | 5000  | 60000 |
| **Kinshuk** | 200.9 | 22000 | 70000 | 70000 |
| **Ankit**   | 30000 | 30000 | 1000  | 80000 |
| **Shruti**  | 40000 | 45000 | 1250  | 90000 |

1) Display the indexes
2) Display the names of the columns
3) Display the dimensions, shape, size, and values
4) Display the last two rows
5) Display the first two columns
6) Change the dataframe Sales such that it becomes its transpose
7) Add data to Sales for the salesman "Sumeet" where the sales made are [196.2, 37800, 52000, 78438] in the years [2014, 2015, 2016, 2017] respectively
8) Delete the data for the the year 2014
9) Update the sale made by Shruti in 2017 to 100000
10) Export the dataframe Sales to a comma separated file "SalesFigures.csv" on the disk. Do not export the indexes or column names
11) Change the name of the salesperson "Ankit" to "Vivaan" and "Kinshuk" to "Shailesh"
12) Delete the data for the salesman "Madhu"

<br>

## CODE

```python
import pandas as pd

data = {
    '2014': [100.5, 150.8, 200.9, 30000, 40000],
    '2015': [12000, 18000, 22000, 30000, 45000],
    '2016': [2000,  5000,  70000, 1000,  1250],
    '2017': [50000, 60000, 70000, 80000, 90000]
}

Sales = pd.DataFrame(
    data,
    index=['Madhu', 'Kusum', 'Kinshuk', 'Ankit', 'Shruti']
)


# 1) Display the indexes
print('\n1)', Sales.index)

# 2) Display the names of the columns
print('\n2)', Sales.columns)

# 3) Display the dimensions, shape, size, and values
print(f'\n3) Dimensions: {Sales.ndim}\nShape: {Sales.shape}\nSize: {Sales.size}\nValues:\n{Sales.values}')

# 4) Display the last two rows
new_df = Sales.tail(2)
print('\n4)')
print(new_df)

# 5) Display the first two columns
new_df = Sales.iloc[:, :2]
print('\n5)')
print(new_df)

# 6) Change the dataframe Sales such that it becomes its transpose
new_df = Sales.T
print('\n6)')
print(new_df)

# 7) Add data to Sales for the salesman "Sumeet" where the sales made are [196.2, 37800, 52000, 78438] in the years [2014, 2015, 2016, 2017] respectively
to_add = pd.DataFrame([[196.2, 37800, 52000, 78438]], columns=Sales.columns, index=['Sumeet'])
new_df = pd.concat([Sales, to_add])
print('\n7)')
print(new_df)

# 8) Delete the data for the year 2014
new_df = Sales.drop(['2014'], axis=1)
print('\n8)')
print(new_df)

# 9) Update the sale made by Shruti in 2017 to 100000
new_df = Sales.copy()
new_df.loc['Shruti', '2017'] = 100000
print('\n9)')
print(new_df)

# 10) Export the dataframe Sales to a comma separated file "SalesFigures.csv" on the disk. Do not export the indexes or column names
Sales.to_csv('SalesFigures.csv', index=False, header=False)
print('\n10) Successfully exported the Sales dataframe to SalesFigures.csv without indexes and column names')

# 11) Change the name of the salesperson "Ankit" to "Vivaan" and "Kinshuk" to "Shailesh"
to_rename = {'Ankit': 'Vivaan', 'Kinshuk': 'Shailesh'}
new_df = Sales.rename(index=to_rename)
print('\n11)')
print(new_df)

# 12) Delete the data for the salesman "Madhu"
new_df = Sales.drop(index='Madhu')
print('\n12)')
print(new_df)
```

<br>

## OUTPUT

<br>

1) Index(['Madhu', 'Kusum', 'Kinshuk', 'Ankit', 'Shruti'], dtype='object')

2) Index(['2014', '2015', '2016', '2017'], dtype='object')

3) Dimensions: 2
Shape: (5, 4)
Size: 20
Values:
[[  100.5 12000.   2000.  50000. ]
 [  150.8 18000.   5000.  60000. ]
 [  200.9 22000.  70000.  70000. ]
 [30000.  30000.   1000.  80000. ]
 [40000.  45000.   1250.  90000. ]]

4)

|        |   2014 |   2015 |   2016 |   2017 |
|:-------|-------:|-------:|-------:|-------:|
| Ankit  |  30000 |  30000 |   1000 |  80000 |
| Shruti |  40000 |  45000 |   1250 |  90000 |

5)

|         |    2014 |   2015 |
|:--------|--------:|-------:|
| Madhu   |   100.5 |  12000 |
| Kusum   |   150.8 |  18000 |
| Kinshuk |   200.9 |  22000 |
| Ankit   | 30000   |  30000 |
| Shruti  | 40000   |  45000 |

6)

|      |   Madhu |   Kusum |   Kinshuk |   Ankit |   Shruti |
|-----:|--------:|--------:|----------:|--------:|---------:|
| 2014 |   100.5 |   150.8 |     200.9 |   30000 |    40000 |
| 2015 | 12000   | 18000   |   22000   |   30000 |    45000 |
| 2016 |  2000   |  5000   |   70000   |    1000 |     1250 |
| 2017 | 50000   | 60000   |   70000   |   80000 |    90000 |

7)

|         |    2014 |   2015 |   2016 |   2017 |
|:--------|--------:|-------:|-------:|-------:|
| Madhu   |   100.5 |  12000 |   2000 |  50000 |
| Kusum   |   150.8 |  18000 |   5000 |  60000 |
| Kinshuk |   200.9 |  22000 |  70000 |  70000 |
| Ankit   | 30000   |  30000 |   1000 |  80000 |
| Shruti  | 40000   |  45000 |   1250 |  90000 |
| Sumeet  |   196.2 |  37800 |  52000 |  78438 |

8)

|         |   2015 |   2016 |   2017 |
|:--------|-------:|-------:|-------:|
| Madhu   |  12000 |   2000 |  50000 |
| Kusum   |  18000 |   5000 |  60000 |
| Kinshuk |  22000 |  70000 |  70000 |
| Ankit   |  30000 |   1000 |  80000 |
| Shruti  |  45000 |   1250 |  90000 |

9)

|         |    2014 |   2015 |   2016 |   2017 |
|:--------|--------:|-------:|-------:|-------:|
| Madhu   |   100.5 |  12000 |   2000 |  50000 |
| Kusum   |   150.8 |  18000 |   5000 |  60000 |
| Kinshuk |   200.9 |  22000 |  70000 |  70000 |
| Ankit   | 30000   |  30000 |   1000 |  80000 |
| Shruti  | 40000   |  45000 |   1250 | 100000 |

10) Successfully exported the Sales dataframe to SalesFigures.csv without indexes and column names

11)

|          |    2014 |   2015 |   2016 |   2017 |
|:---------|--------:|-------:|-------:|-------:|
| Madhu    |   100.5 |  12000 |   2000 |  50000 |
| Kusum    |   150.8 |  18000 |   5000 |  60000 |
| Shailesh |   200.9 |  22000 |  70000 |  70000 |
| Vivaan   | 30000   |  30000 |   1000 |  80000 |
| Shruti   | 40000   |  45000 |   1250 |  90000 |

12)

|         |    2014 |   2015 |   2016 |   2017 |
|:--------|--------:|-------:|-------:|-------:|
| Kusum   |   150.8 |  18000 |   5000 |  60000 |
| Kinshuk |   200.9 |  22000 |  70000 |  70000 |
| Ankit   | 30000   |  30000 |   1000 |  80000 |
| Shruti  | 40000   |  45000 |   1250 |  90000 |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q30) Write code to create the following dataframe "Patient" and write code to perform the following operations:

| PatientID | Treatment_Starts | Drug      | Dosage |
| --------- | ---------------- | --------- | ------ |
| PT1       | 1/14/16          | CISPLATIN | 200    |
| PT20      | 1/2/16           | NIVOLUNAB | 140    |
| PT2       | 1/10/16          | CISPLATIN | 180    |
| PT5       | 1/24/16          | CISPLATIN | 140    |
| PT8       | 2/14/16          | CISPLATIN | 190    |

1) Check for the number of rows in the dataframe
2) Show the datatype of each column
3) Display the first and third column
4) List the number of unique drugs
5) Show the record of the patient with the ID of "PT5" and the "CISPLATIN" drug
6) Display all the rows where the dosage is greater than 180
7) Sort the original dataframe in ascending order of "PatientID" and in descending order of "Treatment_Starts"
8) Show all the drugs and how many patients received those drugs
9) Create a bar chart in seaborn to compare the counts for the two drugs
10) Display the average dosage of each drug

<br>

## CODE

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'PatientID':        ['PT1', 'PT20', 'PT2', 'PT5', 'PT8'],
    'Treatment_Starts': ['1/14/16', '1/2/16', '1/10/16', '1/24/16', '2/14/16'],
    'Drug':             ['CISPLATIN', 'NIVOLUNAB', 'CISPLATIN', 'CISPLATIN', 'CISPLATIN'],
    'Dosage':           [200, 140, 180, 140, 190]
}

Patient = pd.DataFrame(data)


# 1) Check for the number of rows in the dataframe
print(f'\n1) Number of rows in the dataframe: {Patient.shape[0]}')

# 2) Show the datatype of each column
print('\n2)')
print(Patient.dtypes)

# 3) Display the first and third column
new_df = Patient.iloc[:, [0,2]]
print('\n3)')
print(new_df)

# 4) List the number of unique drugs
print(f'\n4) Number of unique drugs: {Patient["Drug"].nunique()}')

# 5) Show the record of the patient with the ID of "PT5" and the "CISPLATIN" drug
new_df = Patient.query('PatientID == "PT5" and Drug == "CISPLATIN"')
print('\n5)')
print(new_df)

# 6) Display all the rows where the dosage is greater than 180
new_df = Patient.query('Dosage > 180')
print('\n6)')
print(new_df)

# 7) Sort the original dataframe in ascending order of "PatientID" and in descending order of "Treatment_Starts"
new_df = Patient.sort_values(by=['PatientID', 'Treatment_Starts'], ascending=[True, False])
print('\n7)')
print(new_df)

# 8) Show all the drugs and how many patients received those drugs
new_df = Patient['Drug'].value_counts()
print('\n8)')
print(new_df)

# 9) Create a bar chart in seaborn to compare the counts for the two drugs
counts = Patient['Drug'].value_counts()
sns.barplot(x=counts.index, y=counts.values)
print('\n9)')
plt.show()

# 10) Display the average dosage of each drug
new_df = Patient.pivot_table(index='Drug', values='Dosage', aggfunc='mean')
print('\n10)')
print(new_df)
```

<br>

## OUTPUT

<br>

1) Number of rows in the dataframe: 5

2)
PatientID           object
Treatment_Starts    object
Drug                object
Dosage               int64
dtype: object

3)

| PatientID   | Drug      |
|:------------|:----------|
| PT1         | CISPLATIN |
| PT20        | NIVOLUNAB |
| PT2         | CISPLATIN |
| PT5         | CISPLATIN |
| PT8         | CISPLATIN |

4) Number of unique drugs: 2

5)

| PatientID   | Treatment_Starts   | Drug      |   Dosage |
|:------------|:-------------------|:----------|---------:|
| PT5         | 1/24/16            | CISPLATIN |      140 |

6)

| PatientID   | Treatment_Starts   | Drug      |   Dosage |
|:------------|:-------------------|:----------|---------:|
| PT1         | 1/14/16            | CISPLATIN |      200 |
| PT8         | 2/14/16            | CISPLATIN |      190 |

7)

| PatientID   | Treatment_Starts   | Drug      |   Dosage |
|:------------|:-------------------|:----------|---------:|
| PT1         | 1/14/16            | CISPLATIN |      200 |
| PT2         | 1/10/16            | CISPLATIN |      180 |
| PT20        | 1/2/16             | NIVOLUNAB |      140 |
| PT5         | 1/24/16            | CISPLATIN |      140 |
| PT8         | 2/14/16            | CISPLATIN |      190 |

8)

| Drug      |   count |
|:----------|--------:|
| CISPLATIN |       4 |
| NIVOLUNAB |       1 |

9)

<center>

<img src="data:image/png;base64,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Xn75ZcXHx/vmLV68WH/6059UUFBQ4+sFcPdxZQRArbIsy+9XLoMGDQr4GOfOndOQIUP89n33MYC6ixgBUKvOnj2rzp07+x43a9bM7+cNGjSQZVl++7ixFfh+IUYA1JqDBw8qOztbjz/+eLljHnjgAV2/fl2FhYW+fVlZWX5jIiIidPz4cb99330MoO7inhEANaKoqEhut1vFxcXKz8/Xvn375HK59OijjyouLq7ceUOHDlXTpk21aNEi/cu//IuOHTvm++ub255++mnNmjVLgwYNUnR0tLZt26aPPvpIDz744F14ZgBqG1dGANSIffv2qU2bNurUqZPGjh2rd999V7/97W+VlpamoKCgcue1bNlSW7Zs0Z49e9SnTx+9+eab+s1vfuM3ZurUqUpISNAvf/lLDRw4UBcuXND06dMVHBx8F54ZgNpms777y1oAqAPGjBmjsLAw/e53vzO9FADVxK9pANzz/u///k/JycmKiYlRUFCQ3nzzTb3zzjtKT083vTQANYArIwDueV9//bUmTJigU6dO6ZtvvlFERISeffZZ/cM//IPppQGoAcQIAAAwihtYAQCAUcQIAAAwihgBAABGESMAAMAoYgQAABhFjAAAAKOIEQAAYBQxAgAAjPp/2KznjpRitAcAAAAASUVORK5CYII=">

</center>


10)

| Drug      |   Dosage |
|:----------|---------:|
| CISPLATIN |    177.5 |
| NIVOLUNAB |    140   |


<div style="page-break-after: always; visibility: hidden">\pagebreak</div>

# Q31) Given a csv file named milknew.csv, write a program to implement a linear regression model to investigate the relationship between the dependent and independent variables present in the dataset. Evaluate the model's performance using two key metrics: the coefficient of determination (R²) and the Mean Squared Error (MSE)

<br>

## CODE

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Load the dataset
df = pd.read_csv('milknew.csv')


# Do ordinal encoding on the "Grade" column
to_replace = {
    'low':    '1',
    'medium': '2',
    'high':   '3'
}
df['Grade'] = df['Grade'].replace(to_replace).astype(int)


# Split the dataset into dependent and independent variables
ATTRS = ['pH', 'Temprature', 'Taste', 'Odor', 'Fat', 'Turbidity', 'Colour']
LABEL = 'Grade'

X = df[ATTRS]
Y = df[LABEL]


# Create the linear regression model
model = LinearRegression()
model.fit(X, Y)

# Print the relationship between the dependent and independent variables
print('\nThe relationship between the dependent and independent variables:')
print('Coefficients:', model.coef_)
print('Intercept:',    model.intercept_)


# Evaluate the model's performance (R^2 and MSE)
r2  = r2_score(Y, model.predict(X))
mse = mean_squared_error(Y, model.predict(X))

print('\nPerformance Metrics:')
print('R²: ', r2)
print('MSE:', mse)
```

<br>

## OUTPUT

<br>

The relationship between the dependent and independent variables:
Coefficients: [ 0.09557826 -0.03288794 -0.11862257  0.28412461  0.37620376 -0.36523753
 -0.00471413]
Intercept: 3.7134139858866346

Performance Metrics:
R²:  0.2768402608210946
MSE: 0.4484672271421274

