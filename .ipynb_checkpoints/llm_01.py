import os
from openai import OpenAI

# 把 API Key 放到环境变量最安全，也可以直接写字符串
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. 用一句话描述任务 → 这就是零样本的核心
task_prompt = """
请判断以下影评的情感倾向，直接返回“正面”或“负面”，不要解释：
“这部电影剧情拖沓，演员表演也很尴尬。”
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",   # 也可换成 "gpt-4"
    messages=[
        {"role": "user", "content": task_prompt}
    ],
    temperature=0            # 温度越低越确定
)

print(response.choices[0].message.content.strip())
# 期望输出：负面