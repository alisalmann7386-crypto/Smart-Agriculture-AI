import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import requests
from PIL import Image

# ==========================================
# PAGE CONFIGURATION
# ==========================================

API_KEY = st.secrets["OPENWEATHER_API_KEY"]

st.set_page_config(
    page_title="Smart Agriculture AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# LOAD CSS
# ==========================================

with open("style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("crop_model.pkl")
encoder = joblib.load("label_encoder.pkl")




# ==========================================
# CROP IMAGE FUNCTION
# ==========================================

def get_crop_image(crop):

    crop = crop.lower()

    images = {
        "apple": "assets/apple.png",
        "banana": "assets/banana.png",
        "blackgram": "assets/blackgram.png",
        "chickpea": "assets/chickpea.png",
        "coconut": "assets/coconut.png",
        "coffee": "assets/coffee.png",
        "cotton": "assets/cotton.png",
        "grapes": "assets/grapes.png",
        "jute": "assets/jute.png",
        "kidneybeans": "assets/kidneybeans.png",
        "lentil": "assets/lentil.png",
        "maize": "assets/maize.png",
        "mango": "assets/mango.png",
        "mothbeans": "assets/mothbeans.png",
        "mungbean": "assets/mungbean.png",
        "muskmelon": "assets/muskmelon.png",
        "orange": "assets/orange.png",
        "papaya": "assets/papaya.png",
        "pigeonpeas": "assets/pigeonpeas.png",
        "pomegranate": "assets/pomegranate.png",
        "rice": "assets/rice.png",
        "watermelon": "assets/watermelon.png"
    }

    return images.get(crop, "assets/default.png")



# ==========================================
# WEATHER FUNCTIONS
# ==========================================

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:

        return (
            data["name"],
            data["main"]["temp"],
            data["main"]["humidity"]
        )

    return None, None, None


def get_weather_location(lat, lon):

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:

        return (
            data["name"],
            data["main"]["temp"],
            data["main"]["humidity"]
        )

    return None, None, None



# ==========================================
# FERTILIZER RECOMMENDATION FUNCTION
# ==========================================

def fertilizer_recommendation(N, P, K):

    recommendations = []

    # Nitrogen
    if N < 50:
        recommendations.append(("Nitrogen", "Low", "🌿 Urea"))
    elif N > 100:
        recommendations.append(("Nitrogen", "High", "Reduce Nitrogen fertilizer"))
    else:
        recommendations.append(("Nitrogen", "Optimal", "No fertilizer required"))

    # Phosphorus
    if P < 40:
        recommendations.append(("Phosphorus", "Low", "🪨 DAP"))
    elif P > 80:
        recommendations.append(("Phosphorus", "High", "Avoid Phosphorus fertilizer"))
    else:
        recommendations.append(("Phosphorus", "Optimal", "No fertilizer required"))

    # Potassium
    if K < 40:
        recommendations.append(("Potassium", "Low", "🌱 Muriate of Potash (MOP)"))
    elif K > 80:
        recommendations.append(("Potassium", "High", "Reduce Potassium fertilizer"))
    else:
        recommendations.append(("Potassium", "Optimal", "No fertilizer required"))

    return recommendations

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    # Logo
    if os.path.exists("assets/logo.png"):
        st.image("assets/logo.png", width=180)

    # App Name (Top)
    st.title("🌾 Smart Agriculture AI")

    st.caption("AI Powered Crop Recommendation System")

    st.markdown("---")

    # Model Status
    st.success("✅ AI Model Loaded Successfully")

    st.markdown("""
### 🌱 About

This AI recommends the best crop using:

- 🌿 Nitrogen
- 🌿 Phosphorus
- 🌿 Potassium
- 🌡 Temperature
- 💧 Humidity
- 🧪 Soil pH
- 🌧 Rainfall

**Machine Learning Model**

Random Forest Classifier
""")

    st.markdown("---")

    # Developer Section
    with st.expander("👨‍💻 Developer Profile"):

        if os.path.exists("assets/profile.jpg"):
            st.image("assets/profile.jpg", width=170)

        st.markdown("""
### Md Salman Ali

🎓 B.Tech CSE (Data Science)

🏫 Jamia Millia Islamia

📧 alisalmann7386@gmail.com

💻 Machine Learning | Deep Learning | NLP
""")

    with st.expander("🛠 Technical Skills"):
        st.write("""
- Python
- Machine Learning
- Deep Learning
- NLP
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Matplotlib
""")

    with st.expander("🚀 Project Information"):
        st.write("""
This application predicts the best crop using a Random Forest Classifier based on soil nutrients and weather conditions.
""")
        

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero">

<h1>🌾 Smart Agriculture AI</h1>

<p>
Predict the Best Crop Using Artificial Intelligence
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# INPUT CARD
# ==========================================

st.markdown('<div class="glass">', unsafe_allow_html=True)

st.subheader("🌱 Soil & Weather Information")

# ==========================================
# LIVE WEATHER (AUTO LOCATION)
# ==========================================

from streamlit_geolocation import streamlit_geolocation

# ==========================================
# LIVE WEATHER
# ==========================================

st.subheader("🌦 Live Weather")

st.info("📍 Click the GPS button below to automatically detect your current location.")



location = streamlit_geolocation()

city = ""
temperature = 25.0
humidity = 80.0

if location and location["latitude"] is not None:

    lat = location["latitude"]
    lon = location["longitude"]

    city_name, temp, hum = get_weather_location(lat, lon)

    if city_name:

        city = city_name
        temperature = temp
        humidity = hum

        st.success("📍 Location detected successfully!")

# Autofill city
city = st.text_input(
    "City",
    value=city,
    placeholder="Searching your location..."
)

# Manual search button
if st.button("🌦 Refresh Weather"):

    city_name, temp, hum = get_weather(city)

    if city_name:

        temperature = temp
        humidity = hum

        st.success(f"Weather Loaded for {city_name}")

    else:

        st.error("City not found.")

st.write("")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("📍 City", city)

with c2:
    st.metric("🌡 Temperature", f"{temperature:.1f} °C")

with c3:
    st.metric("💧 Humidity", f"{humidity:.0f}%")

left, right = st.columns(2)

# ==========================================
# LEFT COLUMN
# ==========================================

with left:

    N = st.slider(
        "Nitrogen (N)",
        min_value=0,
        max_value=150,
        value=90
    )

    P = st.slider(
        "Phosphorus (P)",
        min_value=0,
        max_value=150,
        value=42
    )

    K = st.slider(
        "Potassium (K)",
        min_value=0,
        max_value=150,
        value=43
    )

    temperature = st.slider(
    "Temperature (°C)",
    0.0,
    50.0,
    float(temperature)
    )

# ==========================================
# RIGHT COLUMN
# ==========================================

with right:

    humidity = st.slider(
    "Humidity (%)",
    0.0,
    100.0,
    float(humidity)
    )

    ph = st.slider(
        "Soil pH",
        min_value=0.0,
        max_value=14.0,
        value=6.5
    )

    rainfall = st.slider(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=350.0,
        value=200.0
    )

st.write("")

predict = st.button(
    "🚀 Predict Best Crop",
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# PREDICTION SECTION
# ==========================================

if predict:

    # Create input DataFrame
    input_df = pd.DataFrame({
        "N": [N],
        "P": [P],
        "K": [K],
        "temperature": [temperature],
        "humidity": [humidity],
        "ph": [ph],
        "rainfall": [rainfall]
    })

    # AI Prediction
    with st.spinner("🤖 AI is analyzing soil and weather conditions..."):

        prediction = model.predict(input_df)
        probabilities = model.predict_proba(input_df)

        crop = encoder.inverse_transform(prediction)[0]
        confidence = np.max(probabilities) * 100

    st.toast("🌾 AI Prediction Ready!", icon="🌱")

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#00c853,#00e676);
    padding:18px;
    border-radius:18px;
    text-align:center;
    color:white;
    box-shadow:0 8px 20px rgba(0,255,120,.35);
    margin-bottom:20px;
    ">

    <h2>🎉 Prediction Successful</h2>

    <h4>Your crop recommendation is ready.</h4>

    👇 Scroll down to view the results.

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================
    # RESULT SECTION
    # ==========================================

    col1, col2 = st.columns([1, 2])

    with col1:

        image_path = get_crop_image(crop)

        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
        else:
            
            st.image(
                "https://images.unsplash.com/photo-1500382017468-9049fed747ef",
                use_container_width=True
            )

    with col2:

        st.markdown(f"""
        <div class="result">

        <h1 style="font-size:42px;color:#00ff99;">
        🌱 {crop.upper()}
        </h1>

        <h3 style="color:white;">
        Recommended Crop
        </h3>

        </div>

        """, unsafe_allow_html=True)

        st.write("")

        st.subheader("🤖 AI Confidence")

        progress = st.progress(0)

        for i in range(int(confidence) + 1):
            progress.progress(i)

        st.success(f"Prediction Confidence: {confidence:.2f}%")

    # ==========================================
    # WEATHER METRICS
    # ==========================================

    st.write("")
    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("🌡 Temperature", f"{temperature:.1f} °C")

    with c2:
        st.metric("💧 Humidity", f"{humidity:.1f}%")

    with c3:
        st.metric("🌧 Rainfall", f"{rainfall:.1f} mm")

    # ==========================================
    # SOIL METRICS
    # ==========================================

    st.write("")

    c4, c5, c6 = st.columns(3)

    with c4:
        st.metric("🧪 Nitrogen (N)", N)

    with c5:
        st.metric("🧪 Phosphorus (P)", P)

    with c6:
        st.metric("🧪 Potassium (K)", K)

    # ==========================================
    # AI RECOMMENDATION
    # ==========================================

    st.write("")

    st.info(f"""
### 🌱 AI Recommendation

Based on the soil nutrients and environmental conditions,
the most suitable crop is **{crop.title()}**.

This prediction was generated using a trained **Random Forest Classifier**.
""")


    st.write("")
    st.subheader("🌱 Fertilizer Recommendation")

    recommendations = fertilizer_recommendation(N, P, K)

    for nutrient, status, fertilizer in recommendations:

        if status == "Low":
            st.warning(f"🔸 {nutrient}: LOW\n\nRecommended: {fertilizer}")

        elif status == "High":
            st.error(f"🔴 {nutrient}: HIGH\n\n{fertilizer}")

        else:
            st.success(f"🟢 {nutrient}: OPTIMAL\n\n{fertilizer}")

    # ==========================================
    # PROBABILITY CHART
    # ==========================================

    st.write("")

    probability_df = pd.DataFrame({
        "Crop": encoder.classes_,
        "Probability (%)": probabilities[0] * 100
    })

    probability_df = probability_df.sort_values(
        by="Probability (%)",
        ascending=False
    )

    st.subheader("📊 Crop Prediction Probabilities")

    import plotly.express as px

    fig = px.bar(
        probability_df,
        x="Crop",
        y="Probability (%)",
        color="Probability (%)",
        text="Probability (%)"
    )

    fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")

    fig.update_layout(
        xaxis_title="Crop",
        yaxis_title="Probability (%)",
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)
    st.write("")
    st.subheader("🏆 Top 5 Recommended Crops")

    top5 = probability_df.head(5)

    cols = st.columns([1, 1, 1, 1, 1], gap="small")

    for i, (col, (_, row)) in enumerate(zip(cols, top5.iterrows()), start=1):

        with col:

            image_path = get_crop_image(row["Crop"])

           
            if os.path.exists(image_path):
                st.image(image_path, use_container_width=True)

            st.markdown(
                f"""
                <div style="margin-top:12px;">

                <div style="
                    color:#00ff99;
                    font-size:15px;
                    font-weight:700;
                    margin-bottom:6px;
                ">
                    Rank #{i}
                </div>

                <div style="
                    color:white;
                    font-size:20px;
                    font-weight:800;
                    margin-bottom:10px;
                ">
                    {row["Crop"].title()}
                </div>

                <div style="
                    color:#FFD54F;
                    font-size:24px;
                    font-weight:900;
                ">
                    {row["Probability (%)"]:.2f}%
                </div>

                </div>

                </div>
                """,
                unsafe_allow_html=True,
            )
  


    # ==========================================
    # INPUT SUMMARY
    # ==========================================

    st.write("")

    st.subheader("📋 Input Summary")

    summary = pd.DataFrame({
        "Feature": [
            "Nitrogen (N)",
            "Phosphorus (P)",
            "Potassium (K)",
            "Temperature (°C)",
            "Humidity (%)",
            "Soil pH",
            "Rainfall (mm)"
        ],
        "Value": [
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

# ==========================================
# AI INSIGHTS
# ==========================================

st.write("")
st.markdown("---")
st.subheader("📈 AI Crop Insights")

insight1, insight2, insight3 = st.columns(3)

with insight1:
    st.markdown("""
    <div class="glass">

    <h3>🌱 Soil Health</h3>

    Healthy nutrient values improve crop yield.
    Keep Nitrogen, Phosphorus and Potassium balanced.

    </div>
    """, unsafe_allow_html=True)

with insight2:
    st.markdown("""
    <div class="glass">

    <h3>🌦 Weather</h3>

    Temperature and humidity directly affect
    crop growth and productivity.

    </div>
    """, unsafe_allow_html=True)

with insight3:
    st.markdown("""
    <div class="glass">

    <h3>🤖 AI Prediction</h3>

    This recommendation is generated using
    Machine Learning trained on agricultural data.

    </div>
    """, unsafe_allow_html=True)



# ==========================================
# ABOUT SECTION
# ==========================================

st.write("")
st.markdown("---")

st.subheader("📖 About Smart Agriculture AI")

st.markdown("""
Smart Agriculture AI is an intelligent crop recommendation system
that predicts the most suitable crop based on:

- 🌿 Nitrogen
- 🌿 Phosphorus
- 🌿 Potassium
- 🌡 Temperature
- 💧 Humidity
- 🧪 Soil pH
- 🌧 Rainfall

### Machine Learning Model

Random Forest Classifier

The model has been trained on agricultural datasets
to recommend crops with high accuracy.

""")

# ==========================================
# MODEL INFORMATION
# ==========================================

st.write("")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🤖 Model", "Random Forest")

with col2:
    st.metric("🌾 Crops", "22")

with col3:
    st.metric("📊 Features", "7")

with col4:
    st.metric("⚡ Accuracy", "99.3%")

# ==========================================
# DOWNLOAD REPORT
# ==========================================

st.write("")
st.markdown("---")

st.subheader("📥 Download Prediction Report")

report = pd.DataFrame({

    "Nitrogen":[N],
    "Phosphorus":[P],
    "Potassium":[K],
    "Temperature":[temperature],
    "Humidity":[humidity],
    "Soil pH":[ph],
    "Rainfall":[rainfall],
    "Recommended Crop":[crop if predict else ""]
})

csv = report.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Download Prediction Report",
    data=csv,
    file_name="crop_prediction_report.csv",
    mime="text/csv",
    use_container_width=True
)

# ==========================================
# FOOTER
# ==========================================

st.write("")
st.write("")
st.markdown("---")

st.markdown("""

<div style="text-align:center;padding:20px;">

<h2 style="color:#00ff99;">
🌾 Smart Agriculture AI
</h2>

<p style="color:gray;font-size:18px;">
AI Powered Crop Recommendation System
</p>

<p style="color:gray;">
Developed using
<b>Python</b> •
<b>Streamlit</b> •
<b>Scikit-Learn</b> •
<b>Random Forest</b>
</p>

</div>

""", unsafe_allow_html=True)
