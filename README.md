# 🚀 GitOps JSON Pipeline

> A modular Python-based GitOps JSON processing pipeline that validates, sanitizes, transforms, and verifies JSON configuration files using Python, jq, and GitHub Actions.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Passing-brightgreen)
![jq](https://img.shields.io/badge/jq-1.8-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📌 Project Overview

This project demonstrates a complete GitOps-style JSON processing pipeline built with Python and jq.

The pipeline automates:

- ✅ JSON Validation
- ✅ JSON Sanitization
- ✅ JSON Transformation
- ✅ JSON Verification
- ✅ Artifact Generation
- ✅ Continuous Integration using GitHub Actions

The repository follows a modular project structure where every pipeline stage is independent and can be executed individually or as a complete pipeline.

---

# 🏗️ Project Architecture

```
                input/sample.json
                       │
                       ▼
              Validate (Python)
                       │
                       ▼
             validated.json
                       │
                       ▼
             Sanitize (jq Filters)
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
            Pipeline Success
```

---

# 📂 Project Structure

```
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
│   │   ├── remove_nulls.jq
│   │   ├── remove_duplicates.jq
│   │   ├── remove_metadata.jq
│   │   └── remove_generic_names.jq
│   │
│   └── transform/
│       ├── add_fields.jq
│       └── update_values.jq
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

# ⚙️ Technologies Used

- Python 3.11
- jq
- Git
- GitHub Actions
- JSON
- PowerShell

---

# ✨ Features

- Modular pipeline architecture
- Command-line execution
- JSON schema validation
- jq based sanitization
- Automatic artifact generation
- Pipeline orchestration
- CI/CD using GitHub Actions
- Easy to extend

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
py -m venv .venv
```

Activate it.

### Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

Install Python dependencies.

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

Validate

```bash
python run.py validate
```

Sanitize

```bash
python run.py sanitize
```

Transform

```bash
python run.py transform
```

Verify

```bash
python run.py verify
```

Run the complete pipeline.

```bash
python run.py all
```

---

# 📦 Generated Artifacts

The pipeline generates:

```
artifacts/
│
├── validated.json
├── result.template.json
└── transformed.json
```

These files are automatically uploaded by GitHub Actions after every successful workflow execution.

---

# 🤖 GitHub Actions

The repository includes a CI workflow that automatically runs on:

- Push to `main`
- Pull Requests targeting `main`

Workflow stages:

- Checkout Repository
- Setup Python
- Install Dependencies
- Install jq
- Validate
- Sanitize
- Transform
- Verify
- Upload Artifacts

---

# 📸 Screenshots

Add the following screenshots here.

- VS Code Project Structure
- Successful Local Pipeline Run
- GitHub Actions Workflow
- Uploaded Artifacts

Example:

```
images/
├── workflow-success.png
├── project-structure.png
├── terminal-output.png
```

Then reference them:

```markdown
![Workflow](images/workflow-success.png)
```

---

# 🧪 Sample Output

```
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

PIPELINE EXECUTED SUCCESSFULLY
```

---

# 🎯 Learning Objectives

This project demonstrates practical experience with:

- Python scripting
- CLI application development
- JSON processing
- jq filters
- GitOps concepts
- CI/CD pipelines
- GitHub Actions
- Repository organization
- Automation

---

# 🚀 Future Improvements

- JSON Schema validation
- Docker support
- Kubernetes deployment
- Helm charts
- Terraform integration
- ArgoCD GitOps deployment
- Unit tests
- Logging
- Configuration profiles

---

# 👨‍💻 Author

**Vedank Naidu**

GitHub:

https://github.com/VedankNaidu04

---

# 📄 License

This project is licensed under the MIT License.

See the LICENSE file for details.