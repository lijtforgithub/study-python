from openai import OpenAI
from ai.config import GlobalConfig

client = OpenAI(
    base_url=GlobalConfig.TY_URL,
    api_key=GlobalConfig.TY_KEY,
)

completion = client.chat.completions.create(
    model=GlobalConfig.TY_MODEL,
    messages=[
        {"role": "system", "content": "你是一个职能助手"},
        {"role": "user", "content": "你是Qwen3吗"},
    ],
    # Qwen3模型通过enable_thinking参数控制思考过程（开源版默认True，商业版默认False）
    # 使用Qwen3开源版模型时，若未启用流式输出，请将下行取消注释，否则会报错
    # extra_body={"enable_thinking": False},
)
print(completion.model_dump_json())
