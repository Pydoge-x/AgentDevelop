# 基础模型
import asyncio

from dotenv import load_dotenv

load_dotenv(override=True)
from langchain.chat_models import init_chat_model
import os
import time
from rich import print as rprint

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")

model = init_chat_model(
    model="openai:deepseek-flash",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
)

# 异步调用batch
async def batch_command():
    # 记录开始时间
    start_time = time.perf_counter()
    print("==========程序开始===========")
    # 创建异步任务,发起异步请求
    abatch_resp = asyncio.create_task(model.abatch(["三句话介绍一下什么是Python","一句话讲一下什么是人工智能","一句话告诉我C语言是什么"])
)
    print("已经创建协程，可以同时进行其他任务")
    for i in range(5):
        await asyncio.sleep(1)
        print(f"正在执行第{i + 1}个任务，已耗时:{time.perf_counter() - start_time}")

        # 开始处理返回的结果
    print("模拟结束")
    model_resp = await abatch_resp
    rprint(model_resp)
    end_time = time.perf_counter()
    print(f"\n总计用时{end_time - start_time}")

asyncio.run(batch_command())