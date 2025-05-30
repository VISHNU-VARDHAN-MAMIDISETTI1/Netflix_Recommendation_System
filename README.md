"# Netflix_Recommendation_System" 
🎬 Netflix Recommendation System
A content-based movie recommendation system that suggests movies to users using cosine similarity and Naive Bayes models. The system is built with a clean Flask backend and an interactive HTML/CSS/JavaScript frontend. The project includes end-to-end data preprocessing, model building, and deployment.

🚀 Features
🎯 Content-Based Filtering using:

Cosine Similarity

Naive Bayes Classification

🧹 Data Preprocessing & Cleaning:

Handling missing data

Feature extraction (e.g., genres, cast, keywords)

🌐 Frontend:

Built with HTML, CSS, JavaScript

Simple and intuitive UI

🛠️ Backend:

Built using Flask

RESTful API architecture for recommendations

💾 Model Saving for fast response

🧪 Tested on realistic datasets with consistent performance

📁 Project Structure
graphql
Copy
Edit
├── code/                      # Core Python logic and models
├── datasets/                  # Movie data CSV files
├── saved_models/              # Trained models and vectorizers
├── static/                    # Static files (CSS, JS)
├── templates/                 # HTML frontend pages
├── main.py                    # Flask application entry point
├── requirements.txt           # Python dependencies
├── .gitignore                 # Files ignored by Git
├── .gitattributes             # LFS configuration
└── README.md                  # This file
🛠️ Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/VISHNU-VARDHAN-MAMIDISETTI1/Netflix_Recommendation_System.git
cd Netflix_Recommendation_System
Create Virtual Environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask App

bash
Copy
Edit
python main.py
Open your browser and go to http://127.0.0.1:5000

📊 Tech Stack
Layer	Technology
Backend	Python, Flask
ML Models	Cosine Similarity, Naive Bayes
Frontend	HTML, CSS, JavaScript
Data Source	Movie metadata CSV files

📌 Screenshots
(Insert UI screenshots here if available)

📈 Future Improvements
🎥 Add collaborative filtering for hybrid recommendations

🧠 Improve model accuracy using deep learning (e.g., embeddings)

💬 Add user login and movie rating features

📊 Dashboard to view movie trends

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

📄 License
This project is open source and available under the MIT License. 
