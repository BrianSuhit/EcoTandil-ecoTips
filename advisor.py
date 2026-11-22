from dataclasses import dataclass

from google import genai
from google.genai.errors import APIError


@dataclass(frozen=True)
class TipResult:
    text: str
    is_error: bool = False


class EcoAdvisor:
    def __init__(self):
        self.client = genai.Client()
        self.system_instruction = (
            "Sos un asistente ambiental de Tandil que escribe para chicos de"
            " primaria y secundaria. Generá un tip breve, claro, amable y fácil de"
            " entender sobre cómo cuidar el ambiente al separar el residuo"
            " indicado. No uses palabras difíciles ni des instrucciones"
            " peligrosas. Para residuos que puedan ser peligrosos o necesitar"
            " cuidados, indicá que deben pedir ayuda a una persona adulta. Terminá"
            " siempre diciendo que lo lleven al Punto Limpio seleccionado."
        )

    def generate_tip(self, residuo: str, centro: str) -> TipResult:
        try:
            interaction = self.client.interactions.create(
                model="gemini-3.5-flash-lite",
                system_instruction=self.system_instruction,
                input=f"Residuo: {residuo}. Punto Limpio seleccionado: {centro}.",
                stream=False,
            )
            return TipResult(interaction.output_text)
        except APIError as e:
            print(f"Error en EcoAdvisor: {e}")
            return TipResult(
                "Gemini devolvió un error. Revisá la clave de API o intentá "
                "nuevamente más tarde.",
                is_error=True,
            )
        except Exception as e:  # noqa: BLE001
            print(f"Error inesperado en EcoAdvisor: {e}")
            return TipResult(
                "No se pudo conectar con el asistente ambiental. Revisá tu "
                "conexión a internet e intentá nuevamente.",
                is_error=True,
            )