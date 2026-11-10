# Autonomous Tool Orchestration & Multi-Capability Support Agent



*Project 2 — Future AWS Agent Engineer Nanodegree*



---



## Overview



This repository contains the full implementation for **Project 2**, featuring an autonomous **AI Customer Support Agent** deployed on **Amazon Bedrock AgentCore Runtime**. Built using a single **Strands SDK `Agent`** orchestrator and the `bedrock-agentcore-starter-toolkit`, this agent acts as an intelligent hub for an e-commerce platform by orchestrating multiple underlying AWS tools and capabilities (Model Context Protocol Gateway, Knowledge Base RAG, AgentCore Memory, and Python Code Interpreter).



### 📚 Detailed Articles & References

For a deep dive into the engineering principles, architectural decisions, and step-by-step walkthrough, check out the following resources:

* 🌐 **Technical Blog Post:** [Read full article](https://blog.jonanata.com/autonomous-tool-orchestration-multi-capability-agent-systems-with-amazon-bedrock-agentcore-strands-sdk/)

* ☁️ **AWS Community Builders Article:** [Read on AWS Builders Center](https://builder.aws.com/content/3LvNEFpOuBTNAYB0cyMRGhcP8y6/autonomous-tool-orchestration-and-multi-capability-agent-systems-with-amazon-bedrock-agentcore-and-strands-sdk)

* 🔗 **Official Starter Template:** [udacity/cd14763-project-starter](https://github.com/udacity/cd14763-project-starter)



---



## Architecture & Integrated Tool Subsystems



The agent unifies five distinct AWS and Bedrock capabilities into a single conversational entry point:



1. **AgentCore Gateway & Model Context Protocol (MCP):** Exposes backend AWS Lambda functions (order tracking, refund processing) dynamically at runtime using MCP docstrings and schema definitions.

2. **Bedrock Knowledge Base (RAG):** Connects to an S3 bucket storing unstructured product catalog and policy documents (`product\_catalog.txt`) for grounded vector search retrieval.

3. **AgentCore Memory:** Provides persistent, cross-session context using custom `MemoryHook` implementations to extract semantic facts and user preferences automatically.

4. **AgentCore Code Interpreter:** Executes exact numerical math (points redemptions, tier calculations, and tiered discounts) inside an isolated Python execution sandbox.

5. **AgentCore Browser Tool:** Grants real-time web access for external URL inspection when information is missing from internal databases.



---



## Repository Structure



```text

├── starter/

│   ├── lambda/

│   │   ├── order\_tracker.py

│   │   ├── refund\_processor.py

│   │   └── lambda schema

│   ├── main.py

│   └── product\_catalog.txt

├── setup\_permissions.py

├── pyproject.toml

└── README.md  





