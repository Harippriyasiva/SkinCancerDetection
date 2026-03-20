<div align="center">

<br/>

<div align="center">

```
███████╗██╗  ██╗██╗███╗   ██╗    ██████╗ ███████╗████████╗███████╗ ██████╗████████╗
██╔════╝██║ ██╔╝██║████╗  ██║    ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
███████╗█████╔╝ ██║██╔██╗ ██║    ██║  ██║█████╗     ██║   █████╗  ██║        ██║   
╚════██║██╔═██╗ ██║██║╚██╗██║    ██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   
███████║██║  ██╗██║██║ ╚████║    ██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   
╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   
```

</div>

# Smart Skin Care: Deep Learning in Skin Cancer Detection

**A CNN-powered clinical decision support tool for early-stage skin cancer diagnosis**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Accuracy](https://img.shields.io/badge/Accuracy-95.4%25-brightgreen?style=flat-square)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Conference](https://img.shields.io/badge/Conference-NCITT'25-orange?style=flat-square)](https://drive.google.com/drive/folders/13QIjjmnE1eRRtkcht5CFqvS2CqRYsu4F)
[![Journal](https://img.shields.io/badge/Journal-IJSREM%20Vol.09%20Issue.11-crimson?style=flat-square&color=8B0000)](https://ijsrem.com/volume-09-issue-11-november-2025/)
[![DOI](https://img.shields.io/badge/DOI-10.55041%2FIJSREM54416-blue?style=flat-square)](https://www.doi.org/10.55041/IJSREM54416)

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

## 🏆 Publications

### 📰 Journal Publication — IJSREM (2025)

<div align="center">

| | |
|:--|:--|
| **Journal** | International Journal of Scientific Research in Engineering and Management (IJSREM) |
| **Volume / Issue** | Vol. 09, Issue 11 — November 2025 |
| **SJIF Rating** | 8.586 |
| **ISSN** | 2582-3930 |
| **DOI** | [10.55041/IJSREM54416](https://www.doi.org/10.55041/IJSREM54416) |
| **Authors** | Dr. G. Kavitha · S. Harippriya · R. Lakshana |

</div>

📥 **[Download Published Paper](https://ijsrem.com/download/smart-skin-care-deep-learning-in-skin-cancer-detection/)**  
🌐 **[View on IJSREM](https://ijsrem.com/volume-09-issue-11-november-2025/)**  
📂 **[Drive — Paper & References](https://drive.google.com/drive/folders/13QIjjmnE1eRRtkcht5CFqvS2CqRYsu4F)**

---

### 🎤 Conference Presentation — NCITT'25

> **Dr. G. Kavitha · S. Harippriya · R. Lakshana**  
> *"Smart Skin Care: Deep Learning In Skin Cancer Detection"*  
> National Conference on Innovative Trends in Technologies **NCITT'25**  
> Organized by Computer Society of India — KEC Student Branch  
> Perundurai, Erode, Tamil Nadu, India · **01 March 2025**



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

<details>
<summary>Click to expand full IEEE citation list</summary>

<br/>

[1] Azhar Imran, Arslan Nasir, B. Mohammed, D. Foong, and A. Abbosh, "Benign and malignant skin lesions: Dielectric characterization modelling and analysis in frequency band 1 to 14 GHz", *IEEE Trans.*, vol. 70, no. 2, pp. 628–639, Feb. 2022.

[2] C. P. Davis, *Rosacea, Acne, Shingles, Covid-19 Rashes: Common Adult Skin Diseases*, 2020.

[3] Dipu Chandra Malo et al., "Skin Cancer Detection using Convolutional Neural Network", *2022 IEEE 12th Annual Computing and Communication Workshop and Conference (CCWC)*, pp. 0169–0176, 2022.

[4] Krishna Mridha and Md. Mezbah Uddin, "A Data-Driven Predictive Model for Speed Control in Automotive Safety Applications", *IEEE Sensors Journal*, vol. 22, no. 23, pp. 23258–23266, Dec. 2023.

[5] Lubna Riaz and Anca D. Jurcut, "FeduLPM: Federated Unsupervised Learning-Based Predictive Model for Speed Control in Customizable Automotive Variants", *IEEE Sensors Journal*, vol. 23, no. 13, pp. 14700–14708, July 2023.

[6] M. Chen et al., "AI-skin: Skin disease recognition based on self-learning and wide data collection through a closed-loop framework", *Inf. Fusion*, vol. 54, pp. 1–9, Feb. 2020.

[7] M. Goyal, T. Knackstedt, S. Yan, and S. Hassanpour, "Artificial intelligence-based image classification methods for diagnosis of skin cancer: Challenges and opportunities", *Comput. Biol. Med.*, vol. 127, Dec. 2020.

[8] Raissa Schiavoni and Gennaro Maietta, "In vivo human skin dielectric properties characterization and statistical analysis at frequencies from 1 to 30 GHz", *IEEE Trans. Instrum. Meas.*, vol. 70, 2023.

[9] S. A. R. Naqvi et al., "Benign and malignant skin lesions: Dielectric characterization modelling and analysis in frequency band 1 to 14 GHz", *IEEE Trans. Biomed. Eng.*, vol. 70, no. 2, pp. 628–639, Feb. 2023.

[10] S. A. R. Naqvi et al., "In vivo human skin dielectric properties characterization and statistical analysis at frequencies from 1 to 30 GHz", *IEEE Trans. Instrum. Meas.*, vol. 70, 2021.

[11] S. Samsudeen and G. Senthil Kumar, "A Data-Driven Predictive Model for Speed Control in Automotive Safety Applications", *IEEE Sensors Journal*, vol. 22, no. 23, pp. 23258–23266, Dec. 2022.

[12] S. Samsudeen and G. S. Kumar, "FeduLPM: Federated Unsupervised Learning-Based Predictive Model for Speed Control in Customizable Automotive Variants", *IEEE Sensors Journal*, vol. 23, no. 13, pp. 14700–14708, July 2023.

[13] S. S. Chaturvedi, J. V. Tembhurne, and T. Diwan, "A multi-class skin cancer classification using deep convolutional neural networks", *Multimedia Tools Appl.*, vol. 79, nos. 39–40, pp. 28477–28498, Oct. 2020.

[14] Yessi Jusman et al., "Performance of multi layer perceptron and deep neural networks in skin cancer classification", *2021 IEEE 3rd Global Conference on Life Sciences and Technologies (LifeTech)*, pp. 534–538, 2021.

</details>

---

<div align="center">

*Built with ❤️ at Muthayammal Engineering College · Department of CSE*

</div>
