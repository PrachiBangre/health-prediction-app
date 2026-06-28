from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def predict_health(glucose, haemoglobin, cholesterol):

    try:

        prompt = f"""
Patient blood test values:

Glucose: {glucose}
Haemoglobin: {haemoglobin}
Cholesterol: {cholesterol}

Predict possible health risks in 1-2 professional medical sentences.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        return "Unable to generate AI health remarks at the moment."    #return f"AI Service Error: {str(e)}"