from __future__ import annotations

from typing import Any, Dict, Protocol, runtime_checkable


@runtime_checkable
class MetricsBackend(Protocol):
    def record(self, name: str, value: Any) -> None:
        ...


_backends: Dict[str, MetricsBackend] = {}


def register_backend(name: str, backend: MetricsBackend) -> None:
    _backends[name] = backend


def get_backend(name: str) -> MetricsBackend:
    return _backends[name]


# example in-memory backend
class MemoryBackend:
    def __init__(self) -> None:
        self.storage: Dict[str, Any] = {}

    def record(self, name: str, value: Any) -> None:
        self.storage[name] = value


register_backend("memory", MemoryBackend())
