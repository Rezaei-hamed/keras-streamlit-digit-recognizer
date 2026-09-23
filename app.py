import streamlit as st                            # Importerar Streamlit för webbgränssnittet
from tensorflow.keras.models import load_model

# Importerar load_model för att ladda den tränade Keras-modellen
from streamlit_drawable_canvas import st_canvas


# Sätter rubriken på applikationen
st.title("Rita en siffra")



# Cachar modellen så den inte laddas om vid varje interaktion
@st.cache_resource


# Laddar den sparade Keras-modellen från mappen "model"
def load_my_model():
    return load_model("model/mnist_model.keras")

# Anropar funktionen och sparar modellen i en variabel
model=load_my_model()

# Visar ett bekräftelsemeddelande i appen
st.write("Modellen är laddad !")


# Skapar en ritduk i Streamlit för att rita siffror

canvas_result =st_canvas(
    fill_color="black",        # Fyllnadsfärg för stängda former (används inte här)
    stroke_width=14,           # Tjocklek på pennan i pixlar
    stroke_color="white",      # Färg på pennan (vit linje)
    background_color="black",  # Bakgrundsfärg på duken (svart)
    height=280,                # Höjd på ritduken i pixlar 
    width=280,                 # Bredd på ritduken i pixlar
    drawing_mode="freedraw",   # Tillåter frihandsritning
    key="canvas",              # Unikt ID för komponenten i Streamlit
    return_image_data=True,
)


# Importerar PIL för bildhantering och NumPy för matriser
# Kollar om användaren har ritat något på duken
# Omvandlar ritdukens data till en standardbild
# Gör bilden gråskalig (tar bort färger)
# Ändrar storleken till 28x28 pixlar

from PIL import Image
import numpy as np

if canvas_result.image_data is not None:
    img = Image.fromarray(canvas_result.image_data.astype("uint8"))
    img = img.convert("L")
    img = img.resize((28, 28))





# Normaliserar bilden till 0-1
# #Ändrar formen till (1, 28, 28) för att passa modellens batch-format.
# Beräknar sannolikheter för alla siffror
# Väljer siffran med högst sannolikhet
# Visar resultatet i Streamlit
    img_array =np.array(img) /255.0

    img_array = img_array.reshape(1, 28, 28)

    prediction =model.predict(img_array)
    predicted_digit =np.argmax(prediction)

    st.write(f"Modellen tror att det är:{predicted_digit}")
