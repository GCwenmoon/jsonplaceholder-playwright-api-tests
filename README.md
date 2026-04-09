# JSONPlaceholder API Automated Test（Playwright + pytest）
A practical **API Test Automation** demo project built with Python, designed to practice testing on the popular training website:

**[JSONPlaceholder](https://jsonplaceholder.typicode.com)**

## 🛠️ Tech Stack

- **Language**: Python 3
- **Testing Framework**: Playwright, pytest
- **Test Site**: [JSONPlaceholder](https://jsonplaceholder.typicode.com)


## Quick Start

1. Create Virtual Environement (Optional)
```bash
python -m venv venv

# Activate venv 
## For Windows
venv\Scripts\activate
## For macOS / Linux
source venv/bin/activate
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

3. Install Playwright Browsers
```bash
playwright install
```

4. Run the scripts
```bash
pytest --headed 
```


## Activate Jenkins
```bash
docker compose up -d
```