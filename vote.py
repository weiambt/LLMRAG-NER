# 多句子+投票机制,可以直接根据结果文件计算
import json

from LLM import LLMFactory

class Vote:
    def __init__(self,logger):
        self.logger = logger
        self.model_name = 'Qwen'
        self.document_path = './data/dev.txt'

    def process_single(mp):
        text = mp["text"]
        labels = mp["label"]
        qwen = mp["res_Qwen"]
        res = {}

        # 多个模型投票
        LLMFactory.call("Qwen", system_prompt, user_prompt, self.logger)

        # 选择最优模型结果作为最终结果,保存到文件中,并返回
        return {"res_final":"","res_select":""}


    def process_muti(self,input_file):
        with open(input_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                mp = json.loads(line)
                res = self.process_single(mp)
                # 计算评价指标