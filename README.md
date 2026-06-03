# 📅 BOL Content Schedule System

> A robust schedule management system for Friday shifts and holiday tracking, purpose-built for the **BEMOL Content Team**.

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![Databricks](https://img.shields.io/badge/databricks-SQL-orange.svg)
![License](https://img.shields.io/badge/license-Proprietary-red.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Security](#security)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [CI/CD Pipeline](#cicd-pipeline)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [Support](#support)

---

## 🎯 Overview

The **BOL Content Schedule System** is a web-based application that provides centralized management for:

- **Friday Shift Schedules**: Track team availability and shift assignments
- **Holiday Tracking**: Maintain a company-wide holiday calendar
- **Role-Based Access**: Password-protected admin panel with public visibility layer
- **Cloud-Native Architecture**: Built on Databricks for scalability and reliability

The system implements a dual-interface model:
- **Admin Panel**: Secure management interface with CRUD operations
- **Public View**: Read-only interface for team visibility and planning

---

## 🏗️ Architecture

The project follows the **MVC (Model-View-Controller)** pattern for clean separation of concerns:

```
sistema-de-escala-conteudo-bol/
│
├── 📁 models/
│   └── database.py                  # Data access layer (Databricks integration)
│
├── 📁 views/
│   ├── admin_view.py                # Admin interface components
│   └── public_view.py               # Public-facing interface
│
├── 📁 controllers/
│   └── auth.py                      # Authentication & authorization logic
│
├── 📄 admin.py                      # Streamlit admin application
├── 📄 public.py                     # Streamlit public application
├── 📄 config.py                     # Centralized configuration management
├── 📄 setup_database.py             # Database initialization script
│
├── 📄 requirements.txt              # Python dependencies
├── 📄 .env                          # Environment variables (DO NOT COMMIT)
├── 📄 .env.example                  # Environment template
│
└── 📁 .github/workflows/
    └── ci.yml                       # GitHub Actions CI pipeline
```

### Data Flow

```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │
   ┌───▼────────────┐
   │  Streamlit App │
   │ (admin/public) │
   └───┬────────────┘
       │
   ┌───▼──────────────────┐
   │   Controllers (Auth) │
   └───┬──────────────────┘
       │
   ┌───▼──────────────────┐
   │  Models (Database)   │
   └───┬──────────────────┘
       │
   ┌───▼──────────────────────────────────┐
   │  Databricks (Cloud Data Platform)    │
   │  Tables: escalas_sexta, feriados     │
   └──────────────────────────────────────┘
```

---

## ✅ Prerequisites

Before getting started, ensure you have:

- **Python 3.10+** installed on your system
- **Git** for version control
- **Databricks Workspace** access with appropriate permissions
- **Personal Access Token** from Databricks (for authentication)
- **pip** (Python package manager)

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.10 | 3.11+ |
| Memory | 2 GB | 4 GB+ |
| Disk Space | 500 MB | 1 GB+ |

---

## 🔐 Security

This project implements security best practices:

### Credential Management

- ✅ All credentials stored in environment variables via `.env`
- ✅ `.gitignore` configured to prevent accidental credential commits
- ✅ `.env.example` provided as template for developers
- ✅ Sensitive files excluded from version control

### Access Control

- ✅ Role-based access control (RBAC) via email allowlist
- ✅ Password-protected admin panel with session management
- ✅ Separate authentication layer (`controllers/auth.py`)
- ✅ Clear separation between public and admin interfaces

### Data Protection

- ✅ Databricks managed encryption
- ✅ Personal Access Token authentication
- ✅ HTTPS encryption in transit (Streamlit Cloud native)
- ✅ Environment-based secret injection

⚠️ **Important**: Never commit `.env` files or hardcode credentials in the codebase.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_ORG/sistema-de-escala-conteudo-bol.git
cd sistema-de-escala-conteudo-bol
```

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows
.\venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file from the template:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
# Databricks Configuration
DATABRICKS_SERVER_HOSTNAME
DATABRICKS_HTTP_PATH
DATABRICKS_TOKEN

# Application Security
ADMIN_PASSWORD=your_secure_password_here

# Optional: Application Configuration
APP_TIMEZONE=America/Manaus
LOG_LEVEL=INFO
```

### 5. Initialize the Database

Before running the application, create the required tables:

```bash
python setup_database.py
```

This script will:
- ✅ Connect to your Databricks workspace
- ✅ Create the `escalas_sexta` table (Friday schedules)
- ✅ Create the `feriados` table (holidays)
- ✅ Validate the schema

---

## 💼 Usage

### Admin Panel

```bash
streamlit run admin.py
```

**Access Requirements:**
- Email in authorized list (configured in `config.py`)
- Admin password from environment variables

**Features:**

| Feature | Description |
|---------|-------------|
| 🔐 Secure Login | Email-based authentication with password verification |
| ➕ Add Schedule | Create new Friday shift entries with team members |
| ✏️ Edit Schedule | Update existing schedule records |
| 🗑️ Delete Schedule | Remove outdated or incorrect entries |
| ➕ Add Holiday | Register company holidays |
| ✏️ Edit Holiday | Modify holiday information |
| 🗑️ Delete Holiday | Remove holiday entries |
| 🧹 Auto-Cleanup | Past dates automatically removed on login |
| 📊 Data Validation | Input validation and error handling |

### Public View

```bash
streamlit run public.py
```

**Features:**

| Feature | Description |
|---------|-------------|
| 📅 View Schedules | Display all upcoming Friday shifts |
| 🎉 View Holidays | Show all registered company holidays |
| 📍 Chronological Order | Entries sorted by date (nearest first) |
| 🔴 Visual Highlight | Next upcoming event highlighted in light red |
| 🧹 Auto-Cleanup | Past entries automatically removed on load |
| 🔓 No Login Required | Accessible to all team members |
| 📱 Responsive Design | Mobile-friendly interface |

---

## 🔄 CI/CD Pipeline

The project uses **GitHub Actions** for automated continuous integration and validation on every push and pull request.

### Pipeline Configuration

**File**: `.github/workflows/ci.yml`

```yaml
name: CI Pipeline

on:
  push:
    branches: ["master", "main"]
  pull_request:
    branches: ["master", "main"]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Syntax Validation
        run: |
          python -m py_compile admin.py
          python -m py_compile public.py
          python -m py_compile config.py

      - name: Code Quality Check (Optional)
        run: |
          pip install pylint
          pylint --disable=all --enable=E admin.py public.py || true
```

### Pipeline Stages

| Stage | Purpose | Status |
|-------|---------|--------|
| **Checkout** | Retrieve latest code from repository | ✅ Always |
| **Setup Python** | Configure Python 3.10+ environment | ✅ Always |
| **Install Dependencies** | Install packages from `requirements.txt` | ✅ Always |
| **Syntax Validation** | Check Python syntax errors | ✅ Always |
| **Code Quality** | Optional linting and code analysis | ⚠️ Non-blocking |

### Adding the Workflow

Save the pipeline configuration to your repository:

```bash
mkdir -p .github/workflows
# Save the ci.yml content to .github/workflows/ci.yml
```

---

## 🌐 Deployment

### Streamlit Cloud Deployment

**Step 1: Push Code to GitHub**

```bash
git add .
git commit -m "Deploy to Streamlit Cloud"
git push origin main
```

**Step 2: Connect to Streamlit Cloud**

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Select your GitHub repository
4. Choose branch (`main` or `master`)
5. Set main file path to `admin.py` or `public.py`

**Step 3: Configure Secrets**

In the Streamlit Cloud dashboard → Settings → Secrets:

```toml
# .streamlit/secrets.toml
DATABRICKS_SERVER_HOSTNAME
DATABRICKS_HTTP_PATH 
DATABRICKS_TOKEN 
ADMIN_PASSWORD 
```

**Step 4: Deploy**

Streamlit Cloud automatically:
- ✅ Installs dependencies from `requirements.txt`
- ✅ Manages secrets securely
- ✅ Deploys on every push to main branch
- ✅ Provides automatic HTTPS and CDN

---

## 🔧 Troubleshooting

### Common Issues

#### Issue: `ModuleNotFoundError: No module named 'databricks'`

**Solution:**
```bash
pip install --upgrade databricks-sql-connector
pip install -r requirements.txt
```

#### Issue: `Connection refused` to Databricks

**Solution:**
- Verify `DATABRICKS_SERVER_HOSTNAME` is correct
- Check if Personal Access Token is valid
- Ensure Databricks workspace is accessible
- Test connection manually:

```python
from databricks import sql

try:
    conn = sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        personal_access_token=os.getenv("DATABRICKS_TOKEN")
    )
    print("✅ Connection successful!")
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")
```

#### Issue: Admin login fails

**Solution:**
- Verify email is in the authorized list in `config.py`
- Confirm `ADMIN_PASSWORD` in `.env` matches
- Check for extra spaces or special characters
- Ensure `.env` file is properly loaded:

```bash
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('ADMIN_PASSWORD'))"
```

#### Issue: Streamlit Cloud deployment fails

**Solution:**
- Check GitHub Actions logs for syntax errors
- Verify all secrets are configured in Streamlit dashboard
- Ensure `requirements.txt` includes all dependencies
- Check repository permissions and access tokens

### Debugging Mode

Enable debug logging:

```bash
# Run with verbose output
streamlit run admin.py --logger.level=debug
```

### Getting Help

1. Check application logs: `streamlit run admin.py --logger.level=info`
2. Verify environment variables: `python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.environ)"`
3. Test database connection independently
4. Check GitHub Actions workflow logs

---

## 📦 Tech Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.10+ | Core programming language |
| **Streamlit** | 1.28+ | Web framework & UI |
| **Databricks** | SQL | Cloud data platform |
| **python-dotenv** | Latest | Environment variable management |
| **pandas** | Latest | Data manipulation & analysis |
| **databricks-sql-connector** | Latest | Database connectivity |

### Alternative Data Sources

This system can be adapted to work with:
- ✅ PostgreSQL / MySQL
- ✅ Azure SQL Database
- ✅ Amazon RDS
- ✅ MongoDB
- ✅ Google Cloud SQL

---

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### Branch Strategy

```bash
# Create feature branch
git checkout -b feature/my-feature

# Make changes and commit
git add .
git commit -m "Add feature: describe what you did"

# Push to remote
git push origin feature/my-feature

# Create Pull Request on GitHub
```

### Code Standards

- Follow PEP 8 style guide
- Add docstrings to functions
- Test locally before pushing
- Ensure CI pipeline passes
- Update README if adding new features

### Commit Message Format

```
[TYPE] Short description (50 chars max)

Detailed explanation if needed (72 chars per line)

Type: feat, fix, docs, refactor, test, ci
```

---

## 📞 Support

### Documentation

- 📖 [Streamlit Documentation](https://docs.streamlit.io)
- 🗄️ [Databricks SQL Documentation](https://docs.databricks.com/sql)
- 🐍 [Python Documentation](https://docs.python.org/3)

### Issue Reporting

Found a bug? Please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Environment details (Python version, OS)
- Error messages or logs
- Screenshots if applicable

### Contact

- **Team**: BEMOL Content Team
- **Email**: [your-team-email]
- **Slack**: [your-slack-channel]

---

## 📜 License

**Proprietary** — © BEMOL S.A. All rights reserved.

Unauthorized copying or distribution of this software is strictly prohibited.

---

## 🙏 Acknowledgments

- BEMOL Content Team for requirements and feedback
- Streamlit for the excellent web framework
- Databricks for cloud infrastructure

---

**Last Updated**: June 2026
**Maintained By**: BEMOL Technical Team
**Status**: ✅ Active & Maintained
