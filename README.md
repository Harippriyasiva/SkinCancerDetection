<div align="center">

<br/>

```
███████╗██╗  ██╗██╗███╗   ██╗    ██████╗ ███████╗████████╗███████╗ ██████╗████████╗
██╔════╝██║ ██╔╝██║████╗  ██║    ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
███████╗█████╔╝ ██║██╔██╗ ██║    ██║  ██║█████╗     ██║   █████╗  ██║        ██║   
╚════██║██╔═██╗ ██║██║╚██╗██║    ██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   
███████║██║  ██╗██║██║ ╚████║    ██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   
╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   
```

# Smart Skin Care: Deep Learning in Skin Cancer Detection

**A CNN-powered clinical decision support tool for early-stage skin cancer diagnosis**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Accuracy](https://img.shields.io/badge/Accuracy-95.4%25-brightgreen?style=flat-square)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Published](https://img.shields.io/badge/Published-NCITT'25-red?style=flat-square)](https://drive.google.com/drive/folders/13QIjjmnE1eRRtkcht5CFqvS2CqRYsu4F)

<br/>

> *"Early detection saves lives. This system brings AI-powered dermatology to anyone with a camera."*

<br/>

</div>

---

## 📸 Screenshots

<div align="center">

| Upload Interface | Analysis Dashboard |
|:-:|:-:|
| ![Upload](https://github.com/user-attachments/assets/712a7bb1-cc28-441d-823f-2ac632325d3f) | ![Dashboard](https://github.com/user-attachments/assets/a99656fd-19f4-4992-9b8c-0e72bd0b9669) |

| Segmentation Output | Prediction Result |
|:-:|:-:|
| ![Segmentation](https://github.com/user-attachments/assets/ba6555b7-4e2f-4808-b7e7-fa8a9f08ee0d) | ![Result](https://github.com/user-attachments/assets/ac0a249e-9604-44cc-b3c4-7e5f25e3d29b) |

| EDA Visualization | Model Performance |
|:-:|:-:|
| ![EDA](https://github.com/user-attachments/assets/234c24e6-a759-4257-8317-4824ab6e3790) | ![Performance](https://github.com/user-attachments/assets/4deff159-f232-41d7-9620-3d0492d911d4) |

</div>

---

## 🩺 Why This Matters

Skin cancer is among the most diagnosed cancers worldwide, and **melanoma alone accounts for the majority of skin cancer deaths**. The five-year survival rate drops from ~99% to ~27% when detected late. Yet access to dermatologists remains limited in many regions.

This project bridges that gap — bringing **fast, non-invasive, AI-assisted diagnosis** directly through a browser, with no clinical equipment required.

---

## ✨ Key Features

| Feature | Details |
|--------|---------|
| 🎯 **95.4% Accuracy** | CNN classifier with Softmax output trained on ISIC archive data |
| 🔬 **Spectral Analysis** | Fourier transform integrated into the feature extraction pipeline |
| 🧬 **3 Cancer Types** | Melanoma · Basal Cell Carcinoma · Squamous Cell Carcinoma |
| 🌐 **Web Interface** | Flask-powered UI — upload image, get instant prediction |
| 🔒 **Secure Auth** | Argon2 password hashing + session management |
| 📊 **Full EDA** | Preprocessing, lesion segmentation, and augmentation pipeline |

---

## 🧠 Model Architecture

```
Input Image (RGB)
        │
        ▼
┌──────────────────┐
│  Preprocessing   │  ← Resize, Normalize, Augment
└────────┬─────────┘
         │
         ▼
┌──────────────────────────┐
│  Fourier Spectral Layer  │  ← Frequency-domain feature extraction
└────────┬─────────────────┘
         │
         ▼
┌──────────────────┐
│  CNN Backbone    │  ← Conv2D → MaxPool → BatchNorm (stacked)
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Dense Layers    │  ← Dropout for regularization
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ Softmax Output   │  → Melanoma / BCC / SCC
└──────────────────┘
```

---

## 🛠️ Tech Stack

```
┌─────────────┬──────────────────────────────────────────┐
│  Layer       │  Technologies                            │
├─────────────┼──────────────────────────────────────────┤
│  Frontend    │  HTML5, CSS3 (Jinja2 Templates)          │
│  Backend     │  Python 3.8+, Flask                      │
│  ML Model    │  TensorFlow / Keras (CNN)                 │
│  Database    │  SQLite                                  │
│  Libraries   │  NumPy, OpenCV, Matplotlib, joblib       │
│  Security    │  Argon2 (password hashing)               │
└─────────────┴──────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
smart-skin-care/
│
├── 📂 model/
│   └── model.h5                 # Trained CNN weights
│
├── 📂 static/
│   └── uploads/                 # User-uploaded images
│
├── 📂 templates/
│   ├── index.html               # Landing page
│   ├── about.html               # Project info
│   ├── register.html            # New user registration
│   ├── login.html               # User login
│   ├── predict.html             # Image upload & prediction
│   └── result.html              # Diagnosis result display
│
├── 📄 app.py                    # Flask application entry point
├── 📄 create_database.py        # SQLite schema setup
├── 📄 utils.py                  # Preprocessing & helper functions
└── 📄 requirements.txt
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip / virtualenv

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/smart-skin-care.git
cd smart-skin-care

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize the database
python create_database.py

# 5. Launch the application
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📊 Model Performance

```
┌──────────────────────────────────────────┐
│          Classification Report           │
├────────────────────────┬─────────────────┤
│  Metric                │  Score          │
├────────────────────────┼─────────────────┤
│  Overall Accuracy      │  95.4%          │
│  Dataset               │  ISIC Archive + │
│                        │  Dermatology DB │
│  Classes               │  3              │
│  Classifier            │  CNN + Softmax  │
└────────────────────────┴─────────────────┘

  Melanoma   ████████████████████ 95%+
  BCC        ████████████████████ 95%+
  SCC        ████████████████████ 95%+
```

---

## 🔒 Security

- Passwords are hashed using **Argon2** (memory-hard, phishing-resistant)
- Session-based authentication with server-side validation
- Uploaded images are sandboxed in `/static/uploads/`

---

## 🏆 Publication

> **S. Harippriya, R. Lakshana, Dr. G. Kavitha**  
> *"Smart Skin Care: Deep Learning In Skin Cancer Detection"*  
> National Conference on Innovative Trends in Technologies **NCITT'25**  
> Organized by Computer Society of India — KEC Student Branch  
> Perundurai, Erode, Tamil Nadu, India · **01 March 2025**

<div align="center">

| Certificate |  |
|:-:|:-:|
| ![HP Certificate](https://github.com/user-attachments/assets/acd88712-21c0-45ce-a447-d1ab85a5e378) | ![Lakshana Certificate](https://github.com/user-attachments/assets/20fc59b5-8ee3-47f6-9961-fdfbe5b78135) |

</div>

📄 **[Journal & IEEE Reference Paper →](https://drive.google.com/drive/folders/13QIjjmnE1eRRtkcht5CFqvS2CqRYsu4F)**

---

## 👩‍💻 Authors

<div align="center">

| Name | Roll No. | Role |
|------|----------|------|
| **S. Harippriya** | 21CS089 | Developer & Researcher |
| **R. Lakshana** | 21CS106 | Developer & Researcher |

**Guide:** Dr. G. Kavitha, M.S (By Research), Ph.D  
Department of Computer Science and Engineering  
Muthayammal Engineering College

</div>

---

## 📚 References

See the full IEEE and clinical citations in the [project report and reference folder](https://drive.google.com/drive/folders/13QIjjmnE1eRRtkcht5CFqvS2CqRYsu4F).

---

<div align="center">

*Built with ❤️ at Muthayammal Engineering College · Department of CSE*

</div>
