
# **Cat Fact App - DevOps Engineer Home Exercise**

## **Overview**
This project is a DevOps exercise for creating a REST API that fetches random cat facts. It includes containerization, orchestration with Helm, and a CI/CD pipeline.

---

## **Key Features**
1. **Python Flask REST API**: Provides two endpoints:
   - `/catfact`: Fetches a random cat fact.
   - `/health`: Health status check.
2. **Dockerized Application**: Multi-stage build for optimized image size and separation of concerns.
3. **Helm Chart Deployment**: Deploys the app to Kubernetes.
4. **GitHub Actions CI/CD**:
   - Builds, tests, and deploys the application.
   - Creates artifacts (Helm deployment logs and ingress description) for extended review.

---

## **Endpoints**

| **Endpoint** | **Method** | **Description** |
|--------------|------------|-----------------|
| `/health`    | GET        | Health status: `{ "status": "up" }` |
| `/catfact`   | GET        | Random cat fact: `{ "catFact": "fact here" }` |

---

## **Ingress Explanation**
- An ingress resource was configured in the Helm chart.
- **Decision**: The `nginx-ingress-controller` was intentionally not installed to avoid overcomplicating the pipeline.  
- The pipeline still **validates the ingress** successfully:
   - Ingress logs confirm endpoints and ports are correctly read.
   - This decision keeps the pipeline simpler and focused on core deliverables.

---

## **Multi-Stage Dockerfile**
The Dockerfile uses a multi-stage build to:
- **Stage 1**: Install dependencies in a virtual environment.
- **Stage 2**: Run the application using the lightweight `python:3.11-alpine` image.

This ensures:
- Smaller image size.
- Clean runtime environment with only essential dependencies.

---

## **Deployment Steps**

### **Docker**
1. Build the image:
   ```bash
   docker build -t cat-fact:v1 .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 cat-fact:v1
   ```

### **Helm**
1. Deploy the chart:
   ```bash
   helm upgrade --install cat-fact ./cat-fact --namespace default
   ```
2. Access the app:
   - Port forward the service:
     ```bash
     kubectl port-forward svc/cat-fact 5000:5000
     ```
   - Test endpoints:
     - `http://localhost:5000/health`
     - `http://localhost:5000/catfact`

---

## **CI/CD Pipeline**
The pipeline automates:
1. **Build and Test**: Builds the Docker image and tests endpoints.
2. **Kubernetes Deployment**: Deploys using Helm.
3. **Ingress Validation**: Ensures the ingress definition is recognized and endpoints are exposed.

### Artifacts:
- **Helm Deployment Output**: `helm-deployment-output.log`
- **Ingress Yaml Output**: `ingress-yaml-output.log`
- **Ingress Description**: `ingress-description.log`

---

## **Final Notes**
This exercise demonstrates the ability to create a functional application, containerize it, deploy it using Helm, and automate it with a CI/CD pipeline. The ingress resource was implemented but the controller was not installed to prioritize simplicity while ensuring the pipeline remains clean and functional.

---

