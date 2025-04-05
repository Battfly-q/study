# agent_framework.py

import random
from typing import List, Dict, Any

class Memory:
    def __init__(self):
        self.logs = []

    def add(self, entry: str):
        self.logs.append(entry)

    def get_recent(self, n=5):
        return self.logs[-n:]

class Tool:
    def __init__(self, name: str, func, description: str):
        self.name = name
        self.func = func
        self.description = description

    def run(self, *args, **kwargs):
        return self.func(*args, **kwargs)

class Toolset:
    def __init__(self):
        self.tools: Dict[str, Tool] = {}

    def register(self, tool: Tool):
        self.tools[tool.name] = tool

    def get_tool(self, name: str):
        return self.tools.get(name, None)

    def list_tools(self):
        return list(self.tools.keys())

class LLMInterface:
    def __init__(self):
        pass

    def chat(self, prompt: str, context: List[str] = None) -> str:
        # 🔧 替换为实际 LLM API 调用，比如 OpenAI
        response = f"模拟 LLM 回复: {prompt[:50]}..."
        return response

class Agent:
    def __init__(self):
        self.memory = Memory()
        self.tools = Toolset()
        self.llm = LLMInterface()

    def think(self, goal: str):
        context = self.memory.get_recent()
        prompt = f"目标: {goal}\n上下文: {context}\n该做什么？"
        plan = self.llm.chat(prompt, context)
        self.memory.add(f"计划: {plan}")
        return plan

    def act(self, plan: str):
        # 简单解析调用工具的指令，如 "使用 calculator 工具计算 3+2"
        if "calculator" in plan:
            tool = self.tools.get_tool("calculator")
            if tool:
                result = tool.run("3+2")
                self.memory.add(f"执行结果: {result}")
                return result
        return "未识别的行动"

    def run(self, goal: str):
        print(f"🎯 接收到目标: {goal}")
        plan = self.think(goal)
        result = self.act(plan)
        print(f"✅ 最终输出: {result}")

# 示例工具函数
def simple_calculator(expr: str) -> str:
    try:
        return str(eval(expr))
    except Exception as e:
        return f"错误: {str(e)}"

# 示例运行
if __name__ == "__main__":
    agent = Agent()
    agent.tools.register(Tool(name="calculator", func=simple_calculator, description="计算数学表达式"))
    agent.run("帮我计算 3+2 是多少")
