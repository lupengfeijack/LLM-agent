from http.client import responses
import gradio as gr
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


def gradio_chat_interface(user_input, chat_history):
    # 调用聊天函数
    bot_response = chat(user_input)

    # 更新聊天历史
    chat_history.append((user_input, bot_response))

    # 返回更新后的聊天历史
    return "", chat_history


# 创建Gradio界面
with gr.Blocks() as demo:
    # 标题
    gr.Markdown("# 我的聊天机器人")

    # 聊天记录显示区域
    chatbot = gr.Chatbot(label="聊天记录")

    # 用户输入框
    user_input = gr.Textbox(label="输入你的消息")

    # 发送按钮
    send_button = gr.Button("发送")

    # 清空按钮
    clear_button = gr.Button("清空")

    # 绑定发送按钮事件
    send_button.click(
        fn=gradio_chat_interface,  # 触发的函数
        inputs=[user_input, chatbot],  # 输入组件
        outputs=[user_input, chatbot]  # 输出组件
    )

    # 绑定清空按钮事件
    clear_button.click(
        fn=lambda: [],  # 清空聊天记录
        inputs=None,
        outputs=chatbot
    )

# 启动Gradio应用
demo.launch(share=True)