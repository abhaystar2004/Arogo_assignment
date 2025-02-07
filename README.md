# Arogo_assignment
# Mental Health Prediction App  

This repository contains a **Streamlit web application** for predicting mental health treatment needs based on survey responses. The model is a **Random Forest Classifier**, trained on mental health survey data and saved using `joblib`.  

## 🚀 Features  

- Simple and interactive UI using **Streamlit**  
- Predicts the likelihood of needing mental health treatment  
- Displays **anxiety level on a scale of 1 to 10** using a progress bar  
- Provides an easy way to test the model without coding  

## 🛠 Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/mental-health-prediction.git
   cd mental-health-prediction
   ```

2. **Create a virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Running the App  

1. **Ensure the trained model (`best_model.joblib`) is in the project directory.**  
2. **Start the Streamlit app:**  
   ```bash
   streamlit run app.py
   ```  
3. Open your browser and navigate to **`http://localhost:8501`**  

## 📊 How It Works  

- Fill in the required inputs (age, gender, work environment, etc.).  
- Click the **"Predict"** button.  
- The model predicts whether **mental health treatment** is likely needed.  
- The app also **displays an anxiety level (1-10)** using a progress bar.  

## 📌 Dependencies  

- Python 3.7+  
- `streamlit`  
- `scikit-learn`  
- `joblib`  
- `pandas`  
- `numpy`  

To install dependencies manually, run:  
```bash
pip install streamlit scikit-learn joblib pandas numpy
```

## 🏗 Future Improvements  

- Add visualizations for data insights  
- Deploy online using **Streamlit Cloud** or **Heroku**  
- Improve model accuracy with hyperparameter tuning  

---

### 💡 **Contributions are welcome!**  
Feel free to submit issues or pull requests.  

🔗 **Author**: [Abhay Sharma](https://github.com/abhaystar2004)  

Let me know if you need any modifications! 🚀
