import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def extract_signals(user_text):

    prompt = f"""
You are a professional Food Safety Inspector AI.

Analyze the customer's food review carefully.

Your objectives:

1. Detect food hygiene and safety issues.
2. Infer possible risks even if not directly mentioned.
3. Determine the severity level.
4. Explain your reasoning professionally.
5. Recommend whether the food is safe to consume.

Possible food safety concerns include:

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

Return ONLY:

Assessment Summary:
A professional food safety assessment written in 3-5 sentences.

Severity:
Low, Medium or High

Recommendation:
Safe to Consume / Consume With Caution / Do Not Consume

Customer Review:
{user_text}
"""

    try:

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:

        print("GEMINI ERROR:", e)

        return f"""
Assessment Summary:
Gemini Error: {str(e)}

Severity:
Unknown

Recommendation:
Unable to Analyze
"""