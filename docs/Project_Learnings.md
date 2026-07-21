# GitOps JSON Processing Pipeline
## Project Learnings & Complete Documentation
### Phase 1

Author: Vedank Naidu

---

# Table of Contents

1. Introduction
2. Project Objective
3. Why I Built This Project
4. Problem Statement
5. What is GitOps?
6. Why JSON?
7. Why Python?
8. Why jq?
9. Why GitHub Actions?
10. Technologies Used
11. Overall Project Architecture
12. Pipeline Overview
13. Current Project Scope (Phase 1)

---

# 1. Introduction

This project is a real-world DevOps inspired GitOps JSON Processing Pipeline built using Python, jq and GitHub Actions.

Instead of creating a simple "Hello World" DevOps project, I wanted to build something that resembles how enterprise CI/CD pipelines process configuration files before deployment.

Many modern applications, cloud platforms, Infrastructure-as-Code tools, Kubernetes deployments, Terraform configurations, API gateways, cloud services and deployment pipelines use JSON as a configuration language.

Before these JSON files are consumed by applications, they usually undergo multiple processing stages such as validation, sanitization, transformation and verification.

This project simulates exactly that workflow.

The pipeline takes an input JSON file and processes it through multiple automated stages.

Every stage performs a specific responsibility.

The output of one stage becomes the input of the next stage.

Finally, a verified production-ready JSON artifact is produced.

This project is completely automated using GitHub Actions.

---

# 2. Project Objective

The objective of this project is to design and implement a modular JSON processing pipeline that follows DevOps and GitOps principles.

Instead of writing one large Python script that performs every task, the project separates the processing into multiple independent stages.

Each stage performs exactly one responsibility.

Validate

↓

Sanitize

↓

Transform

↓

Verify

This design follows one of the most important software engineering principles:

Single Responsibility Principle (SRP)

Each script has exactly one job.

This makes the project

• easier to understand

• easier to debug

• easier to test

• easier to extend

• closer to real production systems

---

# 3. Why I Built This Project

Initially, I planned to build a simple Hello World application using GitHub Actions.

However, I quickly realized that such projects do not demonstrate real DevOps skills.

I wanted to build something that shows

• automation

• scripting

• CI/CD

• JSON processing

• configuration management

• pipeline orchestration

• modular architecture

• artifact management

• GitHub Actions

Instead of creating an application, I chose to create a reusable processing pipeline.

This project resembles how many organizations process

Deployment Templates

Configuration Files

Infrastructure Definitions

Cloud Resources

Kubernetes Manifests

API Specifications

Policy Files

before deploying them.

The project can later be extended to upload processed artifacts to AWS S3 or deploy them to an EC2 instance.

Therefore this project is not just a scripting exercise.

It is the foundation of a complete DevOps workflow.

---

# 4. Problem Statement

Imagine an organization with hundreds of developers.

Every developer creates JSON configuration files.

These files contain

Application configurations

Deployment settings

Server information

Metadata

Temporary values

Debug values

Duplicate entries

Testing information

Before these configuration files can be deployed into production, they need to be cleaned and validated.

Doing this manually is

Time consuming

Error prone

Not scalable

Not reliable

The solution is to automate the entire process.

This project automates that workflow.

Instead of manually editing JSON files, the pipeline processes them automatically.

The final output is production-ready.

---

# 5. What is GitOps?

GitOps is a modern DevOps practice where Git becomes the single source of truth.

Instead of making manual changes on servers, every change is first committed to Git.

Git then automatically triggers a pipeline.

The pipeline validates the changes.

If validation succeeds, the changes are processed and eventually deployed.

Traditional Workflow

Developer

↓

Server

↓

Manual Changes

↓

Errors

↓

Inconsistency

GitOps Workflow

Developer

↓

Git Repository

↓

GitHub Actions

↓

Pipeline

↓

Validated Artifact

↓

Deployment

GitOps provides

Consistency

Automation

Traceability

Version Control

Rollback Capability

Auditability

This project follows GitOps principles because every pipeline execution begins with a Git commit.

---

# 6. Why JSON?

JSON (JavaScript Object Notation) is one of the most widely used data interchange formats in software engineering.

Almost every modern application uses JSON.

Examples include

REST APIs

Cloud Configurations

AWS Services

Terraform

Azure

Google Cloud

Docker APIs

Kubernetes APIs

OpenAPI Specifications

GitHub APIs

GitLab APIs

CI/CD Pipelines

Application Configurations

JSON is

Human readable

Machine readable

Language independent

Easy to parse

Easy to validate

Easy to transform

Easy to exchange between systems

Since DevOps engineers constantly work with configuration files, JSON processing is an extremely valuable skill.

---

# 7. Why Python?

Python is one of the most popular scripting languages in DevOps.

Reasons include

Simple syntax

Excellent standard library

Cross platform

Fast development

Large ecosystem

Easy automation

Python is commonly used for

Infrastructure automation

Cloud automation

AWS scripting

Azure scripting

Log analysis

Deployment automation

Configuration management

Testing

CI/CD scripting

Pipeline development

In this project Python is responsible for

Reading JSON

Validating data

Managing pipeline execution

Calling jq

Generating reports

Producing artifacts

Handling errors

---

# 8. Why jq?

jq is a lightweight command-line JSON processor.

It is often called the "sed" or "awk" of JSON.

Instead of writing hundreds of lines of Python code to manipulate JSON structures, jq allows complex transformations using small filter expressions.

Example

Remove metadata

Remove duplicate objects

Delete temporary fields

Rename keys

Transform arrays

Filter nested objects

In this project jq performs the sanitization stage.

The advantages are

Very fast

Very lightweight

Easy to integrate

Designed specifically for JSON

Commonly used in DevOps pipelines

Learning jq is extremely valuable because it is frequently used alongside

AWS CLI

Azure CLI

Kubernetes

Docker

Terraform

GitHub Actions

Linux automation

---

# 9. Why GitHub Actions?

GitHub Actions is GitHub's built-in CI/CD platform.

It allows automation directly inside a Git repository.

Instead of manually executing scripts,

GitHub Actions automatically runs the pipeline whenever code is pushed.

Benefits include

Continuous Integration

Continuous Delivery

Automation

Repeatability

Version controlled workflows

Cloud hosted runners

Artifact storage

Workflow visualization

Pipeline logs

Job dependency management

In this project GitHub Actions performs

Checkout Repository

↓

Install Python

↓

Install jq

↓

Run Validation

↓

Run Sanitization

↓

Run Transformation

↓

Run Verification

↓

Upload Artifacts

Everything happens automatically.

---

# 10. Technologies Used

## Python

Purpose

Pipeline orchestration

Automation

JSON processing

Error handling

CLI development

Skills Learned

Functions

Modules

JSON library

Subprocess

Argument parsing

File handling

Configuration driven programming

------------------------------------------------------------

## JSON

Purpose

Input configuration

Pipeline configuration

Intermediate artifacts

Output artifacts

Skills Learned

Objects

Arrays

Nested structures

Validation

Transformation

Parsing

------------------------------------------------------------

## jq

Purpose

JSON sanitization

Removing duplicate entries

Removing metadata

Cleaning objects

Generating template JSON

Skills Learned

jq filters

walk()

del()

unique_by()

JSON traversal

------------------------------------------------------------

## Git

Purpose

Version control

Tracking changes

Collaboration

Rollback

Skills Learned

Commit

Push

Branching

History

Source control

------------------------------------------------------------

## GitHub

Purpose

Repository hosting

Pipeline hosting

Artifact storage

Collaboration

Skills Learned

Repository management

Actions

Workflow execution

Artifact management

------------------------------------------------------------

## GitHub Actions

Purpose

Continuous Integration

Pipeline execution

Automation

Skills Learned

Jobs

Steps

Artifacts

Dependencies

Workflow triggers

Ubuntu runners

------------------------------------------------------------

## YAML

Purpose

Workflow definition

Pipeline configuration

Skills Learned

Jobs

Steps

Actions

Variables

Dependencies

------------------------------------------------------------

## AWS (Future Scope)

Purpose

Artifact storage

Deployment

Infrastructure

Services planned

Amazon S3

Amazon EC2

IAM

OIDC Authentication

---

# 11. Overall Project Architecture

The entire project follows a modular pipeline architecture.

                     Git Push
                         │
                         ▼
                GitHub Repository
                         │
                         ▼
                GitHub Actions
                         │
      ┌─────────────────────────────────┐
      │                                 │
      ▼                                 ▼
 Validate JSON                 Upload Artifact
      │
      ▼
 Sanitize JSON
      │
      ▼
 Transform JSON
      │
      ▼
 Verify JSON
      │
      ▼
 Final Artifact
      │
      ▼
 Future
 AWS S3 / EC2

Every stage is completely independent.

This modular architecture makes the project easier to maintain.

---

# 12. Pipeline Overview

The pipeline consists of four independent stages.

Stage 1

Validate JSON

Purpose

Ensures that the input JSON is syntactically correct and contains all required root keys.

Output

validated.json

------------------------------------------------------------

Stage 2

Sanitize JSON

Purpose

Remove duplicate entries

Remove metadata

Remove temporary values

Remove null values

Generate reusable template JSON

Output

result.template.json

------------------------------------------------------------

Stage 3

Transform JSON

Purpose

Sort components

Sort servers

Generate summary

Attach pipeline metadata

Output

transformed.json

------------------------------------------------------------

Stage 4

Verify JSON

Purpose

Verify semantic versions

Check duplicate component IDs

Validate deployment stages

Confirm production readiness

Output

Verification Report

---

# 13. Current Project Scope (Phase 1)

Completed

✓ Python based processing pipeline

✓ jq integration

✓ Configuration driven architecture

✓ GitHub Actions pipeline

✓ Artifact generation

✓ Multi-stage processing

✓ Verification

✓ Modular project structure

Upcoming (Phase 2)

AWS S3 integration

AWS EC2 deployment

OIDC authentication

Automatic artifact upload

Pipeline badges

Advanced logging

Secrets management

Docker containerization

Monitoring

Notifications

--------------------------------------------------------------------------------------------------

# Part 2A
# Complete Project Structure & File Explanation

---

# 14. Project Folder Structure

The project follows a modular folder structure.

Instead of placing every file in one directory, the project separates different responsibilities into dedicated folders.

This makes the project

• Easier to understand

• Easier to maintain

• Easier to scale

• Easier to debug

• Similar to real enterprise projects

The folder structure is shown below.

```

gitops-json-pipeline/
│
├── .github/
│ └── workflows/
│ └── pipeline.yml
│
├── artifacts/
│ ├── validated.json
│ ├── result.template.json
│ └── transformed.json
│
├── config/
│ └── pipeline-config.json
│
├── filters/
│ └── sanitize/
│ ├── remove_duplicates.jq
│ ├── remove_generic_names.jq
│ ├── remove_metadata.jq
│ ├── remove_nulls.jq
│ ├── add_fields.jq
│ └── update_values.jq
│
├── input/
│ └── sample.json
│
├── scripts/
│ ├── validate.py
│ ├── sanitize.py
│ ├── transform.py
│ └── verify.py
│
├── requirements.txt
├── run.py
├── README.md
└── Project_Learnings.md

```

Every folder has a specific responsibility.

This is one of the most important characteristics of maintainable software.

---

# 15. Folder by Folder Explanation

---

## 15.1 .github/

Purpose

Stores all GitHub specific configurations.

Inside this folder we have

```

workflows/

```

GitHub automatically scans this folder.

Whenever code is pushed, GitHub looks for YAML workflow files inside this directory.

Our pipeline is stored here.

Without this folder, GitHub Actions would never execute.

---

## 15.2 workflows/

Contains

```

pipeline.yml

```

This file defines our Continuous Integration pipeline.

Instead of manually executing

```

python run.py all

```

GitHub executes it automatically whenever code is pushed.

This file describes

• Jobs

• Dependencies

• Steps

• Python installation

• jq installation

• Artifact uploads

• Artifact downloads

Think of this file as the "brain" of the automation.

---

## 15.3 artifacts/

Purpose

Stores every intermediate output produced by the pipeline.

Pipeline execution

```

sample.json

↓

validated.json

↓

result.template.json

↓

transformed.json

```

Each stage reads the previous artifact.

This is exactly how many enterprise CI/CD pipelines operate.

Advantages

• Easy debugging

• Easy rollback

• Easy inspection

• Independent stages

Example

If sanitization fails,

we already have

```

validated.json

```

We do not need to validate again.

This saves time.

---

## 15.4 config/

Contains

```

pipeline-config.json

```

This is one of the most important files in the project.

Instead of hardcoding values inside Python,

all configurable settings are stored here.

This follows a software engineering principle called

Configuration Driven Development.

Instead of

```

if version == "1.0"

```

we store

```

{
"version":"1.0"
}

```

Advantages

Change behavior

↓

without

↓

changing code

Benefits

• Cleaner code

• Easier maintenance

• Easier deployment

• Better scalability

---

## 15.5 filters/

Contains every jq filter.

Instead of writing hundreds of lines of Python,

jq specializes in manipulating JSON.

Each filter performs exactly one task.

Example

```

remove_nulls.jq

```

only removes null values.

It does not remove duplicates.

Similarly,

```

remove_duplicates.jq

```

does not remove metadata.

Each filter has exactly one responsibility.

Again,

this follows the

Single Responsibility Principle.

---

## 15.6 input/

Contains

```

sample.json

```

This is the source JSON.

Every pipeline execution begins here.

Future versions of this project can process

multiple JSON files,

or automatically process every JSON inside this directory.

---

## 15.7 scripts/

Contains every Python stage.

Instead of one

1500 line script,

we have

```

validate.py

sanitize.py

transform.py

verify.py

```

Each file performs exactly one stage.

Advantages

Smaller code

Independent execution

Easy testing

Easy debugging

Better readability

Enterprise style architecture

---

## 15.8 requirements.txt

Lists every Python dependency.

Instead of manually installing packages,

GitHub Actions executes

```

pip install -r requirements.txt

```

This guarantees

every developer,

every machine,

every GitHub runner

installs exactly the same dependencies.

---

## 15.9 run.py

This file is the orchestrator.

It does not process JSON.

Instead,

it coordinates every stage.

Think of it as a project manager.

It decides

Which script to execute

When to execute it

In what order

Which configuration to pass

Every pipeline begins here.

---

# 16. pipeline-config.json

This is the heart of the project.
Instead of scattering configuration across multiple files, everything is centralized.

```
pipeline-config.json
```
stores
Pipeline information
Validation rules
Sanitization filters
Transformation settings
Verification rules
Paths
Input files
Output files
Future cloud settings
This makes the project extremely flexible.

---

# 17. Why Configuration Driven Development?

Suppose tomorrow
the input JSON changes.
Without configuration
You modify Python.
Re-test Python.
Commit Python.
Deploy Python.
With configuration
Only edit
```
pipeline-config.json
```
Done.
No Python code changes.
This is one of the biggest improvements we made during Phase 1.
---

# 18. Understanding pipeline-config.json
Our configuration file is divided into logical sections.
Example
```
{
"pipeline": {},
"paths": {},
"validation": {},
"sanitize": {},
"transform": {},
"verification": {}
}

```

Each section has a purpose.

---

## 18.1 Pipeline Section

Contains

Project name

Pipeline version

Description

Example

```

"pipeline":

{

"name":"GitOps JSON Pipeline",

"version":"1.0"

}

```

Instead of writing

```

processed_by="GitOps JSON Pipeline"

```

inside Python,

the script reads

```

CONFIG["pipeline"]["name"]

```

Advantages

Easy branding

Easy versioning

Reusable pipeline

---

## 18.2 Paths Section

Stores

Input location

Artifact directory

Output filenames

Instead of writing

```

artifacts/result.template.json

```

inside multiple Python files,

everything comes from one location.

If tomorrow

artifacts/

becomes

```

build/

```

only one configuration file changes.

---

## 18.3 Validation Section

Contains

Required root keys.

Example

```

"required_root_keys":

[

"project",

"components",

"deployment"

]

```

validate.py reads this section.

Therefore,

adding another required key

requires zero Python modifications.

---

## 18.4 Sanitize Section

Contains

Every jq filter.

Example

```

remove_nulls.jq

remove_duplicates.jq

remove_metadata.jq

remove_generic_names.jq

```

sanitize.py simply loops through the list.

Advantages

Want another filter?

Just add

```

remove_comments.jq

```

to the configuration.

No Python changes.

---

## 18.5 Transform Section

Controls

Sorting

Summary generation

Pipeline metadata

Example

```

"sort":

{

"components":true,

"servers":true

}

```

Tomorrow,

if sorting is unnecessary,

simply change

```

true

↓

false

```

No Python modifications.

---

## 18.6 Verification Section

Contains

Semantic Version Regex

Duplicate checks

Deployment validation

Required keys

Example

```

"semantic_version_regex":

"^\\d+\\.\\d+\\.\\d+$"

```

Instead of hardcoding regex inside verify.py,

everything comes from configuration.

---

# 19. Why is this Architecture Professional?

Many beginner projects contain

```

main.py

```

with

1500+

lines of code.

Everything is mixed together.

Validation

Transformation

Configuration

Logging

Execution

Error handling

Output

This becomes difficult to maintain.

Our project separates concerns.

Configuration

↓

pipeline-config.json

Execution

↓

run.py

Validation

↓

validate.py

Cleaning

↓

sanitize.py

Transformation

↓

transform.py

Verification

↓

verify.py

Automation

↓

pipeline.yml

Every file has exactly one purpose.

This is the same philosophy followed in enterprise software.

---

# 20. Software Engineering Principles Used

Our project unintentionally follows many software engineering principles.

Single Responsibility Principle

Each script performs one task.

Configuration Driven Development

Behavior comes from JSON.

Modular Design

Separate scripts.

Reusable Components

Reusable jq filters.

Loose Coupling

Scripts communicate using artifacts.

High Cohesion

Each file contains related logic only.

Pipeline Architecture

Output of one stage becomes input of the next.

Automation First

Everything can execute automatically.

CI/CD Friendly

Designed for GitHub Actions.

Cloud Ready

Easy future integration with AWS.

---

# Summary of Part 2A

In this section we learned
✓ Complete folder structure
✓ Why folders exist
✓ Why files are separated
✓ Configuration Driven Development
✓ pipeline-config.json architecture
✓ Software Engineering principles
✓ Enterprise project organization

The next part will explain every Python script in detail, beginning with `run.py`, followed by `validate.py` and `sanitize.py`. We'll cover each function, why it exists, how it works, and how it interacts with the rest of the pipeline.

# Part 2B
# Detailed Code Walkthrough
## Understanding the Core Python Scripts

---

# 21. Why Multiple Python Scripts?

One of the first design decisions made while building this project was **not** to put everything into one Python file.

Initially, it might seem easier to write one script that:

- Reads the JSON
- Cleans the JSON
- Modifies the JSON
- Verifies the JSON
- Generates the final artifact

However, this approach quickly becomes difficult to maintain.

Imagine the project after a few months.

The single file may grow to

```
1500+
2000+
3000+
Lines of Code
```

Finding bugs becomes difficult.

Testing individual features becomes difficult.

Adding new functionality becomes risky.

Instead, the project was divided into multiple scripts.

Each script performs one responsibility.

```
run.py

↓

validate.py

↓

sanitize.py

↓

transform.py

↓

verify.py
```

This follows one of the most important principles of software engineering.

**Single Responsibility Principle (SRP)**

A module should have one reason to change.

---

# 22. Understanding run.py

run.py is arguably the most important file in the project.

It does **not** process JSON.

Instead,

it coordinates the entire pipeline.

Think of it as a Project Manager.

It tells every other script

"When should you execute?"

and

"What input should you use?"

Without run.py,

the user would need to manually execute

```
python scripts/validate.py

python scripts/sanitize.py

python scripts/transform.py

python scripts/verify.py
```

This is error-prone.

Instead,

the user simply executes

```
python run.py all
```

Everything else happens automatically.

---

# 23. Why Use argparse?

The first thing run.py does is

```
import argparse
```

argparse is Python's built-in command line argument parser.

Instead of hardcoding

```
run.py always executes everything
```

the user can choose

```
python run.py validate

python run.py sanitize

python run.py transform

python run.py verify

python run.py all
```

Advantages

• Flexible

• Reusable

• Professional CLI

• Easy automation

Most DevOps tools

kubectl

terraform

ansible

docker

aws cli

all use command line arguments.

Using argparse makes our project behave like professional DevOps software.

---

# 24. Why Use subprocess?

Inside run.py we use

```
subprocess.run()
```

Instead of importing

```
validate.py
```

directly.

Why?

Because every stage should behave like an independent application.

Each script can run independently.

Example

```
python scripts/verify.py

python scripts/sanitize.py

python scripts/transform.py
```

This is extremely useful.

Suppose validation succeeds,

but transformation fails.

We can simply rerun

```
python run.py transform
```

instead of executing the entire pipeline again.

This modularity makes debugging much easier.

---

# 25. Why Use sys.executable?

Instead of writing

```
python
```

inside subprocess,

we use

```
sys.executable
```

Example

```
PYTHON = sys.executable
```

Why?

Different systems may contain

Python 3.10

Python 3.11

Python 3.12

Python inside a virtual environment

Using

```
sys.executable
```

guarantees that subprocess uses the exact same Python interpreter that launched run.py.

This avoids many environment related problems.

---

# 26. Understanding execute()

Every stage eventually calls

```
execute()
```

Purpose

Execute one pipeline stage.

Display status.

Stop execution if something fails.

Workflow

```
Stage

↓

Execute Python Script

↓

Success?

↓

Yes

↓

Continue

↓

No

↓

Stop Pipeline
```

This is exactly how CI/CD pipelines behave.

If validation fails,

there is no point continuing.

Therefore,

the pipeline immediately exits.

---

# 27. Pipeline Functions

Inside run.py we have

```
validate()

sanitize()

transform()

verify()
```

Notice something interesting.

These functions do **not**

Validate JSON.

Sanitize JSON.

Transform JSON.

Verify JSON.

Instead,

they simply call the corresponding scripts.

Example

```
validate()

↓

scripts/validate.py
```

This separation keeps run.py extremely small.

Its only responsibility is orchestration.

---

# 28. Understanding pipeline()

The pipeline() function is simply

```
validate()

↓

sanitize()

↓

transform()

↓

verify()
```

in sequence.

This creates a complete processing pipeline.

Every stage depends on the previous stage.

```
sample.json

↓

validated.json

↓

result.template.json

↓

transformed.json

↓

Verification Report
```

Notice that every output becomes the next input.

This design is extremely common in

CI/CD

ETL

Data Engineering

Cloud Pipelines

---

# 29. Why Does run.py Never Read JSON?

This is an important design decision.

run.py knows nothing about JSON.

It does not

Open files

Read objects

Modify data

Delete metadata

Verify versions

Instead,

it only executes programs.

This keeps the orchestration layer completely independent.

---

# 30. Understanding validate.py

Validation is the first processing stage.

Its responsibility is very simple.

Determine whether the input JSON is suitable for further processing.

If validation fails,

the remaining stages should never execute.

---

# 31. Why Validate First?

Suppose the JSON is malformed.

Example

```
{
"name":"server"
```

Notice

The closing brace is missing.

Every later stage would fail.

Instead,

validation detects the problem immediately.

Advantages

Fast failure

Better debugging

Cleaner pipeline

Less wasted execution time

---

# 32. Reading JSON

validate.py begins by reading

```
sample.json
```

using

```
json.load()
```

Python converts

```
JSON

↓

Python Dictionary
```

This allows Python to inspect

keys

arrays

objects

values

---

# 33. Required Root Keys

The project requires

```
project

components

deployment
```

These are stored inside

```
pipeline-config.json
```

instead of Python.

Why?

Tomorrow,

suppose another key becomes mandatory.

```
servers
```

Without configuration

Modify Python.

With configuration

Modify JSON.

No code changes.

This is configuration-driven development.

---

# 34. Why Copy Instead of Modify?

If validation succeeds,

we simply copy

```
sample.json

↓

validated.json
```

Why not modify it?

Because validation should never change data.

Its only responsibility is verification.

Keeping validation read-only makes debugging much easier.

---

# 35. Understanding sanitize.py

After validation,

the pipeline moves to sanitization.

Purpose

Remove unwanted information.

Prepare a clean template.

Generate production-ready data.

---

# 36. Why jq Instead of Python?

Everything inside sanitize.py eventually calls

```
jq
```

through

```
subprocess.run()
```

Instead of writing

300

or

400

lines of Python.

Why?

Because jq is specifically designed for JSON manipulation.

Tasks like

Delete keys

Remove duplicates

Traverse nested objects

Filter arrays

are dramatically simpler in jq.

---

# 37. FILTERS List

sanitize.py contains a list

```
FILTERS
```

Example

```
remove_nulls.jq

↓

remove_metadata.jq

↓

remove_duplicates.jq

↓

remove_generic_names.jq
```

Instead of hardcoding every operation,

the script simply loops through this list.

Advantages

Easy extension.

Suppose tomorrow

we create

```
remove_comments.jq
```

Simply add it to the configuration.

No Python modifications.

---

# 38. Why Temporary Files?

Each jq filter produces new JSON.

Instead of modifying the original file,

sanitize.py creates temporary files.

Workflow

```
validated.json

↓

temp1.json

↓

temp2.json

↓

temp3.json

↓

temp4.json

↓

result.template.json
```

This approach has several advantages.

Each filter receives a clean input.

Intermediate results can be inspected.

Failures become easier to debug.

---

# 39. Why subprocess.run() Again?

sanitize.py executes

```
jq
```

using

```
subprocess.run()
```

instead of implementing jq inside Python.

Reason

jq is an external program.

Python simply launches it.

This is exactly how many automation tools work.

Python orchestrates.

Other tools perform specialized tasks.

---

# 40. Error Handling

Suppose jq encounters

Invalid syntax

Invalid JSON

Missing filter

Execution failure

subprocess immediately returns a non-zero exit code.

sanitize.py captures this.

Displays an error.

Stops execution.

This prevents corrupted JSON from reaching the next stage.

---

# 41. Final Output of sanitize.py

After all filters complete,

the final temporary file is copied to

```
artifacts/result.template.json
```

This becomes the official output.

Every later stage uses this file.

Notice once again

Input

↓

Processing

↓

Artifact

Every stage produces an artifact.

This is exactly how GitHub Actions workflows pass data between jobs.

---

# Summary of Part 2B

In this section we learned

✓ Why multiple Python scripts exist

✓ Why run.py is the orchestrator

✓ Why argparse was chosen

✓ Why subprocess.run() is used

✓ Why sys.executable improves portability

✓ Why validate.py is read-only

✓ Why sanitization is delegated to jq

✓ Why temporary files are used

✓ How artifacts flow through the pipeline

✓ The software engineering principles behind the implementation

In the next section (Part 2C), we will examine `transform.py`, `verify.py`, and every jq filter in detail, explaining how they work internally and why each one is important.

-------------------------------------------------------

# Part 2C
# Understanding transform.py, verify.py & jq Filters

---

# 42. Understanding transform.py

Once the JSON has been validated and sanitized, it reaches the transformation stage.

Unlike validation or sanitization, transformation **does not remove incorrect data**.

Instead, it improves and enriches the JSON.

Think of it like this:

Input JSON

↓

Clean JSON

↓

Enhanced JSON

The purpose of this stage is to prepare the JSON for production.

---

# 43. Why Do We Need Transformation?

Suppose we have the following JSON.

```json
{
    "components": [...],
    "servers": [...]
}
```

It works perfectly.

But imagine another application wants to know

- How many components exist?
- How many servers exist?
- Which environment is this?
- Which pipeline generated this file?

Without transformation, every application must calculate this information itself.

Instead,

our pipeline generates these values once.

Every downstream application can reuse them.

---

# 44. Sorting Data

One responsibility of transform.py is sorting.

Example

Before

```
Component-5

Component-2

Component-1
```

After

```
Component-1

Component-2

Component-5
```

Why?

Because predictable ordering is extremely important.

Benefits

• Easier Git comparisons

• Easier debugging

• Consistent output

• Cleaner pull requests

Imagine two developers generating JSON.

Without sorting,

their output order may differ.

Git would report many unnecessary changes.

Sorting eliminates this problem.

---

# 45. Why Sort Servers?

The same idea applies to servers.

Instead of

```
Server-C

Server-A

Server-B
```

we produce

```
Server-A

Server-B

Server-C
```

This creates deterministic output.

Deterministic means

"The same input always produces the same output."

This is a very important property in CI/CD pipelines.

---

# 46. Generating Summary

Our pipeline automatically creates

```
summary
```

Example

```json
"summary":

{

"component_count":12,

"server_count":5,

"environment":"production"

}
```

Why generate this?

Imagine opening a JSON containing

10,000 lines.

Instead of manually counting components,

the summary provides instant information.

This improves readability.

---

# 47. Pipeline Metadata

Another important addition is

```
pipeline
```

Example

```json
"pipeline"

{

"processed_by":"GitOps JSON Pipeline",

"version":"1.0",

"stage":"transform",

"status":"SUCCESS"

}
```

Why?

Suppose someone receives this JSON six months later.

Questions arise.

Who generated it?

Which pipeline?

Which version?

Was processing successful?

Pipeline metadata answers all these questions.

This is common in enterprise systems.

---

# 48. Configuration Driven Transformation

Instead of hardcoding

```
Sort Components

Sort Servers

Generate Summary

Generate Metadata
```

inside Python,

our script reads

```
pipeline-config.json
```

Example

```
sort

↓

summary

↓

pipeline_metadata
```

Changing pipeline behaviour requires changing configuration only.

No Python modifications.

---

# 49. Understanding verify.py

Verification is the final quality gate.

Notice something interesting.

Validation

and

Verification

are different.

Validation asks

"Can this JSON be processed?"

Verification asks

"Should this JSON be trusted?"

This distinction is extremely important.

---

# 50. Validation vs Verification

Validation

Checks

Is JSON valid?

Are required keys present?

Is syntax correct?

Verification

Checks

Versions

Duplicates

Deployment information

Business rules

Think of validation as checking whether a document exists.

Verification checks whether the document is correct.

---

# 51. Why Verify at the End?

Verification happens after transformation.

Reason

Transformation may accidentally introduce errors.

Verification guarantees

The final artifact is safe.

Only verified artifacts should reach production.

This follows the same philosophy as

Testing

↓

Deployment

used by CI/CD systems.

---

# 52. Semantic Version Validation

Our project validates

```
1.0.0

2.5.7

10.15.3
```

using Regular Expressions.

Pattern

```
^\d+\.\d+\.\d+$
```

Meaning

Major

.

Minor

.

Patch

Example

Valid

```
1.0.0

5.12.9
```

Invalid

```
v1

1

latest

2.4

release-1
```

Version consistency is important because software deployment often depends on versions.

---

# 53. Duplicate Component Verification

Earlier,

sanitize.py removes duplicate objects.

verify.py performs one final check.

Imagine

```
Component-101

Component-101
```

Both somehow survive.

Verification catches this.

Pipeline immediately fails.

This prevents incorrect deployments.

---

# 54. Deployment Verification

Our pipeline also checks

```
deployment

↓

stages
```

Why?

Suppose

```
deployment

{

"stages":[]
}
```

There are no deployment stages.

Such configuration is incomplete.

Instead of producing an invalid artifact,

verification stops the pipeline.

---

# 55. Verification Report

Instead of silently succeeding,

verify.py generates a report.

Example

```
✓ Required Keys

✓ Component IDs

✓ Semantic Versions

✓ Deployment Stages
```

or

```
✗ Duplicate Components

✗ Invalid Version

✗ Missing Deployment Stage
```

This provides immediate feedback.

---

# 56. Why Does the Pipeline Stop?

Suppose verification detects

Duplicate IDs.

Continuing would create an unreliable artifact.

Therefore

```
sys.exit(1)
```

immediately stops execution.

GitHub Actions interprets this as

Job Failed

Exactly how professional CI systems behave.

---

# 57. Understanding jq Filters

jq is one of the most important technologies used in this project.

Instead of writing large Python functions,

each jq file performs one tiny task.

Think of them as micro-programs.

Each filter has exactly one responsibility.

---

# 58. remove_nulls.jq

Purpose

Remove every field containing

```
null
```

Example

Before

```json
{

"name":"Server",

"owner":null

}
```

After

```json
{

"name":"Server"

}
```

Advantages

Cleaner JSON

Smaller files

Less unnecessary information

---

# 59. remove_metadata.jq

Purpose

Delete

```
metadata

audit
```

Why?

Metadata is useful during development.

Production systems usually do not require it.

Removing unnecessary metadata reduces clutter.

---

# 60. remove_duplicates.jq

Purpose

Remove duplicate components.

Example

Before

```
Server-A

Server-A

Server-B
```

After

```
Server-A

Server-B
```

Duplicate data causes

Confusion

Incorrect counts

Incorrect deployments

Verification errors

Therefore duplicates are removed early.

---

# 61. remove_generic_names.jq

Purpose

Delete

```
debug

temp

placeholder

dummy

sample

test
```

These values are common during development.

They should never appear inside production artifacts.

Removing them creates cleaner output.

---

# 62. Why Multiple jq Files?

Instead of writing

```
remove_everything.jq
```

we created

```
remove_nulls.jq

remove_metadata.jq

remove_duplicates.jq

remove_generic_names.jq
```

Advantages

Easy debugging

Easy maintenance

Easy testing

Reusable filters

Single Responsibility Principle

Professional architecture

---

# 63. Pipeline Data Flow

The complete data flow looks like this.

```
sample.json

↓

validate.py

↓

validated.json

↓

sanitize.py

↓

jq Filter 1

↓

jq Filter 2

↓

jq Filter 3

↓

jq Filter 4

↓

result.template.json

↓

transform.py

↓

transformed.json

↓

verify.py

↓

Verification Report

↓

Pipeline Success
```

Notice that every stage produces a new artifact.

The original file is never modified.

---

# 64. Design Philosophy

The project intentionally follows several important software engineering principles.

Single Responsibility Principle

Every script has one job.

Configuration Driven Development

Configuration is separated from code.

Pipeline Architecture

Each stage performs one task.

Artifact Based Communication

Stages exchange files instead of sharing memory.

Loose Coupling

Scripts know very little about one another.

High Cohesion

Each file contains closely related logic.

Automation First

Everything can execute without manual intervention.

---

# 65. Why This Project Is Resume Worthy

Unlike beginner projects,

this project demonstrates

✓ Python scripting

✓ JSON processing

✓ jq

✓ Git

✓ GitHub

✓ GitHub Actions

✓ CI/CD

✓ Artifact management

✓ Pipeline orchestration

✓ Configuration driven architecture

✓ Modular software design

✓ Error handling

✓ CLI development

✓ Enterprise project structure

Most importantly,

it demonstrates understanding of DevOps workflows rather than simply using a DevOps tool.

---

# Summary of Part 2C

In this section we learned

✓ Why transformation exists

✓ Why deterministic output is important

✓ How summary generation works

✓ Why pipeline metadata is useful

✓ Difference between validation and verification

✓ Semantic version validation

✓ Duplicate detection

✓ Deployment verification

✓ Purpose of every jq filter

✓ Complete data flow

✓ Enterprise software engineering principles

This concludes the technical implementation explanation of **Phase 1**. The project is now documented from the architectural level down to the implementation details, including the reasoning behind every major design decision.

----------------------------------------------------

# Part 3
# Understanding GitHub Actions & CI/CD

---

# 66. What is CI/CD?

Before understanding GitHub Actions, we first need to understand CI/CD.

CI/CD is one of the most important concepts in DevOps.

CI stands for

Continuous Integration

CD stands for

Continuous Delivery
(or Continuous Deployment)

Almost every modern software company uses some form of CI/CD.

Examples include

Google

Amazon

Microsoft

Netflix

Meta

Adobe

Oracle

Salesforce

Instead of manually building and testing software, everything is automated.

---

# 67. What is Continuous Integration (CI)?

Imagine a team of 20 developers.

Every developer writes code.

Without CI,

Developer A pushes code.

Developer B pushes code.

Developer C pushes code.

Nobody knows whether the application still works.

Eventually,

someone manually tests everything.

Finding bugs becomes difficult.

Continuous Integration solves this problem.

Whenever code is pushed,

the pipeline automatically

• Downloads the latest code

• Builds the project

• Runs validation

• Runs testing

• Reports success or failure

Every commit is verified automatically.

This gives developers immediate feedback.

---

# 68. What is Continuous Delivery (CD)?

Once CI succeeds,

the next step is delivery.

Delivery means

Prepare the application

Generate artifacts

Package outputs

Upload results

Ready for deployment

Notice something important.

Continuous Delivery does NOT necessarily deploy automatically.

Instead,

it prepares everything for deployment.

---

# 69. Continuous Deployment

Continuous Deployment goes one step further.

Instead of stopping after successful testing,

the application is automatically deployed.

Example

Developer pushes code

↓

Pipeline executes

↓

Tests pass

↓

Deploy to AWS

↓

Application becomes live

Our project currently stops before deployment.

Deployment to AWS EC2 will be implemented during Phase 2.

---

# 70. Where Does GitHub Actions Fit?

GitHub Actions is GitHub's automation platform.

Instead of executing commands on our own computer,

GitHub executes them on its own servers.

Whenever we push code,

GitHub creates a temporary machine.

That machine executes our workflow.

When finished,

the machine is destroyed.

This makes the process completely automated.

---

# 71. What is a Workflow?

A Workflow is simply an automation script.

GitHub stores workflows inside

```

.github/workflows/

```

Our project contains

```

pipeline.yml

```

Whenever GitHub detects this file,

it knows

"This repository contains automation."

---

# 72. Why YAML?

GitHub Actions uses YAML.

YAML stands for

YAML Ain't Markup Language.

YAML is designed for configuration.

Advantages

Easy to read

Human friendly

Supports nesting

Widely used

Many DevOps tools use YAML.

Examples

Docker Compose

Kubernetes

Ansible

GitHub Actions

Azure Pipelines

CircleCI

GitLab CI

Learning YAML is therefore an important DevOps skill.

---

# 73. Understanding pipeline.yml

Our entire automation pipeline is described inside

```

pipeline.yml

```

Instead of writing

Python

Java

Go

we describe

what should happen.

Example

```

Push Code

↓

Checkout Repository

↓

Install Python

↓

Install Dependencies

↓

Run Validation

↓

Upload Artifact

```

GitHub performs every step automatically.

---

# 74. Workflow Triggers

Our workflow begins with

```

on:

push:

branches:

- main

pull_request:

branches:

- main

```

This means

Execute the workflow

Whenever

Someone pushes to main

or

Someone creates a Pull Request targeting main

Without triggers,

GitHub would never start the workflow.

---

# 75. What is a Job?

Inside GitHub Actions,

a workflow contains one or more Jobs.

Think of Jobs as independent machines.

Each job has

its own filesystem

its own environment

its own software

its own execution

In our project,

we have four jobs.

```

Validate

↓

Sanitize

↓

Transform

↓

Verify

```

Each job represents one stage of our pipeline.

---

# 76. Why Multiple Jobs?

Instead of one large job,

we intentionally created multiple jobs.

Advantages

Better visualization

Independent execution

Parallel execution (future)

Easy debugging

Professional architecture

Suppose verification fails.

GitHub immediately shows

```

Validate ✓

Sanitize ✓

Transform ✓

Verify ✗

```

Finding problems becomes very easy.

---

# 77. What is a Runner?

Every GitHub Job executes on a Runner.

Our workflow uses

```

runs-on:

ubuntu-latest

```

This means

GitHub creates

a fresh Ubuntu virtual machine.

Everything happens inside this temporary machine.

After execution,

the machine is deleted.

Advantages

Clean environment

Reproducible builds

No leftover files

Consistent execution

---

# 78. Why Setup Python?

GitHub runners do not automatically know

which Python version we need.

Therefore,

we explicitly install Python.

```

uses:

actions/setup-python

```

Version

```

3.11

```

Every execution now uses the same interpreter.

This avoids

"It works on my machine"

problems.

---

# 79. Installing Dependencies

Next,

our workflow executes

```

pip install -r requirements.txt

```

Instead of manually installing packages,

GitHub automatically prepares the environment.

Every runner now has identical dependencies.

This guarantees consistent execution.

---

# 80. Why Install jq?

sanitize.py depends on

jq.

GitHub runners do not include jq by default.

Therefore,

our workflow executes

```

sudo apt-get update

sudo apt-get install jq

```

Now sanitize.py can execute every jq filter.

---

# 81. What are Artifacts?

Artifacts are files produced by one job

and consumed by another.

Example

Validate Job

Produces

```

validated.json

```

Sanitize Job

Downloads

```

validated.json

```

Produces

```

result.template.json

```

Transform Job

Downloads

```

result.template.json

```

Produces

```

transformed.json

```

Artifacts connect independent jobs together.

---

# 82. Why Upload Artifacts?

Every GitHub Job executes on a new machine.

This means

Files from Job 1

DO NOT exist

inside Job 2.

Therefore,

GitHub provides

```

upload-artifact

```

to preserve files.

Without artifacts,

every new job would start with an empty filesystem.

---

# 83. Why Download Artifacts?

The next job requires the previous output.

Example

Transform

needs

```

result.template.json

```

Therefore,

it downloads the artifact.

```

download-artifact

```

This creates a pipeline.

Output

↓

Artifact

↓

Download

↓

Next Stage

---

# 84. Understanding needs

Our workflow contains

```

sanitize

needs:

validate

```

Meaning

Sanitize cannot begin

until

Validate succeeds.

Similarly

```

transform

↓

needs sanitize

```

```

verify

↓

needs transform

```

This creates dependency management.

Exactly like production CI/CD pipelines.

---

# 85. What Happens if Validation Fails?

Suppose

validate.py

returns

```

sys.exit(1)

```

GitHub immediately marks

Validate

❌ Failed

Since

Sanitize

depends on Validate,

it never starts.

Transform also never starts.

Verify never starts.

This prevents wasted execution.

---

# 86. Complete Workflow Execution

The complete execution order is

```

Developer

↓

git push

↓

GitHub detects push

↓

Workflow Trigger

↓

Runner Created

↓

Checkout Repository

↓

Setup Python

↓

Install Dependencies

↓

Validate

↓

Upload validated.json

↓

Runner Destroyed

↓

New Runner

↓

Download validated.json

↓

Install jq

↓

Sanitize

↓

Upload result.template.json

↓

Runner Destroyed

↓

New Runner

↓

Download result.template.json

↓

Transform

↓

Upload transformed.json

↓

Runner Destroyed

↓

New Runner

↓

Download transformed.json

↓

Verify

↓

Pipeline Success

```

---

# 87. Why Is This Pipeline Professional?

Our pipeline demonstrates

✓ Modular jobs

✓ Artifact management

✓ Dependency management

✓ Configuration driven execution

✓ Independent runners

✓ Automation

✓ Error handling

✓ CI/CD best practices

This is very similar to pipelines used inside real organizations.

---

# 88. Skills Demonstrated by This Project

By completing Phase 1,

this project demonstrates practical knowledge of

Programming

• Python

• JSON

• jq

Version Control

• Git

• GitHub

Automation

• GitHub Actions

• YAML

• CLI

CI/CD Concepts

• Continuous Integration

• Workflow Automation

• Jobs

• Runners

• Artifacts

• Pipeline Dependencies

Software Engineering

• Modular Design

• Configuration Driven Development

• Single Responsibility Principle

• Pipeline Architecture

Future Cloud Integration

• AWS EC2

• AWS S3

• GitOps Deployment (Phase 2)

---

# 89. Phase 1 Recap

Our GitOps JSON Pipeline currently performs the following steps.

```

Input JSON

↓

Validate

↓

Sanitize

↓

Transform

↓

Verify

↓

Artifacts Generated

↓

GitHub Actions Executes Pipeline

↓

Pipeline Report

```

Every step is automated.

No manual intervention is required.

This completes Phase 1 of the project.

The next phase will integrate AWS services, allowing the pipeline to automatically publish processed artifacts to Amazon S3 and later deploy workloads on Amazon EC2 using GitOps principles.

---

# Summary of Part 3

In this chapter we learned

✓ What CI/CD is

✓ Continuous Integration

✓ Continuous Delivery

✓ Continuous Deployment

✓ GitHub Actions

✓ Workflows

✓ YAML

✓ Workflow Triggers

✓ Jobs

✓ Runners

✓ Artifact Uploads

✓ Artifact Downloads

✓ Job Dependencies

✓ Complete Workflow Execution

✓ Enterprise CI/CD Architecture

This concludes the documentation for **Phase 1**. At this point, the project is fully documented from the highest-level DevOps concepts down to the implementation details of every script and workflow component.