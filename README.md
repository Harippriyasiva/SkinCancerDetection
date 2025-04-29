# SkinCancerDetection
SMART SKIN CARE: DEEP LEARNING IN SKIN CANCER DETECTION



![Screenshot 2025-03-24 110746](https://github.com/user-attachments/assets/712a7bb1-cc28-441d-823f-2ac632325d3f)

![Screenshot 2025-03-24 110804](https://github.com/user-attachments/assets/a99656fd-19f4-4992-9b8c-0e72bd0b9669)

![Screenshot 2025-03-24 110939](https://github.com/user-attachments/assets/ba6555b7-4e2f-4808-b7e7-fa8a9f08ee0d)

![Screenshot 2025-03-24 111014](https://github.com/user-attachments/assets/ac0a249e-9604-44cc-b3c4-7e5f25e3d29b)

![Screenshot 2025-03-24 111107](https://github.com/user-attachments/assets/234c24e6-a759-4257-8317-4824ab6e3790)

![Screenshot 2025-03-24 111119](https://github.com/user-attachments/assets/4deff159-f232-41d7-9620-3d0492d911d4)

![Conference Completion HP](https://github.com/user-attachments/assets/acd88712-21c0-45ce-a447-d1ab85a5e378)

![Conference Completion laxs](https://github.com/user-attachments/assets/20fc59b5-8ee3-47f6-9961-fdfbe5b78135)


Drive link for journal and reference IEEE paper : https://drive.google.com/drive/folders/13QIjjmnE1eRRtkcht5CFqvS2CqRYsu4F



# Smart Skin Care: Deep Learning in Skin Cancer Detection

A deep learning-based skin cancer detection system that utilizes image processing and convolutional neural networks (CNN) to identify melanoma, basal cell carcinoma, and squamous cell carcinoma with a 95.4% confidence level.

## 🌟 Project Overview

Skin cancer, especially melanoma, is one of the deadliest and most common cancers globally. Early detection can drastically improve survival rates. This project uses dermatologic spot images processed via advanced deep learning and spectral analysis techniques to enable non-invasive, fast, and accurate diagnosis.

## 🔬 Key Features

- 🎯 **High Accuracy**: Achieves 95.4% detection confidence using CNNs.
- 🧠 **Deep Learning Model**: CNN integrated with Fourier spectral analysis.
- ⚙️ **Web Deployment**: Flask-based web interface for image upload and prediction.
- 🏥 **Non-Invasive Diagnosis**: Reduces reliance on biopsies.
- 📊 **EDA & Segmentation**: Detailed preprocessing and lesion isolation.
- 👥 **User Authentication**: Register/login system with secure password hashing.

## 🧩 Modules

- **Melanoma Detection**: Preprocessing, segmentation, augmentation.
- **Squamous Cell Carcinoma**: CNN-based classification and performance tuning.
- **Basal Cell Carcinoma**: Real-time deployment and predictions through a Flask app.

## 🧱 Architecture

```plaintext
Input Image → Preprocessing → CNN + Spectral Analysis → Prediction → Web Output

🛠️ Tech Stack
Frontend: HTML/CSS (Flask templates)

Backend: Python, Flask

Model: TensorFlow/Keras (CNN)

Database: SQLite (for user management)

Libraries: NumPy, OpenCV, joblib, argon2, matplotlib

📂 model/
    └── model.h5
📂 static/
    └── uploads/
📂 templates/
    ├── index.html
    ├── about.html
    ├── register.html
    ├── login.html
    ├── predict.html
    └── result.html
📄 app.py
📄 create_database.py
📄 utils.py

🚀 Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/smart-skin-care.git
cd smart-skin-care
Create a virtual environment and install dependencies:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
Run the Flask app:

bash
Copy
Edit
python app.py
Open http://localhost:5000 in your browser.

📈 Model Performance
Accuracy: 95.4%

Classifier: CNN with Softmax Output

Dataset: ISIC Archive + Dermatology-labeled Images

Classes: Melanoma, Basal Cell Carcinoma, Squamous Cell Carcinoma

🔒 Security
Passwords hashed using Argon2.

Session-based authentication implemented.

📚 References
Refer to the REFERENCES section in the full report for all IEEE and clinical citations that contributed to this research.

📝 Authors
S. Harippriya [21CS089]

R. Lakshana [21CS106]

Project guided by Dr. G. Kavitha, Ph.D, Department of Computer Science and Engineering, Muthayammal Engineering College.

📄 PUBLICATIONS
[1]Dr.G.Kavitha, M.S(By Research), Ph.D, S.Harippriya, R.Lakshana, “Smart Skin Care: Deep Learning In Skin Cancer Detection” , National Conference on Innovative Trends in Technologies NCITT’25 organized by computer society of India KEC student branch, Perundurai, Erode – 638060, Tamilnadu, India, 01-March-2025.

