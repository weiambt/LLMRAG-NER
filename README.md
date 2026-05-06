# LLMRAG-NER

[中文版](./README_zh.md)

## Overview

LLMRAG-NER is a **Retrieval-Augmented Generation (RAG) based Named Entity Recognition** system that leverages Large Language Models (LLM) for entity extraction.

## Features

- **RAG-based NER**: Uses vector similarity search to retrieve relevant examples
- **Multi-entity Support**: Recognizes PER (Person), LOC (Location), ORG (Organization)
- **Flexible LLM Integration**: Supports multiple LLM backends via factory pattern
- **Voting Mechanism**: Ensemble voting for improved accuracy

## Project Structure

| File | Description |
|------|-------------|
| `VectorDB.py` | Vector database for similarity search |
| `preprocess.py` | BIO to JSON data preprocessing |
| `main.py` | Main RAG pipeline |
| `llm_client.py` | LLM client interface |
| `evaluate.py` | Evaluation metrics |
| `vote.py` | Voting mechanism |
| `conf/` | Configuration files |
| `data/` | Training and dev datasets |
| `result/` | Output results |
| `utils/` | Utilities |

## Quick Start

```bash
# Process BIO format data to JSON
python preprocess.py

# Run RAG-NER pipeline
python main.py
```

## Workflow

1. **Preprocess**: Convert BIO format to JSON
2. **Vectorize**: Sentence splitting with spaCy, embedding with HuggingFace
3. **Retrieve**: Search top-k similar examples by vector similarity
4. **Augment**: Include retrieved examples in prompt
5. **Extract**: Call LLM for entity recognition
6. **Output**: Save recognition results

## Dependencies

- Python 3.x
- spaCy (zh_core_web_sm)
- LangChain
- ChromaDB
- HuggingFace sentence-transformers