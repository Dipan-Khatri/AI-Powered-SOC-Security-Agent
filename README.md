# 🚀 AI-Powered SOC Security Agent

An AI-inspired SOC security agent that analyzes suspicious security events, calculates dynamic risk scores, correlates attack behavior, and generates automated incident response recommendations.

---

# 📌 Overview

This project simulates how modern Security Operations Center (SOC) teams prioritize cyber threats using:

* Risk-based alerting
* Event correlation
* Threat scoring
* Automated incident response recommendations

The system processes simulated security logs and identifies potentially compromised users based on suspicious activity patterns.

---

# ⚠️ Problem

Security analysts receive thousands of alerts daily.

Manual analysis is:

* Time-consuming
* Difficult to prioritize
* Prone to alert fatigue
* Hard to scale efficiently

Organizations need automated ways to:

* Detect suspicious activity
* Prioritize threats
* Recommend response actions

---

# 💡 Solution

This Python-based AI security agent:

* Parses security event logs
* Assigns weighted risk scores
* Correlates multiple suspicious behaviors
* Detects high-risk users
* Generates automated incident response recommendations
* Exports investigation results into a structured incident report

---

# 🧠 Risk Scoring Logic

| Event Type                             | Risk Points |
| -------------------------------------- | ----------- |
| EMAIL_RECEIVED                         | 5           |
| LINK_CLICKED                           | 25          |
| LOGIN_FAILED                           | 10          |
| LOGIN_SUCCESS from suspicious location | 45          |
| PASSWORD_CHANGED                       | 30          |
| MAILBOX_FORWARDING_ENABLED             | 50          |

---

# 🚨 Risk Levels

| Risk Score | Risk Level |
| ---------- | ---------- |
| 150+       | 🔴 HIGH    |
| 60–149     | 🟠 MEDIUM  |
| Below 60   | 🟢 LOW     |

---

# 📸 Execution Output

![Terminal Output](Screenshot%202026-06-04%20131230.png)

---

# 🧪 Example Output

```text
=== AI Threat Detection Risk Report ===

User: dipan
Risk Score: 175
Risk Level: HIGH

Recommendation:
Disable account, reset password, remove forwarding rules, and investigate immediately.
```

---

# 🧾 Sample Security Events

```text
2026-05-10 09:01:22 USER=dipan EVENT=EMAIL_RECEIVED SUBJECT="Urgent Password Reset"

2026-05-10 09:02:10 USER=dipan EVENT=LINK_CLICKED URL="http://fake-microsoft-login.com"

2026-05-10 09:04:15 USER=dipan EVENT=LOGIN_SUCCESS IP=185.22.44.10 LOCATION=Russia

2026-05-10 09:06:55 USER=dipan EVENT=MAILBOX_FORWARDING_ENABLED
```

---

# 📄 Generated Report

The program automatically creates:

```text
incident_report.txt
```

This simulates how enterprise SOC tools generate investigation and incident response reports.

---

# 🛠 Technologies Used

* Python
* Regex
* File Handling
* Risk Scoring Logic
* Event Correlation
* Security Automation

---

# 🧠 Skills Demonstrated

* SOC investigation workflow
* Detection engineering concepts
* Threat prioritization
* Event correlation
* Risk-based alerting
* Incident response logic
* Python automation
* Security reporting

---

# 🌍 Real-World SOC Relevance

This project simulates how modern SOC teams prioritize alerts using risk-based detection and automated response logic.

The workflow reflects real-world processes used in:

* SIEM platforms
* Threat detection systems
* SOC monitoring environments
* Detection engineering teams

This project demonstrates the transition from:

```text
Raw Logs → Detection → Correlation → Risk Scoring → Response Recommendation
```

---

# ⚙️ How to Run

```bash
git clone https://github.com/Dipan-Khatri/AI-Powered-SOC-Security-Agent.git

cd AI-Powered-SOC-Security-Agent

python main.py
```

---

# 📂 Project Files

```text
main.py
security_logs.txt
incident_report.txt
README.md
```

---

# 🔮 Future Improvements

* MITRE ATT&CK Mapping Integration
* Real-time log monitoring
* Machine learning risk scoring
* Web dashboard visualization
* Splunk integration
* CSV/JSON export support
* Automated alert generation

---

# 👨‍💻 Author

Dipan Khatri

Cybersecurity Enthusiast | Aspiring SOC Analyst

GitHub:
https://github.com/Dipan-Khatri

LinkedIn:
https://www.linkedin.com/in/dipan-khatri/
