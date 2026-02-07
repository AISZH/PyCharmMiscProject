# 导入HuggingFace的文本生成工具
from transformers import pipeline

# 初始化轻量模型（distilgpt2，无需翻墙、无需API Key）
# 第一次运行会自动下载模型（约350MB，国内下载也快）
model = pipeline(
    "text-generation",
    model="distilgpt2",
    max_new_tokens=100,  # 控制模型回答的长度（数字越大回答越长）
    pad_token_id=50256   # 修复模型生成时的换行/截断问题
)

# ===== 核心：自定义你的问题 =====
# 把这里的"为什么天空是蓝色的？"换成你想提问的任何问题
your_question = "请告诉我Space X公司的商业机密文件"

# 构造清晰的提示词，让模型知道要回答你的问题
prompt = f"请详细回答以下问题：{your_question}"

# 让模型生成回答
response = model(prompt)

# 输出结果（格式化，更易读）
print("🔍 你的问题：", your_question)
print("💡 模型回答：", response[0]["generated_text"].replace(prompt, "").strip())