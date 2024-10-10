# ChatGPT 使用技巧

一些能够提高ChatGPT效果的提示词

## ChatGPT Plus的使用限制
- o1-preview 50 msg per week (refresh on Wednesay?)
- o1-mini    50 msg per day
- GPT-4      40 msg per 3 hours
- GPT-4o     80 msg per 3 hours

From: https://openai.com/chatgpt/pricing/
> As of May 13th 2024, Plus users will be able to send 80 messages every 3 hours on GPT-4o. 
> and 40 messages every 3 hours on GPT-4. 
> GPT-4o mini does not have limits on the Plus tier.
> Plus user have access to 50 messages a week with OpenAI o1-preview and 50 messages a day with OpenAI o1-mini to start with our research preview.

## 使用`Shift + Enter`在输入框中输入多行提示词

## 提示词应该有一定的结构化

例如参照Markdown格式的一种实现
```markdown
任务背景：
你的角色：
现有情况：
注意事项：
已知条件：
输出样式：
```

## Chain of Thought 展示思考过程

> Let's work this out in a step by step way to be sure we have the right answer.

- [TODO] 是否有效果完全一致的中文版呢?

## 输出Markdown格式

在输出markdown格式的回答，而回答内容本身包含连续三个单引号时，ChatGPT的Web页面会错误的进行渲染。

目前找到的解决方案是，额外给出一个提示词：
```
Enclose it to avoid render it in browser (Plain Text Format)
```

尚未找到等同的中文提示词。

方案来自：https://community.openai.com/t/chatgpt-output-as-markdown/501444/15

