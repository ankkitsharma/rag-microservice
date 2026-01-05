import hashlib
from app.embeddings.base import Embedder


class FakeEmbedder(Embedder):
    def __init__(self, dimension: int = 8):
        self._dimension = dimension

    def dimension(self) -> int:
        return self._dimension

    def embed(self, text: str):
        # Deterministic hash -> vector
        h = hashlib.sha256(text.encode()).digest()

        vector = []
        for i in range(self._dimension):
            # Map bytes -> float range [-1, 1]
            value = (h[i] / 255.0) * 2 - 1
            vector.append(value)

        return vector
