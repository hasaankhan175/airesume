"""
LLM Service

Handles communication with Hugging Face Inference API.
"""

from huggingface_hub import InferenceClient

from config import settings


class LLM:

    def __init__(self):

        self.client = InferenceClient(
            provider="hf-inference",
            api_key=settings.HF_API_TOKEN,
        )

        self.model = settings.LLM_MODEL

    def generate(
        self,
        prompt: str,
        max_tokens: int = 1024,
        temperature: float = 0.3,
    ) -> str:
        """
        Generate a response from the LLM.

        Parameters
        ----------
        prompt : str

        Returns
        -------
        str
        """

        try:

            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert ATS recruiter, HR specialist, "
                            "and resume reviewer."
                        ),
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                max_tokens=max_tokens,
                temperature=temperature,
            )

            return completion.choices[0].message.content

        except Exception as e:

            raise RuntimeError(
                f"LLM Error: {e}"
            )