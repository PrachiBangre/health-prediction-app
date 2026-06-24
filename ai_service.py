from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def predict_health(glucose, haemoglobin, cholesterol):

    try:
        # OpenAI or Gemini call here
        prompt = f"""
    Patient blood test values:

    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Predict possible health risks in one short sentence.
    """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception:

        if glucose > 140 and cholesterol > 240:
            return "Possible diabetes and cardiovascular risk."

        elif glucose > 140:
            return "Possible diabetes risk."

        elif cholesterol > 240:
            return "Possible cardiovascular risk."

        elif haemoglobin < 12:
            return "Possible anemia risk."

        return "Values appear within normal range."