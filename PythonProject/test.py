from zhipuai import ZhipuAI

client=ZhipuAI(api_key="89c4205fcf3c44dfa59e989a7f79798f.JIvZcxItDX86UxEf")
histroy=[]
def chat(prompt):
    try:
        histroy.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(
            model="glm-4-flash",
            messages=histroy,
        )
        ai_response = response.choices[0].message.content
        histroy.append({"role": "assistant", "content": prompt})
        return ai_response
    except Exception as e:
        return f"error:{str(e)}"


print("welcome,exit:退出")
while True:
    user_input=input("you:")
    if user_input.lower()=="exit":
        print("bye")
        break
    response=chat(user_input)
    print("ai:",response)


