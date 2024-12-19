# 数据分析

## 数据分析常用包的导入

```python
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

######################################
# %load ../../standard_import.txt
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from scipy.optimize import minimize
from sklearn.preprocessing import PolynomialFeatures

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 150)
pd.set_option('display.max_seq_items', None)

# %config InlineBackend.figure_formats = {'pdf',}
%matplotlib inline

import seaborn as sns
sns.set_context('notebook')
sns.set_style('white')
###################################
```

### numpy

- 生成在 $start \sim stop$ 区间内按 $step$ 间隔的数据：
  ```python
  np.arange([start], stop, [step], [dtype])
  ```
- 生成在 $start \sim stop$ 区间内均分的 $num$ 个数据：
  ```python
  np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
  ```
- 生成在 $start \sim stop$ 区间内均分的对数数据：
  ```python
  np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
  ```
- 生成用零初始化的 numpy array：
  ```python
  np.zeros(shape, dtype=float, order='C')
  ```
- 生成用一初始化的 numpy array：
  ```python
  np.ones(shape, dtype=None, order='C')
  ```
- 基于现有 numpy array 的尺寸创建零或一的 numpy array：
  ```python
  np.zeros_like(a, dtype=None, order='K', subok=True)
  np.ones_like(a, dtype=None, order='K', subok=True)
  ```

### pandas

- 返回数值而不是 `Series`：
  ```python
  df[df.Letters == 'C'].Letters.item()
  df.loc[df['Letters'] == 'C', 'Letters'].values[0]
  ```
- 混合使用行数+列名/行名+列数：
  ```python
  df.loc[df.index[[0, 2]], 'A']
  df.iloc[[0, 2], df.columns.get_loc('A')]
  ```
- 创建一个零填充的 pandas DataFrame：
  ```python
  d = pd.DataFrame(0, index=np.arange(5), columns=['A', 'B'])
  ```
- 添加时序作为索引：
  ```python
  df.index = pd.date_range(startdate, periods=df.shape[0])
  ```
- 创建带有列名的新 DataFrame：
  ```python
  df = pd.DataFrame(columns=['A', 'B', 'C', 'D', 'E', 'F', 'G'])
  pd.DataFrame(columns=['A', 'B'])
  pd.DataFrame({}, columns=['A', 'B'])
  pd.DataFrame(None, columns=['A', 'B'])
  ```
- 选择每隔 $n$ 行或 $n$ 列：
  ```python
  df1 = df[df.index % 3 != 0]
  df.iloc[1::5, :]
  df[df.columns[::2]]
  df.ix[:, 1::2]
  ```
- 将列表或 `Series` 追加到 DataFrame：
  ```python
  list = [['a', 'b']]
  list.append(['e', 'f'])
  df = pd.DataFrame(list, columns=['col1', 'col2'])

  list = [['f', 'g']]
  df = df.append(pd.DataFrame(list, columns=['col1', 'col2']), ignore_index=True)
  ```

### sklearn

- 加载 IRIS（鸢尾花）数据集：
  ```python
  from sklearn.datasets import load_iris
  ```
- 数据预处理：
  - 填充空值：
    ```python
    fare_mode = test["fare"].mode()[0]
    test.loc[test["fare"].isnull(), "fare"] = fare_mode
    ```
  - 计算缺失值：
    ```python
    from numpy import vstack, array, nan
    from sklearn.preprocessing import Imputer

    Imputer().fit_transform(vstack((array([nan, nan, nan, nan]), iris.data)))
    ```
  - 数据标准化：
    ```python
    from sklearn.preprocessing import StandardScaler
    StandardScaler().fit_transform(iris.data)
    ```
  - 数据归一化：
    ```python
    from sklearn.preprocessing import Normalizer
    Normalizer().fit_transform(iris.data)
    ```
  - 特征二值化：
    ```python
    from sklearn.preprocessing import Binarizer
    Binarizer(threshold=3).fit_transform(iris.data)
    ```
  - 特征哑编码：
    ```python
    from sklearn.preprocessing import OneHotEncoder
    OneHotEncoder().fit_transform(iris.target.reshape((-1, 1)))
    ```
