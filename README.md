# LLMRAG-NER

[中文](#中文说明) | [English](#english)

---

## English

### Overview

LLMRAG-NER is a **Retrieval-Augmented Generation (RAG) based Named Entity Recognition** system that leverages Large Language Models (LLM) for entity extraction. The project implements a similarity-based example augmentation approach to improve NER performance.

### Features

- **RAG-based NER**: Uses vector similarity search to retrieve relevant examples
- **Multi-entity Support**: Recognizes PER (Person), LOC (Location), ORG (Organization)
- **Flexible LLM Integration**: Supports multiple LLM backends via factory pattern
- **Voting Mechanism**: Ensemble voting for improved accuracy

### Project Structure

```
LLMRAG-NER/
├── VectorDB.py          # Vector database for similarity search
├── preprocess.py        # BIO to JSON data preprocessing
├── main.py              # Main RAG pipeline
├── llm_client.py        # LLM client interface
├── evaluate.py          # Evaluation metrics
├── vote.py              # Voting mechanism
├── conf/                # Configuration files
├── data/                # Training and dev datasets
├── result/              # Output results
└── utils/               # Utilities (logger, json_util, config)
```

### Quick Start

```bash
# Process BIO format data to JSON
python preprocess.py

# Run RAG-NER pipeline
python main.py
```

### Configuration

Edit `conf/dev/llm.ini` to configure LLM parameters.

---

## 中文说明

### 项目简介

LLMRAG-NER 是一个基于**检索增强生成（RAG）的命名实体识别**系统，利用大语言模型（LLM）进行实体抽取。项目采用基于相似度的示例增强方法来提升 NER 效果。

### 核心功能

- **RAG 增强的 NER**：使用向量相似度检索相关示例
- **多实体类型支持**：识别人名(PER)、地名(LOC)、组织名(ORG)
- **灵活的 LLM 集成**：通过工厂模式支持多种 LLM 后端
- **投票机制**：集成投票提升识别准确率

### 项目结构

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
| `utils/` | 工具模块（日志、JSON工具、配置） |

### 快速开始

```bash
# 将 BIO 格式数据处理为 JSON
python preprocess.py

# 运行 RAG-NER 流程
python main.py
```

### 配置说明

编辑 `conf/dev/llm.ini` 配置 LLM 参数。

### 工作流程

1. **数据预处理**：将 BIO 标注格式转换为 JSON
2. **向量构建**：使用 spaCy 中文模型分句，HuggingFace 嵌入向量化
3. **相似度检索**：根据输入查询检索 top-k 相似示例
4. **示例增强**：将相似示例作为 prompt 的一部分
5. **LLM 调用**：触发大模型进行实体识别
6. **结果输出**：保存识别结果

### 依赖

- Python 3.x
- spaCy (zh_core_web_sm)
- LangChain
- ChromaDB
- HuggingFace sentence-transformers

---

<p align="center">Built with RAG + LLM for Named Entity Recognition</p>