from app.embeddings.fake import FakeEmbedder


def test_fake_embedder_dimension():
    embedder = FakeEmbedder(dimension=8)
    vector = embedder.embed("hello")

    assert len(vector) == 8


def test_fake_embedder_is_deterministic():
    embedder = FakeEmbedder(dimension=8)

    v1 = embedder.embed("hello")
    v2 = embedder.embed("hello")

    assert v1 == v2


def test_fake_embedder_changes_with_text():
    embedder = FakeEmbedder(dimension=8)

    v1 = embedder.embed("hello")
    v2 = embedder.embed("world")

    assert v1 != v2
