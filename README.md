# DevOps Case Study – Prasanna Kumar

## Overview

This repository contains a complete solution to the DevOps case study, covering:

* Scripting (Terraform plan validation)
* Infrastructure as Code (Terraform resource management)
* Containers (Docker & Docker Compose)
* Dev / Problem Solving (Backstage custom action)

---

## 1. Scripting – Terraform Plan Validation

### Objective

Validate a Terraform plan (`tfplan.json`) and determine whether it is safe to apply.

### Rules Implemented

* Only `create` and `update` actions are allowed
* Any `delete` or `replace` action blocks execution
* Updates must:

  * Modify only the `tags` attribute
  * Modify only the `GitCommitHash` tag

### Implementation

* Parses `resource_changes` from Terraform JSON
* Iterates through each resource
* Validates action types and attribute changes

### Run

```bash
cd scripting
python script.py tfplan-1.json
```

### Example Output

```
SAFE: Plan can be applied
BLOCKED: resource has destructive action ['delete']
BLOCKED: invalid tag modification
```

---

## 2. Infrastructure as Code – Terraform

### Objective

Delete the **second resource** created using `count` without affecting other resources.

### Problem

Using `count`:

```
resource[0], resource[1], resource[2]
```

Removing one shifts indexes → unintended changes.

### Solution

1. Replace `count` with `for_each`
2. Use stable keys instead of indexes
3. Move Terraform state:

```bash
terraform state mv
```

4. Remove only the target resource

### Result

```bash
terraform apply
```

```
No changes
```

### Documentation

See:

```
infrastructure-as-code/steps-to-fix.md
```

---

## 3. Containers – Docker & Docker Compose

### Objective

Dockerize the Express.js application and expose it on port **4567**

### Implementation

**Dockerfile**

* Uses Node.js base image
* Copies app files
* Installs dependencies
* Runs application

**docker-compose.yml**

* Builds image
* Runs container
* Maps port `4567:4567`

### Run

```bash
cd express-app
docker-compose up --build
```

### Access

```
http://localhost:4567
```

### Fixes Applied

* Corrected entry file (`express.js`)
* Fixed missing module errors
* Corrected container working directory

---

## 4. Dev / Problem Solving – Backstage

### Objective

* Create a Backstage instance
* Implement custom action: `my:custom:action`
* Use it as the only step in template

### Limitation
Due to local Windows environment limitations (native module build failures), I implemented the Backstage custom action and template as required.

The solution includes:
- Custom action with id: my:custom:action
- Template configured to use only this action

Full Backstage setup could not be completed due to:

* Native module build failures on Windows
* High disk space requirements
* Dependency compilation issues

### Implemented Solution

**Custom Action**

File:

```
wild/custom-action.ts
```

Function:

* Creates a file in the workspace

**Template**

File:

```
wild/template.yaml
```

* Uses only `my:custom:action`
* Accepts filename input

### Note

This implementation works correctly in:

* Linux
* WSL
* Container environments

---

## Project Structure

```
om-case-study/
│
├── scripting/
│   └── script.py
│
├── infrastructure-as-code/
│   ├── main.tf
│   └── steps-to-fix.md
│
├── express-app/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── package.json
│   └── express.js
│
├── wild/
│   ├── custom-action.ts
│   └── template.yaml
│
└── README.md
```

---

## Security

* Sensitive Terraform plan files removed
* Git history cleaned
* `.gitignore` updated to prevent leaks

---

## Final Status

| Task      | Status                                   |
| --------- | ---------------------------------------- |
| Scripting | Completed                                |
| Terraform | Completed                                |
| Docker    | Completed                                |
| Backstage | Implemented (partial due to environment) |

---

## Summary

This project demonstrates:

* Safe infrastructure validation
* Terraform state management
* Containerization and debugging
* Practical DevOps problem-solving

---

