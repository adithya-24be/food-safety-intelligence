import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
else:
    model = None


def extract_signals(user_text):

    if model is None:
        return """
Assessment Summary:
Gemini API key not configured.

Severity:
Unknown

Recommendation:
Unable to Analyze
"""

    prompt = f"""
You are a food-safety decision-support assistant. You help summarize a customer
report for a human reviewer; you do not diagnose illness, confirm contamination,
or replace a food-safety authority.

Analyze the customer's food review carefully.

Objectives:
1. Detect food hygiene and safety issues.
2. Infer possible risks.
3. Determine severity.
4. Explain reasoning.
5. Recommend whether food is safe.

Possible concerns:
- bad smell
- sour smell
- rotten smell
- damaged packaging
- cold food
- undercooked chicken
- undercooked meat
- slimy vegetables
- mold
- expired food
- contamination
- unusual taste
- stale food
- food poisoning symptoms
- improper storage

Return ONLY this exact structure. Use only signal names from the allowed list;
if none apply, write "none". Do not invent facts.

Assessment Summary:
(3-5 sentences)

Detected Signals:
comma-separated signal names or none

Severity Level:
Low, Medium or High

Recommendation:
Monitor / Consume With Caution / Do Not Consume

Customer Review:
{user_text}
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:

        print("GEMINI ERROR:", str(e))

        return f"""
Assessment Summary:
Gemini Error: {str(e)}

Severity:
Unknown

Recommendation:
Unable to Analyze
"""
