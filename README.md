# 🌱 EcoTandil - EcoTips

>  **MVP de concientización ambiental y reciclaje urbano para estudiantes de primaria y secundaria.**

## Demostración

### Probar la aplicación
> 👉 **Demo interactiva:** [Probar la aplicación en vivo en Streamlit](https://ecotandil-ecotips-fcgbpltcyjzgwwo6dh6gld.streamlit.app/)

### Vista Previa
> <img width="1919" height="944" alt="ecotips-img-1" src="https://github.com/user-attachments/assets/0108b2d6-3fca-4e40-8051-840adf0beb19" />

## Contexto
 Mientras estaba en la Tandil Tech Week escuchando a Rodrigo Rotonda sobre los ejes de Tandil 2050, no dejaba de hacerme una pregunta: **¿Qué puedo aportar yo como estudiante y futuro AI Engineer a estas metas?**
 
 Ahí nació este prototipo. Cuidar la ciudad, el medioambiente y aprender a reciclar es mucho más un desafío de educación y hábitos que un problema puramente tecnológico. Por eso, apalancándome en otro de los drivers (Educación y Conocimiento), me propuse enfocar este primer proyecto en los más jóvenes.
 
La idea original contemplaba generar imágenes, pero decidí pivotar hacia un asistente de tips rápidos y directos: una interfaz accesible donde el estudiante selecciona el tipo de residuo y el Punto Limpio de destino, y un modelo de lenguaje genera una recomendación personalizada, segura y pedagógica.

## Decisiones de Diseño y Trade-offs

Para este prototipo (MVP) prioricé la simplicidad y la seguridad de los chicos, asumiendo conscientemente lo que ganaba y lo que resignaba en cada decisión:

**Entrada por menú desplegable (en vez de campo abierto):**
-  ✅ *Pro:* Evito entradas maliciosas o preguntas fuera de tema sin tener que gastar plata ni tokens en filtros complejos de guardrails.
-  ❌ *Contra:* El chico solo puede consultar los residuos y puntos limpios que ya están cargados en la lista fija.

**Prompt enfocado en seguridad infantil:**
-  El sistema evalúa riesgos: si el residuo es peligroso o cortante (como vidrio roto o baterías), exige la supervisión de un adulto en vez de alentar al chico a manipularlo solo.

**Salida en texto simple (en vez de formato JSON):**
-  ✅ *Pro:* El mensaje sale natural, amigable y con el tono adecuado para chicos de primaria y secundaria. 
-  ❌ *Contra:* La respuesta no tiene siempre la misma cantidad exacta de renglones ni un formato rígido. Usar Structure Output en produccion con un framework de fronted mas robusto seria un paso crucial.

## Mejoras a futuro

Cosas que no forman parte de este prototipo pero que son el paso siguiente para llevarlo a la práctica:
-  **Cambiar la arquitectura de despliegue:** Pasar de Streamlit a una API en FastAPI para poder conectar esta misma lógica a un bot de WhatsApp o a una app móvil (Flutter).
-  **Sumar imágenes:** Incorporar generación de imágenes explicativas además del consejo en texto.
-  **Monitoreo y observabilidad:** Medir costos de la API, consumo de tokens, tiempos de respuesta y registro de fallos en tiempo real.

## Stack Tecnológico
- **Lenguaje:** Python 3.14
- **Frontend / UI:** Streamlit
- **LLM:** Google Gemini (`gemini-3.5-flash-lite` vía `google-genai`)

## Estructura del Proyecto
```text
ecotandil-ecotips/
├── app.py       # Interfaz de usuario con Streamlit
├── advisor.py   # Servicio desacoplado para interactuar con Gemini
└── catalogs.py  # Catálogo de residuos y Puntos Limpios de Tandil
```

## Quickstart (Cómo correrlo en local)

### 1. Clonar el repositorio

```bash
git clone https://github.com/BrianSuhit/EcoTandil-ecoTips.git
cd EcoTandil-ecoTips
```

### 2. Instalar dependencias con uv

```bash
uv sync
```

### 3. Configurar variables de entorno

Creá un archivo `.env` en la raíz del proyecto (o exportá la variable en tu terminal):

```env
GEMINI_API_KEY="tu_api_key_aqui"
```

### 4. Iniciar la aplicación

```bash
uv run streamlit run app.py
```
