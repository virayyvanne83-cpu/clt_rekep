from openai import OpenAI

# 填入你的中转 URL 和 Key
client = OpenAI(
    base_url="https://api.openai-proxy.org/v1",
    api_key="sk-oXkh8s67VHw7JvcIOKimNjG6s0Di7wtzPYWax6GjE1GouLl6" # 请替换为您最新的Key
)

try:
    print("正在连接测试...")
    response = client.chat.completions.create(
        model="gpt-4o", # 测试用个便宜的模型即可
        messages=[{"role": "user", "content": "你好，请回复我123"}]
    )
    print("调用成功！回复内容：", response.choices[0].message.content)
except Exception as e:
    print("调用失败！错误信息：\n", e)