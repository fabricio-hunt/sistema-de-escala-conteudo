📅 BOL Content Schedule System
> A schedule management system for Friday shifts and holidays, built for the **BEMOL Content Team**.
![CI Pipeline](https://github.com/YOUR_ORG/sistema-de-escala-conteudo-bol/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-framework-red.svg)
![Databricks](https://img.shields.io/badge/databricks-cloud-orange.svg)
---
Overview
The BOL Content Schedule System is a web-based application that manages Friday shift schedules and holiday entries for BEMOL's content team. It provides a password-protected admin panel for managing records and a public-facing view for team visibility — backed by Databricks as the data platform.
---
Architecture
The project follows the MVC (Model-View-Controller) pattern:
```
sistema-de-escala-conteudo-bol/
├── models/
│   └── database.py          # Data access layer (Databricks)
├── views/
│   ├── admin_view.py        # Admin interface
│   └── public_view.py       # Public interface
├── controllers/
│   └── auth.py              # Authentication logic
├── admin.py                 # Streamlit app (Admin)
├── public.py                # Streamlit app (Public)
├── config.py                # Centralized configuration
├── setup_database.py        # Database initialization script
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (DO NOT COMMIT)
└── .env.example             # Environment variables template
```
---
Security
Credentials stored in environment variables via `.env`
`.gitignore` configured to protect sensitive data
Authentication required to access the admin area
Restricted list of authorized email addresses
Clear separation between the public view and the admin panel
---
Getting Started
1. Clone the repository
```bash
git clone https://github.com/YOUR_ORG/sistema-de-escala-conteudo-bol.git
cd sistema-de-escala-conteudo-bol
```
2. Create a virtual environment
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Configure environment variables
Create a `.env` file based on the provided template:
```bash
cp .env.example .env
```
Then fill in your values:
```env
DATABRICKS_SERVER_HOSTNAME=adb-926216925051160.0.azuredatabricks.net
DATABRICKS_HTTP_PATH=sql/protocolv1/o/926216925051160/0325-154030-toes330
DATABRICKS_TOKEN=your_personal_access_token_here
ADMIN_PASSWORD=your_secure_password_here
```
5. Initialize the database
Ensure your `.env` is configured, then run the setup script to create the `escalas_sexta` and `feriados` tables on Databricks:
```bash
python setup_database.py
```
---
Usage
Admin Panel
```bash
streamlit run admin.py
```
Access credentials:
Authorized emails (configured in `config.py`)
Password (configured in `.env`)
Features:
Secure login
Add, edit, and delete Friday shift schedules
Add, edit, and delete holiday entries
🧹 Auto-cleanup — past schedules and holidays are automatically removed on login
---
Public View
```bash
streamlit run public.py
```
Features:
View all Friday shift schedules
View all upcoming holidays
📅 Ascending date order — the next upcoming date always appears at the top
🔴 Visual highlight — the first row (next date) is highlighted in light red for quick identification
🧹 Auto-cleanup — past entries are automatically removed on page load
No login required
Clean and responsive interface
---
CI/CD
This project uses GitHub Actions for continuous integration. The pipeline runs automatically on every push or pull request to `main` / `master`.
Pipeline: `ci.yml`
```yaml
name: CI Pipeline

on:
  push:
    branches: [ "master", "main" ]
  pull_request:
    branches: [ "master", "main" ]

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

      - name: Syntax Check
        run: |
          python -m py_compile admin.py
          python -m py_compile public.py
```
What the pipeline checks:
Step	Description
Checkout	Pulls the latest code from the repository
Set up Python	Configures Python 3.10 on the runner
Install Dependencies	Installs all packages from `requirements.txt`
Syntax Check	Validates `admin.py` and `public.py` for syntax errors
> To add this workflow, save the file as `.github/workflows/ci.yml` in your repository.
---
Deployment on Streamlit Cloud
Push your code to GitHub
Go to share.streamlit.io
Connect your repository
Configure Secrets in the Streamlit Cloud dashboard:
```toml
DATABRICKS_SERVER_HOSTNAME = "adb-926216925051160.0.azuredatabricks.net"
DATABRICKS_HTTP_PATH = "sql/protocolv1/o/926216925051160/0325-154030-toes330"
DATABRICKS_TOKEN = "your_personal_access_token_here"
ADMIN_PASSWORD = "your_secure_password_here"
```
Deploy — Streamlit Cloud handles the rest automatically.
---
Tech Stack
Technology	Purpose
Python 3.10+	Core language
Streamlit	Web framework
Databricks	Cloud data platform
python-dotenv	Environment variable management
pandas	Data manipulation
---
License
Proprietary — © BEMOL S.A. All rights reserved.
