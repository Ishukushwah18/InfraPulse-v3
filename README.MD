🚀 InfraPulse v3

A modern Infrastructure Monitoring Dashboard built with **Python, Flask, Docker, Docker Compose, and Nginx**.

InfraPulse continuously monitors network devices using Ping and TCP Port checks and displays their real-time status through a clean web dashboard.

---

# 📸 Dashboard

![Dashboard](screenshots/dashboard.png)


---

✨ Features

- ✅ Real-time Network Monitoring
- ✅ Ping Status Check
- ✅ TCP Port Monitoring
- ✅ Responsive Dashboard
- ✅ Auto Refresh every 10 seconds
- ✅ Dockerized Application
- ✅ Nginx Reverse Proxy
- ✅ Docker Compose Deployment
- ✅ Health Check Endpoint
- ✅ Environment Variable Support

---

🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| Flask | Web Framework |
| Docker | Containerization |
| Docker Compose | Multi-container Deployment |
| Nginx | Reverse Proxy |
| HTML/CSS | Dashboard UI |
| Git | Version Control |

---

📁 Project Structure

```
InfraPulse-v3/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .gitignore
│
├── nginx/
│   └── default.conf
│
├── templates/
│   └── index.html
│
└── screenshots/
    └── dashboard.png
```

---

 Installation

Clone the repository

```bash
git clone https://github.com/Ishukushwah18/InfraPulse-v3.git
```

Move into project

```bash
cd InfraPulse-v3
```

Build Docker Image

```bash
docker compose build
```

Start Containers

```bash
docker compose up -d
```

Open browser

```
http://localhost
```

---

📊 Dashboard Monitors

Current monitored hosts:

| Device | Host | Port |
|---------|------|------|
| Google DNS | 8.8.8.8 | 53 |
| Cloudflare DNS | 1.1.1.1 | 53 |
| GitHub | github.com | 443 |

---

❤️ Health Endpoint

```
http://localhost/health
```

Example Response

```json
{
  "status": "UP",
  "application": "InfraPulse",
  "version": "3.0"
}
```

---

🐳 Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up -d
```

Stop

```bash
docker compose down
```

View Logs

```bash
docker compose logs -f
```      

📌 Future Improvements

- CPU Monitoring
- RAM Monitoring
- Disk Usage
- Docker Container Status
- Response Time Graph
- Email Alerts
- Slack Notifications
- Authentication
- Prometheus Integration
- Grafana Dashboard

---

👨‍💻 Author

Ishu Kushwah

IT Technician | Aspiring Cloud & DevOps Engineer

GitHub

https://github.com/Ishukushwah18

LinkedIn

https://www.linkedin.com/in/ishu-kushwah-94b341317

---

⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
