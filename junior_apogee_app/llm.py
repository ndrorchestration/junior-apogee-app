from __future__ import annotations

from typing import Any, Dict


# placeholder LLM wrapper; real implementation would call Anthropic/OpenAI/etc.

def call_llm(prompt: str, model: str = "claude-2") -> str:
    """Return a mocked LLM response for the given prompt."""
    # in production, import and call anthropic.Client or similar
    return f"[mocked {model} answer] {prompt}"
