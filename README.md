# 🌾 Smart Agriculture AI

An AI-powered web application that recommends the most suitable crop based on soil nutrients, weather conditions, and environmental parameters. The application uses a Random Forest Machine Learning model and provides an interactive dashboard built with Streamlit.

---

## 🌐 Live Demo

Try the application here:

https://smart-agriculture-ai-salman.streamlit.app/

---

## 🚀 Features

- 🌾 AI-powered Crop Recommendation
- 🌦 Live Weather Integration using OpenWeather API
- 📍 Automatic Current Location Detection
- 🌱 Soil Nutrient Analysis (N, P, K)
- 🏆 Top 5 Recommended Crops with Images
- 📊 Interactive Prediction Probability Chart
- 📈 Confidence Score Visualization
- 🌿 Fertilizer Recommendation System
- 📄 Download Prediction Report (CSV/PDF)
- 🎨 Modern Glassmorphism User Interface
- 📱 Responsive Streamlit Dashboard

---

## 🧠 Machine Learning Model

The project uses:

- **Algorithm:** Random Forest Classifier
- **Feature Scaling:** StandardScaler 
- **Label Encoding:** LabelEncoder
- **Model Serialization:** Joblib

### Input Features

The model predicts the most suitable crop using:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- Soil pH
- Rainfall (mm)

---

## 🌦 Weather Integration

The application automatically fetches real-time weather information using the OpenWeather API.

Displays:

- 🌡 Temperature
- 💧 Humidity
- 📍 Current Location Detection
- 🌍 City Name

---

## 🌱 Supported Crops

The model can recommend crops such as:

- Rice
- Maize
- Cotton
- Coffee
- Banana
- Apple
- Chickpea
- Kidney Beans
- Lentil
- Mango
- Orange
- Papaya
- Watermelon
- Coconut
- Grapes
- Jute
- Blackgram
- Mungbean
- Mothbeans
- Muskmelon
- Pigeonpeas
- Pomegranate

---

## 📊 Visualizations

The dashboard includes:

- Interactive Probability Bar Chart
- Top 5 Crop Recommendation Cards
- Crop Images
- Confidence Percentage
- Weather Dashboard

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Plotly
- Requests
- Pillow
- ReportLab
- OpenWeather API

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud** and provides an interactive AI-powered crop recommendation system accessible from any device.

---

## 📂 Project Structure

```
Smart-Agriculture-AI/
│
├── app.py
├── style.css
├── crop_model.pkl
├── label_encoder.pkl
├── requirements.txt
├── README.md
├── assets/
│   ├── logo.png
│   ├── profile.jpg
│   ├── crop images...
```

---

## 🎯 Future Enhancements

- 🍃 Crop Disease Detection using Deep Learning
- 🛰 Satellite Weather Integration
- 🌍 Interactive Farm Location Map
- 📈 Yield Prediction
- 💰 Live Crop Market Prices
- 🤖 AI Farming Assistant
- 🌾 Soil Health Analysis

---

## 👨‍💻 Author

**Md Salman Ali**

B.Tech Computer Science Engineering (Data Science)

Jamia Millia Islamia

---

⭐ **If you found this project useful, please consider giving it a Star on GitHub!**
