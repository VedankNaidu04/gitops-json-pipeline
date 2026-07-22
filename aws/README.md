# AWS Infrastructure

## Phase 2 – AWS GitOps Pipeline

This directory contains all AWS-related resources for the GitOps JSON Pipeline project.

The goal of Phase 2 is to extend the local JSON processing pipeline into a cloud-based deployment pipeline while remaining fully compatible with the AWS Free Tier.

---

# Architecture

```
                Git Push
                   │
                   ▼
            GitHub Actions
                   │
                   ▼
              Validate
                   │
                   ▼
              Sanitize
                   │
                   ▼
              Transform
                   │
                   ▼
                Verify
                   │
                   ▼
        Upload transformed.json
                   │
                   ▼
               Amazon S3
                   │
                   ▼
              Amazon EC2
                   │
                   ▼
        Download Latest Artifact
                   │
                   ▼
          Local Deployment Folder
```

---

# AWS Services

The project currently uses the following AWS services.

## Amazon S3

Purpose:

- Store processed pipeline artifacts
- Act as the deployment source for EC2
- Maintain deployment history

---

## Amazon EC2

Purpose:

- Simulate a deployment server
- Download processed artifacts
- Store deployed JSON files

---

## IAM

IAM is used to provide secure access between services.

The project uses:

- IAM User
    - Used by GitHub Actions
    - Uploads artifacts to Amazon S3

- IAM Role
    - Attached to the EC2 instance
    - Downloads artifacts from Amazon S3

No AWS credentials are stored on the EC2 instance.

---

# Security

Sensitive credentials are never committed to Git.

GitHub Secrets will store:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION
- S3_BUCKET_NAME

---

# Directory Structure

```
aws/

├── iam/
│   ├── github-actions-policy.json
│   └── ec2-role-policy.json
│
├── s3/
│
├── ec2/
│
└── README.md
```

---

# Deployment Flow

1. Developer pushes code to GitHub.

2. GitHub Actions validates the JSON pipeline.

3. The pipeline sanitizes the input.

4. The pipeline transforms the data.

5. The pipeline verifies the final artifact.

6. The transformed artifact is uploaded to Amazon S3.

7. Amazon EC2 downloads the latest artifact.

8. The deployment directory is updated.

---

# AWS Free Tier

This project is intentionally designed to remain within the AWS Free Tier.

Current AWS services:

- Amazon S3
- Amazon EC2
- IAM

No additional paid AWS services are required for Phase 2.

---

# Future Phases

Phase 3

- Docker

Phase 4

- Logging

Phase 5

- Secrets Management

Phase 6

- Notifications

Phase 7

- Monitoring

Phase 8

- Production Architecture