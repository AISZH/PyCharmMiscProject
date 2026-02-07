from openai import OpenAI
import os
# 推荐通过环境变量存储 API Key，避免明文泄露
# 你可以先在终端设置环境变量（Windows：set OPENROUTER_API_KEY=你的密钥；Mac/Linux：export OPENROUTER_API_KEY=你的密钥）
# 也可以直接在代码中临时设置（仅用于测试，正式环境优先终端/配置文件设置）
os.environ["OPENROUTER_API_KEY"] = "sk-qzzobmekpemzsbxutwnzsnoqapsmakiuepblgyvgckogntkv"

def get_criticism_response():
    try:
        # 初始化客户端
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")  # 从环境变量获取密钥
        )

        # 发起聊天补全请求
        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",
            messages=[
                {
                    "role": "user",
                    "content": "what can I do if criticism is too harsh?"
                }
            ],
            temperature=0.7,  # 随机性最低，输出更稳定(0,1)
            max_tokens=1024,  # 最大生成token数
            # 以下为默认值，可省略
            # top_p=1.0,
            # frequency_penalty=0,
            # presence_penalty=0,
        )

        # 返回模型回复内容
        return completion.choices[0].message.content

    except Exception as e:
        # 捕获所有异常并返回错误信息
        return f"请求失败：{str(e)}"

# 调用函数并打印结果
if __name__ == "__main__":
    response = get_criticism_response()
    print("模型回复：")
    print(response)