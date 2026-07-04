# AI Intelligence Assistant

一个基于 FastAPI + LLM 的 AI 应用开发项目。

## 项目简介

本项目是一个 AI 助手后端服务，目标是实现：

- 多模型支持（DeepSeek、OpenAI 等）
- 对话接口
- Prompt 管理
- Tool Calling
- RAG 检索增强
- 会话管理
- 日志监控
- Docker 部署

本项目按照企业级后端架构开发，重点体现 AI 应用开发能力，而不仅仅是调用大模型 API。

---

## 技术栈

- Python 3.13
- FastAPI
- OpenAI SDK
- DeepSeek API
- Pydantic
- Uvicorn
- Git & GitHub

---

## 项目结构

```text
app
├── api
├── core
├── models
├── services
├── utils
└── main.py
```

---

## 当前开发进度

- [x] 项目初始化
- [x] FastAPI 服务
- [x] Health Check
- [ ] LLM Client
- [ ] Chat API
- [ ] Prompt 管理
- [ ] Tool Calling
- [ ] RAG
- [ ] Docker 部署

---

## 启动方式

```bash
uvicorn app.main:app --reload
```