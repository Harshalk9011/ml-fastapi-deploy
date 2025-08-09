🚀 FastAPI ML Deployment with Kubernetes & CI/CD
This project demonstrates deploying a Machine Learning model using FastAPI, Docker, Kubernetes, and GitHub Actions with CI/CD automation.

📌 Features
FastAPI backend serving an ML model (Iris classifier)

Dockerized application for consistent deployments

Kubernetes manifests for scalable deployment

Minikube / Cloud Ready setup

GitHub Actions CI/CD pipeline for automated builds & deployments

🏗 Architecture
mermaid
Copy
Edit
flowchart LR
    A[Developer Pushes Code] --> B[GitHub Actions CI]
    B --> C[Docker Image Built]
    C --> D[Push to Docker Hub]
    D --> E[Kubernetes Deployment Updated]
    E --> F[FastAPI Service Exposed]
    F --> G[User Sends API Request]
📂 Project Structure
bash
Copy
Edit
.
├── app.py                  # FastAPI app
├── requirements.txt        # Dependencies
├── Dockerfile              # Docker build file
├── k8s/
│   ├── deployment.yaml     # Kubernetes deployment
│   ├── service.yaml        # Kubernetes service
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions CI/CD
└── README.md               # Project documentation
⚙️ Setup & Run Locally
1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/<your-username>/ml-fastapi-deploy.git
cd ml-fastapi-deploy
2️⃣ Build & run locally
bash
Copy
Edit
docker build -t fastapi-ml .
docker run -p 8000:8000 fastapi-ml
API will be live at: http://127.0.0.1:8000

☸️ Deploy to Kubernetes (Minikube Example)
Start Minikube
bash
Copy
Edit
minikube start
Apply Kubernetes manifests
bash
Copy
Edit
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
Get service URL
bash
Copy
Edit
minikube service fastapi-ml-service --url
📡 API Usage
Example Request:
bash
Copy
Edit
curl -X POST "http://<service-url>/predict" \
  -H "Content-Type: application/json" \
  -d '{
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
      }'
Example Response:
json
Copy
Edit
{
  "prediction": 0,
  "species": "setosa"
}
📸 Screenshots
API Docs	Sample Prediction

🚀 CI/CD Workflow
Push code to main branch

GitHub Actions builds Docker image

Image is pushed to Docker Hub

Kubernetes deployment is updated automatically

Live API gets new version with zero downtime

📝 Tech Stack
FastAPI (Backend)

scikit-learn (ML model)

Docker (Containerization)

Kubernetes (Orchestration)

GitHub Actions (CI/CD)

Minikube / Cloud (Deployment)

📄 License
This project is licensed under the MIT License.

<img width="1536" height="1024" alt="ChatGPT Image Aug 10, 2025, 02_39_48 AM" src="https://github.com/user-attachments/assets/6ad66474-6e2e-4734-ab58-f1bbc047fc89" />











ChatGPT can make mist
