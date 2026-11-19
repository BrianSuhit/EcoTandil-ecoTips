# EcoTips de Tandil

La interfaz web llama a Gemini desde un servidor JavaScript local. La clave se
lee de `GEMINI_API_KEY` en el servidor y no se envía al navegador.

En PowerShell, configurá la variable de entorno y ejecutá:

```powershell
$env:GEMINI_API_KEY = "tu-clave-de-gemini"
node server.js
```

Después abrí http://127.0.0.1:3000. Opcionalmente, podés elegir el modelo con
`GEMINI_MODEL`; por defecto se usa `gemini-3.5-flash-lite`.