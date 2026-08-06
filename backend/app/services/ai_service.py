from groq import Groq
from app.core.config import settings
import json

client = Groq(
    api_key=settings.groq_api_key
)

def ai_analyze(cv_text: str, job_description: str):
    prompt = f"""
    Du bist ein professioneller HR-Experte und technischer Recruiter mit Erfahrung in der Bewertung von Bewerbungen.

    Deine Aufgabe ist es, den Lebenslauf des Kandidaten mit der Stellenbeschreibung zu vergleichen und eine objektive Analyse zu erstellen.

    Lebenslauf:
    {cv_text}

    Stellenbeschreibung:
    {job_description}

    Analysiere die Übereinstimmung zwischen den Fähigkeiten des Kandidaten und den Anforderungen der Stelle.

    Regeln:
    - Berechne den Match Score realistisch zwischen 0 und 100 basierend auf der tatsächlichen Übereinstimmung.
    - Berücksichtige nur Informationen, die im Lebenslauf vorhanden sind.
    - Erfinde keine Erfahrungen, Projekte, Technologien oder Fähigkeiten.
    - Schreibe unter "skills" nur Fähigkeiten, die im Lebenslauf vorhanden sind UND direkt zu den Anforderungen der Stelle passen.
    - Schreibe keine allgemeinen Fähigkeiten wie "Teamfähigkeit", "Motivation" oder "Flexibilität", außer sie werden ausdrücklich in der Stellenbeschreibung gefordert und sind im Lebenslauf belegt.
    - Schreibe unter "missing_skills" nur wichtige Anforderungen aus der Stellenbeschreibung, die im Lebenslauf nicht nachgewiesen werden können.
    - Vergleiche Technologien, Programmiersprachen, Frameworks, Tools und Berufserfahrung besonders genau.
    - Gib Verbesserungsvorschläge, die dem Kandidaten helfen, besser auf diese konkrete Stelle zu passen.
    - Erstelle ein professionelles Anschreiben, aber verwende ausschließlich Informationen aus dem Lebenslauf.
    - Behaupte niemals, dass der Kandidat Erfahrung mit einer Technologie hat, wenn diese nicht im Lebenslauf steht.

    Falls der Lebenslauf oder die Stellenbeschreibung ungültig sind (z.B. nur einzelne Buchstaben, Zahlen, zufällige Zeichen oder keine echten Informationen enthalten), gib zurück:
    match_score: 0
    skills: []
    missing_skills: []
    improvements: ["Bitte geben Sie einen gültigen Lebenslauf und eine gültige Stellenbeschreibung ein."]
    cover_letter: "Bitte geben Sie einen gültigen Lebenslauf und eine gültige Stellenbeschreibung ein."

    Antworte ausschließlich als gültiges JSON ohne Markdown, ohne ``` und ohne zusätzliche Erklärungen.

    Format:
    {{
      "match_score": 0,
      "skills": [],
      "missing_skills": [],
      "improvements": [],
      "cover_letter": ""
    }}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    ai_response = response.choices[0].message.content
    clean_json = ai_response.replace("```json","").replace("```","").strip()
    result_dict = json.loads(clean_json)

    return result_dict

