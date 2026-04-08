🛡️ Sentinel-Agent: AI-Driven System Orchestrator

🚀 Overview
Sentinel-Agent is an **Agentic Coding** project designed to bridge high-level logic with **Linux & Windows System** management. It moves beyond static monitoring by using an autonomous "Sense-Think-Act" loop to maintain system health.
 🧠 The Agentic Loop
 Sense: Scans system processes via `subprocess` calls to `tasklist` (Windows) or `ps` (Linux).
 Think: Dynamically detects the OS environment and triages process memory usage.
 Act: Autonomously generates execution-ready scripts (`.bat` or `.sh`) and programmatically manages file permissions (`chmod`).

#🛠️ Technical Features
- **Cross-Platform Compatibility:** Logic-switch for Windows/POSIX kernels.
- **Automated Remediation:** Generates self-contained fix scripts.
- **System-Level Integration:** Uses pipes and filters to parse stdout data.

## 📈 Outcome-Focused Design
This project was built to demonstrate the **Solutionist** mindset: prioritizing delivered outcomes and automation over manual system triage.
