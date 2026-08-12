\# AI Red-Teaming \& Security Evaluation Lab



A local environment for benchmarking, probing, and evaluating Large Language Model (LLM) endpoints against prompt injection, system prompt extraction, and adversarial inputs using \*\*PyRIT\*\*, \*\*garak\*\*, and custom Python probe suites.



\---



\## 📌 Project Overview



This repository demonstrates practical offensive security testing (red-teaming) against a local LLM customer support endpoint (`http://localhost:8000/chat`). The goal is to identify safety boundaries, evaluate resilience against adversarial prompts, and document jailbreak and extraction vulnerabilities.



\---



\## 🛠️ Repository Structure



```text

ai-red-teaming-lab/

├── app/

│   └── main.py              # Local FastAPI target application (LLM endpoint)

├── results/

│   ├── pyrit\_results.json   # Output log from custom adversarial probe suite

│   └── garak\_hitlog...     # Automated vulnerability scan logs from garak

├── simple\_test.py           # Custom Python adversarial probe runner

├── garak\_target.py          # Custom function wrapper for garak integration

├── requirements.txt         # Environment dependencies lockfile

└── README.md                # Project documentation \& vulnerability report

---

## 🙏 Acknowledgements & Attribution

This lab implementation is based on the AI Red-Teaming Lab guide from [Taimur Ijlal's AI Security Projects repository](https://github.com/taimurijlal/AI-Security-Projects/tree/main/01-ai-red-teaming-lab).
