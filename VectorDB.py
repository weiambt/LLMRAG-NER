
import json
from langchain.document_loaders import TextLoader
from langchain.docstore.document import Document
import spacy
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

class VectorDB:
    def __init__(self,data_path,logger):
        self.db = None
        self.logger = logger
        self.init_db(data_path)

    def init_db(self,data_path):
        # 加载中文模型
        nlp = spacy.load("zh_core_web_sm")

        # 加载文档
        loader = TextLoader(data_path)
        documents = loader.load()
        text = documents[0].page_content  # 提取文本内容
        # 先根据\n分割
        paragraphs = [p.strip() for p in text.split('\n') if p.strip()]

        sentences = []
        for para in paragraphs:
            doc = nlp(para)
            # 暂时只按\n划分
            # sentences.extend([sent.text.strip() for sent in doc.sents if sent.text.strip()]) # todo 这里是以句号分割的，如果没有句号多个句子会变成同一个句子
            sentences.append(doc.text)
        # 创建句子级Document对象
        docs = [Document(page_content=s, metadata={"source": "your_file.txt"}) for s in sentences]

        # 配置嵌入模型
        embeddings = HuggingFaceEmbeddings(
            model_name="../huggingface/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
            # model_name="../huggingface/bert-base-chinese"
        )

        # 存入向量数据库
        self.db = Chroma.from_documents(
            documents=docs,
            embedding=embeddings,
            # persist_directory="./chroma_db"  # 向量数据库存储路径
        )
        # db.persist()

    def search(self,query,k):
        # 检索相似句子
        results = self.db.similarity_search(query, k=k)
        res = []# 返回前3个相似句子
        for doc in results:
            # print(doc.page_content)
            res.append(doc.page_content)
        return res


if __name__ == '__main__':
    db = VectorDB(data_path="./data.txt")
    res = db.search("李四",k=2)
    print(res)