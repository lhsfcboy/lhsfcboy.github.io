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
任务背景：我正在为同事和上司撰写对他们的feedback，我将给出我的大致想法和印象，请给出对应的输出
你的角色：熟悉商务英语的写作, 在欧美企业工作多年
现有情况：
注意事项：
已知条件：
输出样式：两篇英语短文, 字数在50左右， 第一篇内容为`Strengths`, 第二篇内容为`Areas of Development`
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
https://yesaiwen.com/chatgpt-best-practice-prompts/

尚未找到等同的中文提示词。可以尝试如下:
```
结果以Markdown格式返回,整体的返回包括在一个代码块之中
```

最简单的解决办法: 使用复制答案功能把返回复制到Markdown编辑器中

## 官方的提示词指南

- https://yesaiwen.com/chatgpt-best-practice-prompts/
