# SQL 操作速查手册

增删改查

## INSERT

```sql
-- Insert with duplicate key
REPLACE INTO tbl VALUES(1,50);
INSERT IGNORE INTO tbl VALUES (1,10);
```