# 基础模型
import asyncio
from dotenv import load_dotenv

load_dotenv(override=True)
from langchain.chat_models import init_chat_model
import os
import time

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")

model = init_chat_model(
    model="openai:deepseek-flash",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL,
)


# 异步调用invoke
async def invoke_command():
    # 记录开始时间
    start_time = time.perf_counter()
    print("==========程序开始===========")
    # 创建异步任务,发起异步请求
    model_task = asyncio.create_task(model.ainvoke(
        "介绍一下什么是人工智能"))  # ainvoke是一个异步函数，调用它只会创建一个协程对象，并不会立刻执行里面的请求逻辑。因此需要使用asyncio.create_task创建一个异步任务，才能够执行。
    print("已经创建协程，可以同时进行其他任务")
    # 在等待请求返回的过程中，程序进行其他
    for i in range(3):
        await asyncio.sleep(1)
        print(f"正在执行第{i + 1}个任务，已耗时:{time.perf_counter() - start_time}")

    # 开始处理返回的结果
    print("模拟结束")
    model_resp = await model_task
    end_time = time.perf_counter()
    print(model_resp.content)
    print(f"总计用时{end_time - start_time}")
    # 由于网络延迟等情况，调用大模型返回结果的时间可能会超过3秒，因此，可能会存在最终总计用时大于3的情况，并不是错误，而是正常的，因为对于异步程序来说，最终的运行时间由最长的那个决定，而不是相加或者最短的决定。

asyncio.run(invoke_command())
