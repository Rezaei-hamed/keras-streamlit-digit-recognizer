# Rapport: Model Serving med Keras och Streamlit

## Syfte

Jag ville lära mig hur man kan ta en färdigtränad modell och göra den användbar i en riktig app, inte bara i en Jupyter-notebook. Jag ville också förstå hur Streamlit fungerar, särskilt hur man undviker att ladda om modellen varje gång.

## Området och dess relevans

Jag valde Streamlit tillsammans med en Keras-modell, eftersom jag redan hade lite erfarenhet av Keras men aldrig använt Streamlit. Det här är relevant för en Data Scientist eftersom man ofta behöver visa upp sina resultat för andra som inte kan koda. Streamlit är ett populärt verktyg för just det.

## Viktiga begrepp

**Model serving** betyder att man gör en färdig modell tillgänglig så att andra kan använda den, till skillnad från att bara träna den.

**`st.cache_resource`** gör att en funktion bara körs en gång. Det behövs eftersom Streamlit kör om hela filen varje gång användaren gör något (till exempel ritar på canvasen). Utan cache skulle modellen laddas om från disk hela tiden, vilket är onödigt långsamt.

**Preprocessing av bilden** betyder att man gör om användarens ritning så att den ser ut som bilderna modellen tränades på: gråskala, 28×28 pixlar, och samma färger (ljus siffra på svart bakgrund).

## Genomförande

Jag tränade en enkel modell i Keras på MNIST-datasetet, som redan finns inbyggt i Keras. Modellen har ett `Flatten`-lager, ett `Dense`-lager med 128 neuroner, och ett sista lager med 10 neuroner (en för varje siffra 0–9). Jag tränade i 5 epoker och sparade modellen med `model.save()`.

Sen byggde jag en Streamlit-app med `streamlit-drawable-canvas`, ett bibliotek som låter användaren rita med musen. Jag satte vit färg på svart bakgrund, samma som i MNIST. När användaren ritat, gör jag om bilden till gråskala, skalar ner den till 28×28 pixlar, och skickar den till modellen med `model.predict()`.

Ett problem jag stötte på var att canvas-biblioteket krävde en extra inställning (`return_image_data=True`) för att jag skulle kunna komma åt bilden alls. Utan den fick jag ett felmeddelande.

## Resultat

Modellen fick 97,58 % rätt på testdatan. Appen fungerar och ger en prediktion direkt när man ritar. För siffror som är tydligt ritade (till exempel 1, 3, 7) fungerar det bra och stabilt.

## Begränsningar och möjliga förbättringar

Modellen gissar fel oftare på siffror som är ritade med musen jämfört med testdatan, särskilt på siffror som liknar varandra, som 8 och 9. Jag tror det beror på att siffrorna i MNIST alltid är centrerade och ungefär lika stora, medan man kan rita var som helst och i vilken storlek som helst på canvasen.

En förbättring hade varit att hitta var på bilden själva siffran finns, klippa ut bara den delen, och sedan centrera den likadant som i MNIST. Jag hann identifiera problemet men inte implementera lösningen fullt ut.

## Koppling till yrkesrollen

Att kunna paketera en modell i ett enkelt gränssnitt är användbart i jobbet som Data Scientist, till exempel för att visa upp en modell för kollegor eller göra ett snabbt test-verktyg innan man bygger något större.

## Källor

- Streamlit officiell dokumentation (docs.streamlit.io)
- GitHub-repot för streamlit-drawable-canvas
- Keras dokumentation för mnist, Sequential och model.save()/load_model()

## Självreflektion

**Vad lärde du dig som du inte kunde innan?**
Jag lärde mig hur man kopplar ihop en färdig modell med ett användargränssnitt, och hur Streamlit cachar saker för att inte bli långsamt.

**Vad var svårast?**
Att förstå varför modellen gissade fel på mina egna ritningar trots att den var bra på testdatan. Jag var tvungen att tänka igenom hela processen från ritning till prediktion för att hitta orsaken.

**Vilket tekniskt val är du mest nöjd med?**
Att använda `st.cache_resource` för modellen, eftersom det visar att jag förstod varför det behövs, inte bara att koden fungerade.

**Vad hade du gjort annorlunda?**
Testat appen med egna ritningar tidigare, så jag hade upptäckt problemet med 8:or och 9:or i tid att lösa det.

**Nästa steg?**
Implementera beskärning och centrering av ritningen, och lägga till en knapp för att rensa canvasen.

**G eller VG?**
[skriv din egen bedömning här]