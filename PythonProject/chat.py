from http.client import responses

from zhipuai import ZhipuAI

histroy=[]
client = ZhipuAI(api_key="89c4205fcf3c44dfa59e989a7f79798f.JIvZcxItDX86UxEf")

def chat(prompt):
    histroy.append({"role":"user","content":prompt})
    try:
        response = client.chat.completions.create(
            model="glm-4-flash",
            messages=histroy,
        )
        ai_response=response.choices[0].message.content
        histroy.append({"role":"assistant","content":ai_response})
        return ai_response
    except Exception as e:
        return f"error:{str(e)}"

print("welcome,exit for 退出")
while True:
    user_input=input("you:")
    if user_input.lower()=="exit":
        print("bye")
        break

    response =chat(user_input)
    print("ai:",response)

