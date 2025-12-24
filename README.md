🎓 Smart Career Guidance System

An AI-powered Career Guidance Portal designed to assist students in identifying suitable career paths and structured learning roadmaps based on their skills, interests, and academic background.

📌 Project Overview

Choosing the right career path is a major challenge for students due to lack of awareness, guidance, and personalized insights.
This project addresses that gap by leveraging Machine Learning and AI techniques to recommend careers and learning paths in a structured and accessible digital platform.

The system analyzes user inputs such as skills and interests, processes them using ML models, and provides career recommendations along with curated learning resources.

🎯 Objectives

To provide personalized career recommendations based on individual student profiles

To assist students in exploring suitable career paths using ML-based prediction models

To offer structured learning roadmaps with free and paid certification resources

To create a centralized, user-friendly platform integrating career assessment and guidance tools

To promote inclusive access to career guidance, reducing hesitation in seeking help

🧠 Machine Learning Models Used

The system employs multiple ML techniques to improve recommendation accuracy:

TF-IDF Vectorization – Converts skills and interests into numerical feature vectors

Cosine Similarity – Measures similarity between student profiles and career datasets

K-Nearest Neighbors (KNN) – Identifies closely matching career profiles

Decision Tree Classifier – Maps skill patterns to potential career outcomes

Support Vector Machine (SVM) – Enhances classification accuracy for career prediction

(Using multiple models ensures robustness and better generalization.)

🏗️ System Architecture

Frontend: Next.js (React) with Tailwind CSS

Backend: Node.js (API layer) + Python/Django (ML processing)

Machine Learning: Scikit-learn, Pandas, NumPy

Data Storage: CSV-based datasets (can be extended to databases)

Model Artifacts: Serialized ML models (.pkl files)

⚙️ Features

Skill & interest-based career assessment

AI-driven career recommendations

Career-specific learning roadmaps

Clean and responsive UI

Modular backend with ML integration

Scalable design for future enhancements

📂 Project Structure (Simplified)
smart-career-guide/
│
├── frontend/            # Next.js frontend
├── backend/             # Node.js backend APIs
├── career_portal/       # Django + ML logic
├── datasets/            # Career & student datasets
├── models/              # Trained ML models (.pkl)
└── README.md

🚀 How to Run the Project (Basic)
1️⃣ Clone the Repository
git clone https://github.com/your-username/smart-career-guide.git
cd smart-career-guide

2️⃣ Frontend Setup
cd frontend
npm install
npm run dev

3️⃣ Backend Setup
cd backend
npm install
node server.js

4️⃣ ML Environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python train_model.py

📈 Future Enhancements

Integration with real-time job market APIs

User authentication and profile tracking

Cloud deployment (Vercel / Render / AWS)

Advanced deep learning models

Real-time mentor interaction modules

👩‍💻 Developed By

Preeti
Master’s Student – Computer Applications
Interest Areas: AI, Machine Learning, Web Development

📜 License

This project is developed for academic and educational purposes.
