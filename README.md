# ACEest DevOps Assignment

## 📌 Project Overview

This project is a Flask-based Fitness Client Management Web Application. It demonstrates the implementation of CI/CD practices using GitHub Actions, Docker, and Jenkins.

---

## 🚀 Features

* Add new client (Name, Age, Weight)
* View client list
* Automated testing using Pytest
* Docker containerization
* CI/CD pipeline using GitHub Actions
* Jenkins integration for local CI

---

## 🛠️ Tech Stack

* Python (Flask)
* SQLite Database
* Pytest
* Docker
* GitHub Actions
* Jenkins

---

## 📂 Project Structure

```
aceest-devops/
│
├── app.py
├── requirements.txt
├── test_app.py
├── Dockerfile
├── README.md
│
├── templates/
│   ├── index.html
│   └── add_client.html
│
└── .github/workflows/
    └── main.yml
```

---

## ⚙️ Local Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/2024tm93719/ACEest-DevOps-Assignment.git
cd ACEest-DevOps-Assignment
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Run Application

```
python app.py
```

Open in browser:

```
http://localhost:5000
```

---

### 4. Run Tests

```
pytest
```

---

## 🐳 Docker Setup

### Install Docker

1. Download Docker Desktop from:
   https://www.docker.com/products/docker-desktop/
2. Install Docker Desktop and restart your system
3. Start Docker Desktop application

### Verify Installation

```
docker --version
```

---

### Build Docker Image

```
docker build -t aceest-app .
```

---

### Run Docker Container

```
docker run -p 5000:5000 aceest-app
```

Open in browser:

```
http://localhost:5000
```

---

## 🔄 CI/CD using GitHub Actions

* Pipeline runs automatically on every push and pull request
* Steps performed:

  * Install dependencies
  * Run tests using pytest
  * Build Docker image

### Workflow File Location

```
.github/workflows/main.yml
```

---

## ⚙️ Jenkins Setup

### Prerequisites

* Install Java (JDK 17)
* Install Jenkins

---

### Install Java

1. Download from: https://adoptium.net/
2. Install JDK 17
3. Set environment variable:

   ```
   JAVA_HOME = C:\Program Files\Eclipse Adoptium\jdk-17
   ```
4. Add to PATH:

   ```
   %JAVA_HOME%\bin
   ```

---

### Install Jenkins

1. Download from: https://www.jenkins.io/download/
2. Install using Windows `.msi` installer
3. Select **Run service as Local System**
4. Open Jenkins:

   ```
   http://localhost:8080
   ```

---

### Unlock Jenkins

1. Open file:

   ```
   C:\Program Files\Jenkins\secrets\initialAdminPassword
   ```
2. Copy password and paste into Jenkins UI
3. Install suggested plugins
4. Create admin user

---

### Create Jenkins Job

1. Click **New Item**
2. Enter name: `aceest-devops-job`
3. Select **Freestyle Project**
4. Under Source Code Management → Select Git
5. Add your GitHub repository URL
6. Add Build Step → Execute Command:

```
pip install -r requirements.txt
pytest
docker build -t aceest-app .
```

7. Click **Build Now**

---

## 🔁 CI/CD Workflow

```
Local Development → GitHub → GitHub Actions → Jenkins → Docker
```

---

## 📌 Important Notes

* Flask app runs on `0.0.0.0` for Docker compatibility
* Database initializes automatically during app startup
* `.gitignore` and `.dockerignore` are used for clean builds
* GitHub authentication uses Personal Access Token (PAT)

---

## 🎯 Conclusion

This project demonstrates:

* Continuous Integration (CI)
* Automated Testing
* Containerization using Docker
* CI/CD pipeline using GitHub Actions and Jenkins

---

## 👨‍💻 Author

Vikash Mahala
