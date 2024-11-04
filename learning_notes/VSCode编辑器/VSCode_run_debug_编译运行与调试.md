




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
