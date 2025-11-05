# SQL 学习

## 教程

https://www.w3schools.com/sql/default.asp

https://github.com/baagod/sql_node/blob/master/mysql/MySQL%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md

https://github.com/C10H16/MySQL-notes/blob/master/1-MySQL%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C.md

https://gist.github.com/Chryzanthemum/29cc9a6a69900d044562d54bf31df321


```sql
SELECT TOP 3 * FROM Customers;
SELECT TOP 50 PERCENT * FROM Customers;
```

## 常见的数据库

- MySQL
- PostgreSQL
 - PostgreSQL 开发者把它念作post-gress-Q-L。PostgreSQL 的 Slogan 是 "世界上最先进的开源关系型数据库"
 - 严格支持SQL语言
- [Oracle Database Express Edition](http://www.oracle.com/technetwork/database/database-technologies/express-edition/overview/index.html)
- Microsoft SQL Server
- Sybase SQL Server
  - 现在归属德国SAP公司
- SQLite3
  - 单机/测试/学习

### 数据库的表和字段命名

小写。标识符应该全部用小写字母来书写，使用first_name，不是"First_Name"或者"FirstName"。

数据类型不是名称。避免使用仅为数据类型的名字（如text或timestamp）。

强调单独的单词。由多个单词组成的对象名称应该用下划线分隔，例如使用word_count或team_member_id，而不是wordcount或wordCount。

完整的单词，而不是缩写。例如使用middle_name，不是mid_nm。

使用常用缩写。对于几个长词而言，缩写词比词本身更为常见，比如i18n和l10n，这时使用缩写。


## SQL语句执行顺序

SELECT语句的基本语法如下：

 ```sql
SELECT selection_list # What columns to select 从过滤的分组结果中选择列的子集。这也是𝗪𝗜𝗡𝗗𝗢𝗪 𝗳𝘂𝗻𝗰𝘁𝗶𝗼𝗻 𝗮𝗴𝗴𝗿𝗲𝗴𝗮𝘁𝗶𝗼𝗻𝘀发生的地方
FROM table_list       # Which tables to select rows from  𝗙𝗥𝗢𝗠 𝗮𝗻𝗱 𝗝𝗢𝗜𝗡 确定感兴趣的基础数据。
WHERE primary_constraint # What conditions rows must satisfy 过滤感兴趣的基础数据，仅保留满足where子句的数据
GROUP BY grouping_columns # How to group results 按特定列或多列对过滤后的数据进行分组。组用于计算所选列的聚合
HAVING secondary_constraint # Secondary conditions rows must satisfy 通过对我们分组所依据的列定义约束来再次过滤数据
ORDER BY sorting_columns # How to sort results 按一列或多列对结果进行排序
LIMIT from, count; # Limiting row count on results 仅保留排序结果中的前 n 行
```

![image](https://github.com/user-attachments/assets/d7e5d7bc-cd92-470b-8eda-454353b5d2ff)

1. FROM:对FROM子句中的前两个表执行笛卡尔积，生成虚拟表VT1。
from子句组装来自不同数据源的数据

3. ON:对VT1应用ON筛选器。只有那些使<join_condition>为真的行才被插入VT2。
 
4. OUTER(JOIN):如果指定了OUTER JOIN，保留表中未找到匹配的行将作为外部行添加到VT2，生成VT3。
如果FROM子句包含两个以上的表，则对上一个联接生成的结果表和下一个表重复执行步骤1到步骤3，直到处理完所有的表为止。

5. 对VT3应用WHERE筛选器。只有使<where_condition>为TRUE的行才被插入VT4。
where子句基于指定的条件对记录行进行筛选

6. GROUP BY:按GROUP BY 子句中的列列表对VT4中的行分组，生成VT5。
group by子句将数据划分为多个分组

7. CUBE|ROLLUP:把超组插入VT5，生成VT6。
使用聚集函数进行计算

8. HAVING:对VT6应用HAVING筛选器。只有使<having_condition>为TRUE的组才会被插入VT7。
使用having子句筛选分组

9. SELECT:处理SELECT列表，产生VT8。
 
10. DISTINCT:将重复的行从VT8中移除，产生VT9。
 
11. ORDER BY:将VT9中的行按ORDER BY子句中的列列表排序，生成一个有表(VC10)。
使用order by对结果集进行排序

12. TOP:从VC10的开始处选择指定数量或比例的行，生成表VT11,并返回给调用者。
