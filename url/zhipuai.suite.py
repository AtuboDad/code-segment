# pip install zhipuai 请先在终端进行安装

from zhipuai import ZhipuAI


client = ZhipuAI(api_key="your api key")

question = '桥梁总长度是多少?'
response = client.chat.completions.create(
    model="glm-4",
    messages=[
        {
            "role": "user",
            "content": "从文档\n\"\"\"\n有一座桥梁分为10段，第一段100米，第二段200米，第三段200米，第四段200米，第五段200米，第六段200米，第七段200米，第八段200米，第九段200米，第十段200米。\n\n\"\"\"\n中找问题\n\"\"\"\n" + question + "\n\"\"\"\n的答案，找到答案就仅使用文档语句回答问题，找不到答案就用自身知识回答并且告诉用户该信息不是来自文档。\n\n不要复述问题，直接开始回答。"
        }
    ],
    top_p=0.7,
    temperature=0.95,
    max_tokens=1024,
    stream=True,
)


resp = []
for trunk in response:
    resp.append(trunk.choices[0].delta.content)

print(''.join(resp))