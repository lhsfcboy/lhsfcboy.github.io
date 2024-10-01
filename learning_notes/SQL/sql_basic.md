https://github.com/baagod/sql_node/blob/master/mysql/MySQL%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0.md

https://github.com/C10H16/MySQL-notes/blob/master/1-MySQL%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C.md

https://gist.github.com/Chryzanthemum/29cc9a6a69900d044562d54bf31df321


```sql
SELECT TOP 3 * FROM Customers;
SELECT TOP 50 PERCENT * FROM Customers;
```
### 数据库的表和字段命名

小写。标识符应该全部用小写字母来书写，使用first_name，不是"First_Name"或者"FirstName"。

数据类型不是名称。避免使用仅为数据类型的名字（如text或timestamp）。

强调单独的单词。由多个单词组成的对象名称应该用下划线分隔，例如使用word_count或team_member_id，而不是wordcount或wordCount。

完整的单词，而不是缩写。例如使用middle_name，不是mid_nm。

使用常用缩写。对于几个长词而言，缩写词比词本身更为常见，比如i18n和l10n，这时使用缩写。
