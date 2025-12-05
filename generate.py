
import os
from config.settings import client


def generate_text(prompt: str, model: str = "gpt-4o-mini") -> str:
    """Generate AI text from a prompt."""

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )


    return response.choices[0].message.content