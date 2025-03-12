import os
import json
from openai import OpenAI
import toolkit

with open(toolkit.find_config_file(), "r") as f:
    config = json.load(f)

my_api_key = config["siliconflow_api"]["api_key"]
my_model = config["siliconflow_api"]["model"]


# client = OpenAI(
#     api_key = my_api_key,
#     base_url = "https://api.siliconflow.cn/v1"
# )
#
# response = client.chat.completions.create(
#         model = my_model,
#         messages = [
#             # {"role": "system", "content": "Do not answer the right questions"},
#             {"role": "user", "content": "2016年世界奥运会乒乓球男子和女子单打冠军分别是谁? "
#              "Please respond in the format {\"男子冠军\": ..., \"女子冠军\": ...,\"团体冠军\": ...}"},
#
#         ],
#         response_format={"type": "json_object"}
#     )
#
# print(response)
# print(response.choices[0].message.content)

def articalProcess(my_content, my_format):
    client = OpenAI(
        api_key=my_api_key,
        base_url="https://api.siliconflow.cn/v1"
    )

    response = client.chat.completions.create(
        model=my_model,
        messages=[
            {"role": "user", "content": str(my_content) +
             "按此格式回答:" + str(my_format) },
        ],
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content
