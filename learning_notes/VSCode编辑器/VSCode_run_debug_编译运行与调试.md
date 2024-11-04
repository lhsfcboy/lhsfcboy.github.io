## 单个文件的编译运行与调试

对于如下的单个C语言文件, `main.c`
```c
#include <stdio.h>
int main()
{
    int sum = 0;
    for (int i = 1; i <= 10; i++)
    {
        sum += i;
        printf("加上 %d 后,当前和为: %d\n", i, sum);
    }
    printf("最终结果: %d\n", sum);
    return 0;
}
```

- 使用命令行
  `gcc -Wall -Wextra -std=c99 -o main main.c`
- 使用`make`命令, 对应的`Makefile`示例如下

```make
all: clean main run

main: main.c
	gcc -Wall -Wextra -std=c99 -o main main.c

run: main
	./main

clean:
	rm -f sum_program

.PHONY: all run clean
```



## 多个文件的编译运行

这里推荐借助`make`命令实现

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Make",
      "type": "shell",
      "command": "make",
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "problemMatcher": [],
      "detail": "Runs the Make command to build the project."
    }
  ]
}
```
