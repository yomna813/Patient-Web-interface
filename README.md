
# Patient Management Interface – DevOps Project

This repository presents a full-stack deployment of a **Patient Management Interface** built using Python Flask. The project incorporates modern DevOps tools and workflows including Docker, GitHub Actions, Terraform, and Kubernetes to automate build, deployment, and infrastructure provisioning.

---

## 📦 Key Components

- **Flask App** – A lightweight web application that simulates basic patient management.
- **Dockerfile** – Containerizes the app for deployment in any environment.
- **GitHub Actions** – Automates the CI/CD pipeline for testing and deployment.
- **Terraform** – Provisions cloud infrastructure on AWS (EC2, VPC, etc.).
- **Kubernetes** – Manages application deployment via Minikube or AWS EKS.

---

## ⚙️ Prerequisites

Ensure the following are installed and configured on your system before proceeding:

1. Git
2. Docker Engine / Docker Desktop
3. Terraform
4. AWS CLI (linked to your AWS account)
5. Minikube
6. kubectl
7. Docker Hub account (with credentials)

---

## 🚀 Getting Started

### 1. Clone the Repository

bash
git clone https://github.com/yomna813/patient-devops-interface.git
cd patient-devops-interface
---

### 2. Dockerize the Flask Application

The Dockerfile defines how to build the image:

bash
docker build -t yomna813/patient-app .
docker run -p 5000:5000 yomna813/patient-app

Test the app by navigating to `http://localhost:5000`.

---

### 3. Infrastructure as Code with Terraform

Navigate to the terraform directory:

bash
cd terraform
cp terraform.tfvars.example terraform.tfvars

Edit the `terraform.tfvars` file with your AWS key pair name and AMI ID.

Then, provision infrastructure:

bash
terraform init
terraform plan
terraform apply

This will create an EC2 instance and required networking.

---

### 4. Setting Up Kubernetes on EC2

SSH into your EC2 instance:

bash
ssh -i your-key.pem ubuntu@<EC2_PUBLIC_IP>

Then install the following:

bash
# Docker
sudo apt update
sudo apt install -y docker.io
sudo usermod -aG docker ubuntu
newgrp docker

# kubectl
curl -LO "https://dl.k8s.io/release/$(curl -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Start Minikube
minikube start --driver=docker

---

### 5. Deploy to Kubernetes

Copy files from your local machine to EC2:

bash
scp -i your-key.pem -r kubernetes/ ubuntu@<EC2_PUBLIC_IP>:~/
scp -i your-key.pem scripts/deploy-to-minikube.sh ubuntu@<EC2_PUBLIC_IP>:~/

Then on the EC2 instance:

bash
chmod +x deploy-to-minikube.sh
./deploy-to-minikube.sh

This script applies the deployment and service manifests.

---

### 6. Accessing the Application

Forward the port:

bash
kubectl port-forward service/patient-web-interface-service 8080:80

Now access the application from your browser at:

http://<EC2_PUBLIC_IP>:8080
`

---

## 🔁 GitHub Actions – CI/CD Workflow

Located at: `.github/workflows/ci-cd.yml`

This pipeline automates:

* Cloning the repository
* Logging in to Docker Hub
* Building the Docker image
* Pushing to Docker Hub (e.g., `yomna813/patient-app:latest`)
