# Keras + Streamlit Digit Recognizer

Det här projektet är en enkel Streamlit-app som kan känna igen handskrivna siffror.

Användaren ritar en siffra mellan 0 och 9 med musen. Sedan använder appen en Keras-modell som är tränad på MNIST för att gissa vilken siffra som har ritats.

Appen visar sedan vilken siffra modellen tror att det är och hur säker modellen är på sin gissning.


## Installation

1. Klona repot
2. Skapa en virtuell miljö: `python -m venv .venv`
3. Aktivera den: `source .venv/Scripts/activate`
4. Installera beroenden: `pip install -r requirements.txt`

## Användning

Kör appen:
```bash
streamlit run app.py
```

Appen öppnas i webbläsaren på `http://localhost:8501`. Rita en siffra (0–9) på den svarta canvasen så visar modellen en prediktion i realtid.

## Projektstruktur

```
keras-streamlit-demo/
- model/
  - mnist_model.keras
- app.py
- train_model.py
- requirements.txt
- README.md
```

## Om modellen och data

Modellen är en enkel neural network (Flatten + Dense-lager) tränad på MNIST-datasetet, som ingår i Keras (`keras.datasets.mnist`).
 Modellen uppnådde 97.70% noggrannhet på testdatan. För att träna om modellen,
  kör:

```bash
python train_model.py
```