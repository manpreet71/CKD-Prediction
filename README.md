# CKD-Prediction



# 🩺 Chronic Kidney Disease Prediction Project

## 📌 Overview
This project focuses on predicting **Chronic Kidney Disease (CKD)** using a machine learning approach. The goal is to assist healthcare professionals in early detection of CKD based on several medical parameters. The model is trained using clinical data and deployed with a user-friendly **Flask web application** interface.

---

## 📊 Dataset

- **File**: `kidney_disease.csv`
- **Records**: 400 patients
- **Target variable**: `classification` (ckd / notckd)

### 🔍 Key Features:
| Feature | Description |
|---------|-------------|
| `age` | Age of the patient (years) |
| `bp` | Blood pressure (mm/Hg) |
| `sg` | Specific gravity of urine |
| `al` | Albumin in urine (0–5) |
| `hemo` | Hemoglobin level (g/dL) |
| `sc` | Serum creatinine (mg/dL) |
| `htn` | Hypertension (yes/no) |
| `dm` | Diabetes mellitus (yes/no) |
| `cad` | Coronary artery disease (yes/no) |
| `appet` | Appetite status (good/poor) |
| `pc` | Pus cell (normal/abnormal) |

---

## 🧠 Model Training

- **Notebook**: `project_main.ipynb`
- **Model Used**: Gradient Boosting Classifier (`model_rfc.pkl`)
- **Data Processing**:
  - Missing value imputation
  - Label encoding for categorical features
  - Standard scaling with `StandardScaler`

- **Manually Encoded Columns**:
  - Categorical features like `htn`, `dm`, `cad`, `appet`, and `pc` were label encoded to numerical values to be used by the model.

---

## 🧪 Evaluation

- **Accuracy**: ~97%
- **F1 Score**: High, indicating balanced performance
- **Confusion Matrix**: Low false negatives and false positives
- **Cross-validation**: Used to validate model generalization

---

## 🌐 Deployment (Flask)

- **File**: `app.py`
- **Frontend Template**: `templates/index3.html`
- **Image Assets**: Stored in `static/images/`
  - `CKD3.jpg`
  - `CKD4.png`
  - `CKD5.png`

### 🔧 Folder Structure:
```
project/
│
├── models5/
│   ├── model_rfc.pkl
│   └── scaler.pkl
│
├── static/
│   └── images/
│       ├── CKD3.jpg
│       ├── CKD4.png
│       └── CKD5.png
│
├── templates/
│   └── index3.html
│
├── app.py
├── kidney_disease.csv
├── project_main.ipynb
├── requirements.txt
└── README.md
```

---

## 📷 Screenshots

![Screenshot 2025-04-30 133348](https://github.com/user-attachments/assets/cb5e82bc-6e82-4a66-8fc3-1b1dce90054c)
![Screenshot 2025-04-30 140834](https://github.com/user-attachments/assets/c1be3fd5-5d13-4113-9bff-5f5c453f5dd0)

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/ckd-prediction.git
cd ckd-prediction
pip install -r requirements.txt
python app.py
```

---

## 💡 How It Works

1. User inputs patient data on the web interface.
2. Data is preprocessed and scaled using the saved `scaler.pkl`.
3. Model makes a prediction using `model_rfc.pkl`.
4. Output (CKD / Not CKD) is displayed on the web page.

---

## 📁 Requirements

All dependencies are listed in `requirements.txt`. Some key packages:
- Flask
- pandas
- numpy
- scikit-learn
- matplotlib (for plots if any)

---

## 📣 Future Improvements

- Add more patient data for better generalization.
- Deploy to cloud using Render / Heroku / Azure.
- Include visualization dashboard for doctors.

---

## 👨‍⚕️ Conclusion

This project demonstrates how **machine learning** can aid in **healthcare diagnostics**, especially for **chronic diseases**. With more data and continual refinement, such tools can be life-saving.
