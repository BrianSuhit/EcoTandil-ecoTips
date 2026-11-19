from google import genai

client = genai.Client()

print("--- SELECCIONÁ EL MATERIAL ---")
print("1. Vidrio")
print("2. Cartón")
print("3. Botellas de plástico")
print("4. Latas")
print("5. Aerosoles")
print("6. Telgopor")
print("7. Envases de tetra brick")
print("8. Rezagos informáticos")
print("9. Aceite de cocina usado")
print("10. Sachets")

opcion_mat = input("\nIngresá el número del material (1-10): ")
match opcion_mat:
    case "1":
        residuo = "Vidrio"
    case "2":
        residuo = "Cartón"
    case "3":
        residuo = "Botellas de plástico"
    case "4":
        residuo = "Latas"
    case "5":
        residuo = "Aerosoles"
    case "6":
        residuo = "Telgopor"
    case "7":
        residuo = "Envases de tetra brick"
    case "8":
        residuo = "Rezagos informáticos"
    case "9":
        residuo = "Aceite de cocina usado"
    case "10":
        residuo = "Sachets"
    case _:
        residuo = "Material reciclable general"

print("\n--- SELECCIONÁ EL PUNTO LIMPIO ---")
print("1. Centro (Rivadavia 250)")
print("2. Norte (Darragueira y Jurado)")
print("3. Estación Oeste (Reynoso al 2030)")
print("4. Villa Italia Norte (Pasteur 1150)")
print("5. Juan B. Justo (Av. Juan B. Justo 238)")
print("6. Cerro Leones (Plaza Democracia: Maderni y Lamberto)")
print("7. Vela (Corralón Municipal)")
print("8. Gardey (Corralón Municipal)")

opcion_cen = input("\nIngresá el número del centro (1-8): ")
match opcion_cen:
    case "1":
        centro = "Centro (Rivadavia 250)"
    case "2":
        centro = "Norte (Darragueira y Jurado)"
    case "3":
        centro = "Punto Limpio estación Oeste (Reynoso al 2030)"
    case "4":
        centro = "Villa Italia Norte (Pasteur 1150)"
    case "5":
        centro = "Juan B. Justo (Av. Juan B. Justo 238)"
    case "6":
        centro = "Cerro Leones - plaza Democracia (Maderni y Lamberto)"
    case "7":
        centro = "Vela (Corralón Municipal)"
    case "8":
        centro = "Gardey (Corralón Municipal)"
    case _:
        centro = "el Punto Limpio más cercano"

print(f"\nGenerando un tip para: {residuo} -> Destino: {centro}...")

interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    system_instruction=(
        "Sos un asistente ambiental de Tandil que escribe para chicos de primaria "
        "y secundaria. Generá un tip breve, claro, amable y fácil de entender sobre "
        "cómo cuidar el ambiente al separar el residuo indicado. No uses palabras "
        "difíciles ni des instrucciones peligrosas. Para residuos que puedan ser "
        "peligrosos o necesitar cuidados, indicá que deben pedir ayuda a una persona "
        "adulta. Terminá siempre diciendo que lo lleven al Punto Limpio seleccionado."
    ),
    input=f"Residuo: {residuo}. Punto Limpio seleccionado: {centro}.",
    stream=True
)

for event in interaction:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)