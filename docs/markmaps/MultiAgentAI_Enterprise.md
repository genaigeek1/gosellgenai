---
title: Multi Agent AI Enterprise
markmap:
  colorFreezeLevel: 2
---

# Multi Agent AI Enterprise

## What are Agents?
- Intelligent systems acting on behalf of users
- Capabilities:
  - Reasoning
  - Planning
  - Memory

## Why Multi-Agent Systems?
- Collaborate across multiple agents
- Operate across different frameworks/providers
- Work under human supervision
- Think multiple steps ahead
- Execute tasks across various systems

## Enablers of Multi-Agent Systems
- Advanced reasoning models (e.g., Gemini 2.5) (🟦 First Party, GA)
- Workflow integration (⚪ Third Party / Custom)
- Access to enterprise data

## Vertex AI Role (🟦 First Party, GA)
- Orchestrates production AI:
  - Models
  - Data
  - Agents
- Combines:
  - Open approach (🟩 Open Source support)
  - Comprehensive platform features
- Delivers:
  - Seamless agent performance
  - Avoidance of fragmented, fragile solutions

## Agent Development & Deployment

### Agent Development Kit (ADK) (🟩 Open Source, 🟨 Public Preview)
- Build agents in <100 lines of Python
- Guardrails and orchestration for control
- Bidirectional audio & video streaming
- Integrated Agent Garden:
  - Samples, reusable patterns
- Model flexibility:
  - Gemini (🟦), 200+ Model Garden models (⚪/🟩)
- Deploy to:
  - Local, Cloud Run, Kubernetes, Vertex AI
- Supports Model Context Protocol (MCP) (🟩, 🟨 Public Preview)
- Optimized for Gemini 2.5 Pro Experimental
- ![ADK framework](https://storage.googleapis.com/gweb-cloudblog-publish/original_images/Image_1_ADK_Coding.gif)

#### Customer Use Cases
- **Revionics** – Retail pricing with agentic AI
- **Renault** – EV charger optimization via agents
- **Nippon TV** – Video AI agent on Agent Engine + Workflows

### Agent Engine (🟦 First Party, GA)
- Fully managed production runtime
- Works with any framework (ADK, LangGraph, Crew.ai)
- Compatible with major models: Gemini, Claude, Mistral AI
- Features:
  - Context memory (short- & long-term)
  - Evaluation tools + Example Store
  - Integration with Google Agentspace
- ![Agent Engine](https://storage.googleapis.com/gweb-cloudblog-publish/images/Image_2_Agent_Engine.max-1900x1900.png)

#### Coming Soon
- Simulation testing
- Code execution
- Computer-use capabilities

## Agent Interoperability & Collaboration

### Agent2Agent Protocol (🟩 Open Source Initiative, 🟨 Public Preview)
- Enables agent communication across frameworks
- Negotiates interaction methods
- 50+ partners: Box, Salesforce, UiPath, etc.
- ![Partners](https://storage.googleapis.com/gweb-cloudblog-publish/images/image1_yIJGtNA.max-1400x1400.png)

## Data & Tool Integration

### Enterprise Truth Access
- MCP in ADK (🟩, 🟨 Public Preview)
- 100+ prebuilt connectors: AlloyDB, BigQuery, NetApp
- Call tools from:
  - LangGraph, LangChain, CrewAI, MCP, OpenAPI
- API access via Apigee (800K+ APIs) (🟦 First Party)

### Grounding & Enrichment
- Google Search (🟦)
- 3rd-Party Data: Cotality, S&P Global, Zoominfo
- Google Maps (🟦, 🟨 Public Preview): 100M+ updates/day

## Enterprise-Ready Controls & Security

### Gemini & Vertex AI Safeguards
- Configurable safety filters
- Identity-based permissions
- VPC Service Controls (🟦)
- Guardrails:
  - Input screening
  - DB access restrictions
  - Tool validators
- Full observability:
  - Tracing, action logging, reasoning paths

## Getting Started with Vertex AI Agents
- Build: ADK (🟩)
- Deploy: Agent Engine (🟦) or custom
- Integrate: MCP, APIs, Connectors
- Secure: VPC, IAM, Guardrails
- Explore: Vertex AI Console & Docs

## 🆚 Comparison with LangChain Ecosystem

### LangChain Stack (🟩 Open Source + 🟨 Beta/GA)
- **LangChain** – Agent abstractions, toolchains
- **LangGraph** – State-machine agent orchestration
- **LangSmith** – Observability & evaluation

### Vertex AI vs. LangChain
- **ADK vs. LangChain** – Framework comparison
- **Agent Engine vs. LangGraph** – Runtime vs. orchestrator
- **Vertex vs. LangSmith** – Native ops vs. open tracing tools
- **Agent2Agent vs. LangGraph Messaging** – Interop protocols