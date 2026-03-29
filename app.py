import streamlit as st
import pickle
import numpy as np
import streamlit.components.v1 as components

# 1. Page Configuration (Must be first)
st.set_page_config(
    page_title="Bio-AI Diagnosis Core",
    page_icon="🧬",
    layout="centered"
)

# --- NEW: Injecting HTML/CSS Animation from my another code ---
# This replicates the rotating circles from the Quiz landing page
animation_html = """
<style>
/* Base Styles from your HTML */
:root {
    --white-glow: 0 0 10px rgba(255,255,255,0.6), 0 0 5px rgba(255,255,255,0.9);
}

@keyframes rotateCircle { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
@keyframes rotateCircleAntiClockwise { from { transform: rotate(360deg); } to { transform: rotate(0deg); } }

/* The containers for the circles */
.animation-container {
    position: relative;
    width: 100%;
    height: 150px; /* Adjusted for Streamlit header space */
    display: flex;
    justify-content: center;
    align-items: center;
    background: black; /* Match App Background */
    margin-bottom: 20px;
}

/* Yen 1: Clockwise Outer Circle */
.yen1 {
    height: 91px; width: 91px;
    border-radius: 50%;
    border: 1px solid white;
    animation: rotateCircle .7s linear infinite;
    position: absolute;
    box-shadow: 0 0 7px #fff, 0 0 13px #fff, 0 0 27px #fff;
}

/* Yen 3: Anti-Clockwise Inner Circle */
.yen3 {
    height: 61px; width: 61px;
    border-radius: 50%;
    border: 1px solid white;
    animation: rotateCircleAntiClockwise .7s linear infinite;
    position: absolute;
    box-shadow: 0 0 7px #fff, 0 0 13px #fff, 0 0 27px #fff;
}

/* Yen 2 & 4: Small dots on the circles */
.yen2, .yen4 {
    height: 13px; width: 13px; border-radius: 50%;
    background: white; position: absolute;
    box-shadow: 0 0 9px #fff, 0 0 17px #fff, 0 0 29px #fff, 0 0 47px #fff;
}
.yen2 { top: -5px; left: 59%; }
.yen4 { bottom: -5px; left: 40%; }
</style>

<div class="animation-container">
    <div class="yen1"><div class="yen2"></div></div>
    <div class="yen3"><div class="yen4"></div></div>
</div>
"""

# 2. Mera favourite design
st.markdown("""
    <style>
    /* Pure Black Background and Neon Base */
    .stApp {
        background-color: #000000 !important;
        color: #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Neon White Glow Title */
    [id="bio-digital-neural-health-diagnosis"] {
        color: #ffffff !important;
        text-shadow: 0 0 10px #ffffff, 0 0 20px #00f2fe !important;
        letter-spacing: 2px;
        font-weight: bold;
        text-align: center;
    }

    /* --- THE FIX: VERY AGGRESSIVE BLACK NUMBERS --- */
    /* Targetting multiple selectors that Streamlit uses for tooltips and values */
    
    /* 1. Main tooltip value bubble */
    div[data-baseweb="tooltip"] div,
    [data-testid="stThumbValue"],
    .stSlider div[role="slider"] div {
        color: #000000 !important;
        font-weight: 900 !important;
        background-color: #ffffff !important; /* White bubble to show black number */
        border-radius: 4px;
        padding: 2px 6px;
        font-size: 16px !important;
        box-shadow: 0 0 10px rgba(0,0,0,0.5) !important;
    }

    /* 2. Min/Max values at slider ends */
    [data-testid="stTickBarMin"], [data-testid="stTickBarMax"] {
        color: #ffffff !important;
        font-weight: bold !important;
    }

    /* Input Elements: Deep Dark with Neon Border on Hover */
    .stNumberInput div div input, .stSlider {
        background-color: #0a0a0a !important;
        border-radius: 8px;
        border: 1px solid #333 !important;
        color: #fff !important;
    }
    
    .stNumberInput div div input:hover, .stSlider:hover {
        border-color: #00f2fe;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.4);
    }

    /* Standardized Input Labels */
    label {
        color: #ffffff !important;
        font-weight: bold !important;
    }

    /* Subheader Styling */
    h5 {
        color: #ffffff;
        text-shadow: 0 0 10px rgba(0, 242, 254, 0.6);
        letter-spacing: 1px;
    }

    /* Futuristic Neon Prediction Button */
    .stButton>button {
        width: 100%;
        background-color: transparent !important;
        color: #00f2fe !important;
        border: 2px solid #00f2fe !important;
        border-radius: 5px !important;
        font-weight: bold;
        transition: 0.5s;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.3);
        text-transform: uppercase;
    }
    
    .stButton>button:hover {
        background-color: #00f2fe !important;
        color: #000 !important;
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.9);
        transform: translateY(-2px);
    }

    /* Results Box Styling */
    .stAlert {
        border-radius: 10px;
        background-color: #0a0a0a;
        border: 1px solid #333;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Model ko safely load karna
@st.cache_resource
def load_research_model():
    try:
        with open('diabetes_model.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

# Modle ko load karna
model = load_research_model()

# --- Animation ko Display karna---
components.html(animation_html, height=150)

# Header
st.markdown("<h1 id='bio-digital-neural-health-diagnosis'>🧬 BIO-DIGITAL HEALTH INTERFACE</h1>", unsafe_allow_html=True)
st.markdown("Biochemical markers predictive analysis core operational.")
st.divider()

if model is None:
    st.error("❌ CRITICAL SYSTEM ERROR: 'diabetes_model.pkl' not detected. Neural Core offline.")
    st.info("Ensure the pkl file is in the same directory.")
else:
    # 4. Input Fields
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h5>🩸 Blood Analysis</h5>", unsafe_allow_html=True)
        preg = st.number_input('Pregnancies', 0, 20, 0)
        gluc = st.slider('Glucose Level', 0, 200, 110)
        bp = st.slider('Blood Pressure', 0, 140, 70)
        skin = st.number_input('Skin Thickness', 0, 100, 20)

    with col2:
        st.markdown("<h5>🧪 Physical Metrics</h5>", unsafe_allow_html=True)
        ins = st.number_input('Insulin', 0, 900, 30)
        bmi = st.number_input('BMI', 0.0, 70.0, 24.7)
        dpf = st.number_input('Pedigree Function', 0.0, 2.5, 0.47)
        age = st.slider('Subject Age', 21, 100, 25)

    st.divider()

    # 5. Prediction Execution
    if st.button('Predict Results'):
        features = np.array([[preg, gluc, bp, skin, ins, bmi, dpf, age]])
        prediction = model.predict(features)
        
        st.write("### DIAGNOSIS RESULT:")
        if prediction[0] == 1:
            st.markdown("""
                <div style="background-color: rgba(255, 75, 75, 0.1); padding: 20px; border-radius: 10px; border: 1px solid #ff4b4b; box-shadow: 0 0 15px rgba(255, 75, 75, 0.5);">
                    <h2 style="color: #ff4b4b; text-shadow: 0 0 10px #ff4b4b; margin:0; text-align:center;">⚠️ POSITIVE</h2>
                    <p style="color: white; text-align:center;">Biochemical markers indicate high risk of Diabetes. Clinical consultation required.</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="background-color: rgba(0, 255, 127, 0.1); padding: 20px; border-radius: 10px; border: 1px solid #00f2fe; box-shadow: 0 0 15px rgba(0, 242, 254, 0.5);">
                    <h2 style="color: #00f2fe; text-shadow: 0 0 10px #00f2fe; margin:0; text-align:center;">✅ NEGATIVE</h2>
                    <p style="color: white; text-align:center;">Subject appears healthy. All biomarkers are within stable physiological limits.</p>
                </div>
                """, unsafe_allow_html=True)
