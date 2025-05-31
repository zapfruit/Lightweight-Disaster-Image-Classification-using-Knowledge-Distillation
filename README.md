
# 🌍 Lightweight Disaster Image Classification using Knowledge Distillation

This project presents a lightweight yet effective deep learning pipeline for disaster image classification. Leveraging knowledge distillation, we train a compact student model to mimic a larger, more powerful teacher model—making the solution efficient for real-world deployments on low-resource devices.

---

## 🔗 Live Demo
👉 [**Try the Streamlit App**](https://lightweight-disaster-image-classification.streamlit.app/)


---

## 🚀 Features

- ✅ Real-time image classification via web interface
- 🧠 Knowledge distillation for model compression
- 🔬 Supports multiple disaster categories (e.g., earthquake, flood, wildfire, etc.)
- 📦 Lightweight architecture optimized for deployment
- 🌐 Easy-to-use and accessible from any device with a browser

---

## 🧑‍💻 Tech Stack

- **Frontend & Deployment:** Streamlit
- **Model Training:** PyTorch
- **Model Optimization:** Knowledge Distillation
- **Backend:** Python
- **Hosting:** Streamlit Cloud

---

## 🗂️ Project Structure

```
.
├── app.py                   # Streamlit application
├── models/                  # Trained teacher and student models
├── utils/                   # Utility functions for preprocessing, prediction, etc.
├── assets/                  # Sample images and assets
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🛠️ Setup Instructions

1. **Clone the repository**
    ```
    git clone https://github.com/zapfruit/Lightweight-Disaster-Image-Classification-using-Knowledge-Distillation.git
    cd Lightweight-Disaster-Image-Classification-using-Knowledge-Distillation
    ```

2. **Install dependencies**
    ```
    pip install -r requirements.txt
    ```

3. **Run locally**
    ```
    streamlit run app.py
    ```
```
