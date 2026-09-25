import streamlit as st                            # Importerar Streamlit för webbgränssnittet
from tensorflow.keras.models import load_model
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np

# Sätter rubriken på applikationen
st.title("Rita en siffra")

# Cachar modellen så den inte laddas om vid varje interaktion
@st.cache_resource
def load_my_model():
    return load_model("model/mnist_model.keras")

model = load_my_model()

st.write("Modellen är laddad !")

canvas_result = st_canvas(
    fill_color="black",
    stroke_width=14,
    stroke_color="white",
    background_color="black",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
    return_image_data=True,
)

if canvas_result.image_data is not None:
    img = Image.fromarray(canvas_result.image_data.astype("uint8"))
    img = img.convert("L")
    img = img.resize((28, 28))

    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 28, 28)

    prediction = model.predict(img_array)
    predicted_digit = np.argmax(prediction)
    confidence =np.max(prediction)

    st.write(f"Modellen tror att det är: {predicted_digit}(säkerhet:{confidence*100:.1f}%)")