"""
LLM Service

Handles communication with Hugging Face Inference API.
"""

from huggingface_hub import InferenceClient

from config import settings


class LLM:
    """Wrapper for Hugging Face chat completion."""

    def __init__(self):

        self.client = InferenceClient(
            api_key=settings.HF_API_TOKEN
        )

        self.model = settings.LLM_MODEL

    def generate(
        self,
        prompt: str,
        system_prompt: str = "You are an expert ATS recruiter and resume reviewer.",
        max_tokens: int = 1024,
        temperature: float = 0.3,
    ) -> str:

        try:

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                max_tokens=max_tokens,
                temperature=temperature,
            )

            return response.choices[0].message.content

        except Exception as e:
            raise RuntimeError(f"LLM Error: {e}")