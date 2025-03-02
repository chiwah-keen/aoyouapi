from src.conf import conf
from src.services.chat import chat_robots


def ask(question):
    if not conf.CHAT_SERVERS:
        raise Exception('聊天对象不存在！！！')
    # TODO 后续可以添加选择的机器人
    return chat_robots.ask_deepseek_with_deepseekchat(question)