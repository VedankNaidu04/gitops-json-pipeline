# 🚀 GitOps-Inspired JSON Processing Pipeline

> A modular CI pipeline that validates, sanitizes, transforms, verifies, and publishes JSON configuration artifacts using **Python**, **jq**, **GitHub Actions**, and **Amazon S3**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Passing-brightgreen)
![AWS S3](https://img.shields.io/badge/AWS-S3-orange)
![jq](https://img.shields.io/badge/jq-1.8-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📌 Overview

This project demonstrates an automated **CI pipeline** for processing JSON configuration files.

Every push to the repository automatically triggers a GitHub Actions workflow that:

- Validates JSON structure
- Sanitizes configuration data using **jq**
- Transforms the JSON
- Verifies the generated output
- Uploads the final artifact to **Amazon S3**

The project follows a modular architecture where every pipeline stage can be executed independently or as a complete end-to-end workflow.

---

# ✨ Features

- ✅ Modular Python CLI
- ✅ JSON Validation
- ✅ jq-based Sanitization
- ✅ JSON Transformation
- ✅ Output Verification
- ✅ Artifact Generation
- ✅ GitHub Actions CI
- ✅ Amazon S3 Integration
- ✅ IAM Authentication
- ✅ Automated Cloud Upload
- ✅ Public Artifact Publishing

---

# 🏗 Architecture

```text
                    Developer
                        │
                    git push
                        │
                        ▼
              GitHub Repository
                        │
                        ▼
               GitHub Actions CI
      ┌──────────────────────────────┐
      │ Validate JSON                │
      │ Sanitize JSON (jq)           │
      │ Transform JSON               │
      │ Verify Output                │
      └──────────────────────────────┘
                        │
                        ▼
             Upload Artifact to S3
                        │
                        ▼
           Public JSON Configuration
```

---

# ⚙ Pipeline Workflow

```text
input/sample.json
        │
        ▼
Validate (Python)
        │
        ▼
validated.json
        │
        ▼
Sanitize (jq)
        │
        ▼
result.template.json
        │
        ▼
Transform (Python)
        │
        ▼
transformed.json
        │
        ▼
Verify (Python)
        │
        ▼
Amazon S3
```

---

# 📂 Project Structure

```text
gitops-json-pipeline/
│
├── .github/
│   └── workflows/
│       └── pipeline.yml
│
├── artifacts/
│
├── config/
│   └── pipeline-config.json
│
├── filters/
│   ├── sanitize/
│   └── transform/
│
├── input/
│   └── sample.json
│
├── scripts/
│   ├── validate.py
│   ├── sanitize.py
│   ├── transform.py
│   └── verify.py
│
├── run.py
├── requirements.txt
└── README.md
```

---

# 🛠 Technologies

| Category | Technologies |
|-----------|--------------|
| Programming | Python 3.11 |
| JSON Processing | jq |
| CI | GitHub Actions |
| Cloud | Amazon S3 |
| Authentication | AWS IAM |
| Version Control | Git |
| Configuration | JSON |
| Shell | PowerShell / Bash |

---

# 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/VedankNaidu04/gitops-json-pipeline.git
```

Move into the project.

```bash
cd gitops-json-pipeline
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

### Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Install jq.

### Windows

```powershell
winget install jqlang.jq
```

### Ubuntu

```bash
sudo apt install jq
```

---

# ▶ Running the Pipeline

Run individual stages.

```bash
python run.py validate
```

```bash
python run.py sanitize
```

```bash
python run.py transform
```

```bash
python run.py verify
```

Run the complete pipeline.

```bash
python run.py all
```

---

# ☁ GitHub Actions Workflow

The workflow automatically executes on every:

- Push to `main`
- Pull Request targeting `main`

Pipeline stages:

1. Checkout Repository
2. Setup Python
3. Install Dependencies
4. Install jq
5. Validate JSON
6. Sanitize JSON
7. Transform JSON
8. Verify JSON
9. Upload Workflow Artifacts
10. Upload Final Artifact to Amazon S3

---

# ☁ Amazon S3 Integration

After every successful workflow execution, the generated artifact is automatically uploaded to Amazon S3.

Example:

```text
pipeline-artifacts/
└── transformed.json
```

The uploaded JSON can be accessed through the generated S3 Object URL.

---

# 📦 Generated Artifacts

```text
artifacts/
│
├── validated.json
├── result.template.json
└── transformed.json
```

---

# 📄 Sample Output

```text
RUNNING STAGE : Validate JSON
✓ Validation Successful

RUNNING STAGE : Sanitize JSON
✓ remove_nulls
✓ remove_metadata
✓ remove_duplicates
✓ remove_generic_names

RUNNING STAGE : Transform JSON
✓ Transformation Successful

RUNNING STAGE : Verify JSON
✓ Required keys exist
✓ Component IDs unique
✓ Versions valid
✓ Deployment stages present

✓ Uploading Artifact to Amazon S3...

✓ Pipeline Completed Successfully
```

---

# 📸 Screenshots

## Project Structure

```
docs/images/project-structure.png
```

---

## GitHub Actions Workflow

```
docs/images/github-actions-success.png
```

---

## Amazon S3 Upload

```
docs/images/s3-upload.png
```

---

## Public JSON Artifact

```
docs/images/public-json.png
```

---

# 🎯 Skills Demonstrated

- Python Automation
- JSON Processing
- jq Filters
- CLI Development
- Git
- GitHub Actions
- Continuous Integration (CI)
- AWS IAM
- Amazon S3
- YAML Pipelines
- Artifact Management
- Cloud Automation

---

# 📈 Future Improvements

- Docker Containerization
- Kubernetes Deployment
- ArgoCD Integration
- Terraform Infrastructure
- JSON Schema Validation
- Unit & Integration Testing
- Logging & Monitoring
- Versioned S3 Artifacts
- Automated Release Pipeline

---

# 📚 What I Learned

Through this project I gained hands-on experience with:

- Designing modular automation pipelines
- Building reusable Python CLI tools
- Writing jq filters for JSON manipulation
- Creating CI workflows using GitHub Actions
- Managing AWS IAM credentials securely with GitHub Secrets
- Publishing build artifacts to Amazon S3
- Structuring production-style repositories

---

# 👨‍💻 Author

**Vedank Naidu**

- GitHub: https://github.com/VedankNaidu04
- LinkedIn: *(Add your LinkedIn profile URL here)*

---

# 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

⭐ If you found this project interesting, consider giving it a star!