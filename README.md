# EcoTips de Tandil

EcoTips es un prototipo de aplicación del microecosistema de Tandil 2050, dentro
del Driver de Medioambiente y Sustentabilidad. Está pensado para acercar la
separación de residuos y el uso de los Puntos Limpios de Tandil a chicos y
chicas, con tips breves y fáciles de entender.

## Qué permite hacer

- Elegir un material reciclable.
- Seleccionar un Punto Limpio de Tandil.
- Generar con Gemini un tip adecuado para chicos.
- Recordar pedir ayuda a una persona adulta cuando el residuo requiera cuidados.

El prototipo actual funciona desde la consola con Python (`main.py`).

## Ejecutar

Requisitos: Python 3.14 o posterior, [uv](https://docs.astral.sh/uv/) y una
clave de Gemini.

En PowerShell, instalá las dependencias, configurá la clave como variable de
entorno e iniciá la aplicación:

```powershell
uv sync
$env:GEMINI_API_KEY = "tu-clave-de-gemini"
uv run main.py
```

La clave se lee desde `GEMINI_API_KEY`; no la guardes en el código ni la
compartas.
