import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def sugerir_mejoras(contenido_archivo):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un ingeniero senior que sugiere mejoras limpias y escalables para proyectos Python."},
            {"role": "user", "content": f"Analiza este código y sugiere mejoras:\n\n{contenido_archivo}"}
        ]
    )
    return response.choices[0].message.content
