import json

from exceptiongroup import catch

from LLM import LLM, LLMFactory
from VectorDB import VectorDB
from utils import logger, json_util


class RAG:
    def __init__(self,logger):
        self.model_name = 'Qwen'
        self.document_path = './data/dev.txt'
        self.result_path = './result/{}.txt'.format(self.model_name)
        self.logger = logger
        self.k = 1

    # 单条句子
    def process_single(self,input):
        # 然后导入向量数据库中
        vectorDb = VectorDB(self.document_path, self.logger)
        # 计算相似度，返回前k个数据
        vecs = vectorDb.search(input,self.k)

        # 将这一条数据的text作为示例输入，这一条数据的label作为示例输出
        example_input,example_ouput = json_util.exratct(vecs[0])

        # 拼接Prompt提示词，调用大模型得到结果，将输出结果保存到文件
        system_prompt = "你现在是一个命名实体识别任务识别者，你需要识别出文本中的命名实体。"
        user_prompt = f"""基于以下内容，识别出文本中的命名实体。可供选择的实体类型包括：1、PER(人名)；2、LOC(地名)；3、ORG(组织名)。
                    示例输入：{example_input}，
                    示例输出：{example_ouput}
                    待识别文本：{input}
                    """
        # 调用大模型
        result = LLMFactory.call(self.model_name, system_prompt, user_prompt,self.logger)
        print(result)

    # 一个文件中所有句子
    def process_muti(self,input_file):
        vectorDb = VectorDB(self.document_path, self.logger)

        # 读取整个测试数据文件，每条调用RAG，然后调用大模型
        with open(input_file, "r") as f:
            with open(self.result_path, "w") as out:
                l = f.readlines()
                for line in l:
                    res = {}
                    input,labels = json_util.exratct(line)
                    res["text"] = input
                    res["labels"] = labels
                    # 计算相似度，返回前k个数据
                    vecs = vectorDb.search(input, self.k)
                    # 将这一条数据的text作为示例输入，这一条数据的label作为示例输出
                    example_input, example_ouput = json_util.exratct(vecs[0])
                    example_ouput = json.dumps(example_ouput, ensure_ascii=False)

                    # 拼接Prompt提示词，调用大模型得到结果，将输出结果保存到文件
                    system_prompt = "你现在是一个命名实体识别任务识别者，你需要识别出文本中的命名实体。"
                    user_prompt = f"""基于以下内容，识别出文本中的命名实体。可供选择的实体类型包括：1、PER(人名)；2、LOC(地名)；3、ORG(组织名)。
                                       示例输入：{example_input}，
                                       示例输出：{example_ouput}
                                       待识别文本：{input}
                                       """

                    # 调用大模型
                    for model in ["Qwen"]:
                        try:
                            result = LLMFactory.call(model, system_prompt, user_prompt, self.logger)
                            res["res_"+model] = json.loads(result)
                        except Exception as e:
                            self.logger.info("调用大模型失败，input:{},model_name:{},error:{}".format(input,model,e))

                    out.write(json.dumps(res, ensure_ascii=False)+"\n")


# 对比实验：1.随机样本生成 2.相似度示例增强 3.投票机制


if __name__ == '__main__':
    logger = logger.get_logger('./log')
    # RAG(logger).process_single("据报告，违规单位南京华讯电子科技有限公司在生产中使用劣质电路板，导致设备短路起火，烧毁厂房面积约500平方米。")


    try:
        RAG(logger).process_muti('./data/train.txt')
    except Exception as e:
        logger.info("调用大模型失败，error:{}".format(e))

