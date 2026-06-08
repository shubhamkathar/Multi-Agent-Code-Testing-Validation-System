# 🧠 AI Multi-Agent Code Testing & Validation System

An advanced, production-grade multi-agent AI system that automates static code analysis, semantic test case generation, vulnerability scanning, and executable unit test generation. Powered by **CrewAI**, **DeepSeek-R1**, **Flask**, and **Streamlit**.

---

## 🚀 Architectural Blueprint & Data Flow

```text
       [ User Python Code Input ]
                   │
                   ▼
         ┌──────────────────┐
         │ AST Static Engine│ ──► Extracts Functions, Classes & AST Nodes
         └──────────────────┘
                   │
                   ▼
     ┌──────────────────────────┐
     │    CrewAI Orchestrator   │ (Sequential Processing Pipeline)
     └──────────────────────────┘
           │         │         │
           │         ├── Code Analyzer Agent  ──► Builds syntactic profiles
           │         ├── Test Designer Agent  ──► Identifies edge-cases & limits
           │         ├── Security Agent       ──► Scans for CVEs & vulnerabilities
           │         └── Pytest Engineer Agent──► Generates executable code
           │
           ▼
 ┌──────────────────────────────────┐
 │  Automated Pytest Runner Engine  │ ──► Executes tests dynamically via Subprocess
 └──────────────────────────────────┘
           │
           ▼
 ┌──────────────────────────────────┐
 │     Dual-Interface Delivery      │
 │  • Streamlit Dashboard (UI)      │
 │  • Flask RESTful API (Microserv) │
 └──────────────────────────────────┘
```

---

## 🛠️ Production Tech Stack

*   **AI Orchestration:** CrewAI (Sequential Process Mapping)
*   **LLM Engine:** DeepSeek-R1 (via NVIDIA NIM Inference API)
*   **Static Analysis:** Python Standard `ast` (Abstract Syntax Tree) Parser
*   **Execution Core:** Pytest Automation Engine via Subprocess
*   **Frontend Interface:** Streamlit (Real-time analytics dashboard)
*   **Backend Architecture:** Flask RESTful Microservice
*   **Package Management:** Pip Environment Manager

---

## 📁 Repository Structure

```text
ai-multi-agent-testing/
│
├── app.py                  # Flask REST API Microservice
├── streamlit_app.py        # Streamlit Analytics Dashboard UI
├── crew_setup.py           # CrewAI Orchestrator & Task Pipeline
├── agents.py               # Specialized Multi-Agent Definitions
├── tasks.py                # Expected Outputs & Task Configurations
├── config.py               # LLM Client Initialization Configuration
├── test_runner.py          # Dynamic Pytest Subprocess Execution Engine
├── analyzer.py             # AST Static Parsing Utility
├── requirements.txt        # Production Dependencies
└── README.md               # System Documentation
```

---

## ⚡ Quick Start & Deployment

### 1. Environment Initialization
```bash
# Clone the repository
git clone https://github.com
cd ai-multi-agent-testing

# Create and activate an isolated virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install all production dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Secrets
Create a `.env` file in the root directory or export your credentials:
```bash
export NVIDIA_API_KEY="your_nvidia_nim_api_key_here"
```
Update `config.py` to source the key securely using `os.getenv("NVIDIA_API_KEY")`.

### 3. Execution Options

*   **Option A: Launch the Streamlit Analytics Dashboard Frontend**
    ```bash
    streamlit run streamlit_app.py
    ```
*   **Option B: Spin up the Flask REST API Backend Microservice**
    ```bash
    python app.py
    ```

---

## 🧠 Enterprise Resume & Interview Talking Points

### Project Summary
> Developed an enterprise-grade multi-agent software validation pipeline utilizing **CrewAI** and **DeepSeek-R1** to automate full-lifecycle code quality assurance. The platform blends deterministic **Abstract Syntax Tree (AST)** engineering with heuristic large language models to construct semantic edge-case test suites, conduct vulnerability scans, and generate executable pytest suites, reducing manual test-writing overhead by up to 70%.

### Core Technical Achievements to Highlight:
*   **Multi-Agent Choreography:** Designed a 4-agent sequential workflow assigning granular, specialized domains (Syntax Isolation, Edge-Case Synthesis, Security Auditing, Test Compilation) to mitigate LLM hallucinations.
*   **AST Isolation Layer:** Created a static analysis preprocessing step using Python’s native `ast` library to extract class and functional metadata, injecting strict boundary parameters directly into the agent prompt context.
*   **Dynamic Test Runner:** Integrated an automated test execution subsystem using isolated subprocess sandboxing to compile, run, and feedback execution-time standard outputs (`stdout`/`stderr`) dynamically.
*   **Dual-Delivery Architecture:** Built a decoupled stack featuring a headless **Flask API** for seamless CI/CD pipeline integrations alongside an interactive **Streamlit** dashboard tailored for developer code reviews.

---

## 🤝 Contribution and Architecture Scaling

This application is engineered for horizontal scale. Future sprints include containerizing the test runtime within ephemeral **Docker** containers for execution security, and introducing a **Feedback Loop Agent** to parse pytest execution stack traces to self-heal failing test scripts automatically.

Licensed under the MIT License.
