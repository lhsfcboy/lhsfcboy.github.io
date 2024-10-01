# Pandas 备忘录

## 数据清洗

- 填充缺失值

```python
df.fillna(0)
df.fillna(method='ffill') # 照抄前一个
df.fillna(method='bfill')
df.fillna(df.mean())      # 以当列的平均值填充
```

- 除重, 处理重复数据

```python
dupli_data.drop_duplicates()
```

- 数据离散化

```python
birth_year_bins = [1980,1985,1990,1995,2000]
group_names = ["first1980", "second1980", "first1990", "second1990"]
birth_year_cut_data = pd.cut(birth_year,birth_year_bins, labels=group_names)

pd.value_counts(birth_year_cut_data)

pd.cut(birth_year,2) # 均匀的自动分割
```