# 🎬 CineVisor-Ops: Autonomous Media Infrastructure Agent

![Grafana](https://img.shields.io/badge/Grafana-Cloud_MCP-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Gemini AI](https://img.shields.io/badge/Google_Gemini-3.6_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Python](https://img.shields.io/badge/Python-Flask-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active_Production-success?style=for-the-badge)

**CineVisor-Ops** is an elite, AI-driven observability and automated incident remediation agent built specifically for **Agentic Cinema: The Blockbuster Hackathon (Grafana Track)** hosted by Google Cloud. 

Designed for the high-stakes Media & Entertainment (M&E) industry, CineVisor-Ops autonomously diagnoses critical live-broadcast failures (e.g., 4K stream dropouts, GPU VRAM exhaustion, SRT network jitter) by natively integrating with the **Grafana Cloud MCP (Model Context Protocol)**.

---

## 🏆 Hackathon Track Alignment: Grafana MCP
This project strictly fulfills the core requirements of the Grafana track by implementing **Actual Runtime Integration** with the Grafana Cloud MCP server. 
* **Interactive Auth:** It utilizes the official OAuth 2.1 browser flow to authenticate dynamically.
* **Real Tool Execution:** It programmatically executes tools to fetch live telemetry (Prometheus metrics, Loki logs, Tempo traces, and IRM alerts) instead of relying solely on simulated prompt data.
* **Actionable Intelligence:** Processes raw telemetry through Google Gemini 3.6 Flash to generate highly technical, Markdown-formatted incident reports and remediation steps.

---

## ✨ Enterprise-Grade Features

* **🧠 Agentic RCA (Root-Cause Analysis):** Powered by `gemini-3.6-flash`, the agent correlates disparate logs, metrics, and traces to understand *why* a broadcast node failed.
* **🔌 Dynamic Grafana MCP Tool Calling:** Natively connects to `mcp.grafana.com` via the official Agent Development Kit (ADK) logic.
* **🔐 Secure Browser Authorization:** Implements interactive browser-based authentication for secure, short-lived session tokens.
* **📊 Markdown Telemetry Dashboard:** Parses raw LLM JSON/Text output into a beautiful, scannable, and highly professional technical incident report UI.
* **🏢 Robust MVC Architecture:** Clean, modular Python codebase separating frontend templates, AI logic, and server routing.

---

## 🏗️ Project Architecture

The project is structured following enterprise microservice patterns:

```text
cinevisor-ops/
│
├── core/
│   └── agent.py            # Gemini AI logic & Grafana MCP Tool Calling engine
│
├── templates/
│   └── index.html          # Frontend UI with Markdown parsing & AJAX submission
│
├── app.py                  # Main Flask Server & Routing Controller
├── requirements.txt        # Python dependencies (Flask, google-generativeai, requests, mcp)
└── .env                    # Environment variables (Ignored in Git for security)
```

**Data Flow:**  
`User Interface` ──(POST)──► `Flask Backend` ──(Trigger)──► `Agent.py` ──(OAuth/HTTP)──► `Grafana Cloud MCP` ──(Context)──► `Gemini 3.6 Flash`

---

## 🚀 Quick Start & Installation

Since the Grafana MCP requires interactive browser authorization, this agent is designed to run locally on your development machine.

### Prerequisites
* Python 3.8 or higher installed.
* A free [Grafana Cloud Account](https://grafana.com/products/cloud/).
* A Google Gemini API Key.
* **Important:** You must accept the Grafana Assistant terms in your Grafana Cloud dashboard (under the AI section) before running the agent.

### 1. Clone the Repository
```bash
git clone [https://github.com/irrathodofficial/cinevisor-ops.git](https://github.com/irrathodofficial/cinevisor-ops.git)
cd cinevisor-ops
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory and add your secure credentials:
```env
GEMINI_API_KEY=your_google_gemini_api_key_here
GRAFANA_MCP_ENDPOINT=[https://mcp.grafana.com/mcp](https://mcp.grafana.com/mcp)
GRAFANA_URL=https://<your-stack-name>.grafana.net
```

### 4. Run the Agent
```bash
python app.py
```
* Open `http://localhost:5000` in your web browser.
* Select a live broadcast incident scenario from the dropdown.
* Click **Execute Gemini Agent + Grafana MCP**.
* *Note: On the first execution, the agent will automatically open a new browser tab for Grafana OAuth authorization. Once authorized, the telemetry will be processed.*

---

## 🎥 Hackathon Demo Video
👉 **[Watch the 3-Minute Live Demo on YouTube](https://youtu.be/YOUR_VIDEO_ID_HERE)**  
*(Watch how CineVisor-Ops authenticates with Grafana Cloud and resolves a 4K Stream Dropout in real-time).*

---

## 👨‍💻 Author
Engineered with passion for infrastructure automation by **Ishwar Rathod**
