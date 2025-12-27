from app.processing.chunker import chunk_text


def test_single_chunk_when_text_is_small():
    text = "Hello world"
    chunks = chunk_text(
        text=text,
        upload_id="u1",
        chunk_size=500,
        overlap=50,
    )

    assert len(chunks) == 1
    assert chunks[0]["text"] == "Hello world"
    assert chunks[0]["chunk_index"] == 0


def test_multiple_chunks_with_overlap():
    text = "A" * 600

    chunks = chunk_text(
        text=text,
        upload_id="u1",
        chunk_size=500,
        overlap=50,
    )

    assert len(chunks) == 2

    assert chunks[0]["text"] == "A" * 500
    assert chunks[1]["text"] == "A" * 150


def test_chunk_metadata():
    text = "B" * 600

    chunks = chunk_text(
        text=text,
        upload_id="upload-123",
        chunk_size=500,
        overlap=50,
    )

    for idx, chunk in enumerate(chunks):
        assert chunk["upload_id"] == "upload-123"
        assert chunk["chunk_index"] == idx
