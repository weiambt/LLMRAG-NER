# LLMRAG-NER

[English Version](./README.md)

## 项目简介

LLMRAG-NER 是一个基于**检索增强生成（RAG）的命名实体识别**系统，利用大语言模型（LLM）进行实体抽取。

## 核心功能

- **RAG 增强的 NER**：使用向量相似度检索相关示例
- **多实体类型支持**：识别人名(PER)、地名(LOC)、组织名(ORG)
- **灵活的 LLM 集成**：通过工厂模式支持多种 LLM 后端
- **投票机制**：集成投票提升识别准确率

## 项目结构

| 文件 | 说明 |
|------|------|
| `VectorDB.py` | 向量数据库，用于相似度检索 |
| `preprocess.py` | BIO 格式数据预处理为 JSON |
| `main.py` | RAG 主流程 |
| `llm_client.py` | LLM 客户端接口 |
| `evaluate.py` | 评估指标 |
| `vote.py` | 投票机制 |
| `conf/` | 配置文件目录 |
| `data/` | 训练和开发数据集 |
| `result/` | 输出结果目录 |
| `utils/` | 工具模块 |

## 快速开始

```bash
# 将 BIO 格式数据处理为 JSON
python preprocess.py

# 运行 RAG-NER 流程
python main.py
```

## 工作流程

1. **数据预处理**：将 BIO 标注格式转换为 JSON
2. **向量构建**：使用 spaCy 中文模型分句，HuggingFace 嵌入向量化
3. **相似度检索**：根据输入查询检索 top-k 相似示例
4. **示例增强**：将相似示例作为 prompt 的一部分
5. **LLM 调用**：触发大模型进行实体识别
6. **结果输出**：保存识别结果

## 依赖

- Python 3.x
- spaCy (zh_core_web_sm)
- LangChain
- ChromaDB
- HuggingFace sentence-transformers