import json

from openai import OpenAI, api_key

import utils.readconfig
import utils.logger


class LLMClient:
    def __init__(self,logger,conf):
        self.logger = logger
        self.api_params = utils.readconfig.load_multiple_objects_config(conf)

    def execute(self,model_name,system_prompt,user_prompt):
        model_config = self.get_model_config(model_name)

        client = OpenAI(
            api_key = model_config["api_key"],
            base_url = model_config["base_url"],
        )

        completion = client.chat.completions.create(
            model = model_config["model"],
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt},
            ],
        )
        data = completion.choices[0].message.content
        self.logger.info('==user_prompt:{}'.format(user_prompt))
        self.logger.info('==result:{}'.format(data)) # 输出的是json_str

        # res = completion.model_dump_json()
        # json_res = json.loads(res)
        # # print(json_res)
        # # print(json_res["choices"][0]["message"]["content"])
        # data = json_res["choices"][0]["message"]["content"]
        # self.logger.info('==user_prompt:{}'.format(user_prompt))
        # self.logger.info('==result:{}'.format(data)) # 输出的是json_str
        return data

    def get_model_config(self,model_name):
        model_config = {}
        if model_name == "qwen":
            model_config = self.api_params[model_name]
            model_config["model"] = "qwen-turbo"
        elif model_name == "chatgpt":
            model_config = self.api_params[model_name]
            model_config["model"] = "gpt-3.5-turbo"
        elif model_name == "baichuan":
            model_config = self.api_params[model_name]
            model_config["model"] = "Baichuan2-Turbo"
        elif model_name == "deepseek":
            model_config = self.api_params[model_name]
            model_config["model"] = "deepseek-r1"
        else:
            self.logger.error("unknown model name: {}".format(model_name))
        return model_config

if __name__ == '__main__':
    logger = utils.logger.get_logger("log")
    client = LLMClient(logger,"conf/online/llm.ini")
    client.execute("qwen", "你是一个回答者", "介绍下自己")
    # res = client.execute("chatgpt", "", "介绍下自己")
    client.execute("baichuan", "你是一个回答者", "介绍下自己")
    client.execute("deepseek", "你是一个回答者", "介绍下自己")

    # res = LLMFactory.call("Qwen","","介绍下自己",logger)

    # res = LLMFactory.call("ChatGPT","","介绍下自己",logger)
    # res = LLMFactory.call("Baichuan","你是个回答助手","介绍下自己",logger)
    # print(res)
