# 年月日到星期日的计算

```c
int dayOfWeek(int y, int m, int d) {
    static int t[] = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4};
    y -= m < 3;
    return (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7;
}
```

## 阅读并试图分析其含义

## 添加测试用例, 并添加输入检查

## 扩展到1582年10月15日之前的使用

## 参考
```c
#include <stdio.h>

// 计算某日期是星期几
int dayOfWeek(int y, int m, int d) {
    static int t[] = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4};
    y -= m < 3;
    return (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7;
}

int main() {
    int year, month, day;
    char *weekday[] = {"Sunday", "Monday", "Tuesday", "Wednesday",
                       "Thursday", "Friday", "Saturday"};
    
    printf("Please input date (year month day): ");
    scanf("%d %d %d", &year, &month, &day);
    
    if(month < 1 || month > 12) {
        printf("Invalid month!\n");
        return 1;
    }
    
    if(day < 1 || day > 31) {
        printf("Invalid day!\n");
        return 1;
    }
    
    int w = dayOfWeek(year, month, day);
    printf("%d-%d-%d is %s\n", year, month, day, weekday[w]);
    
    return 0;
}
```