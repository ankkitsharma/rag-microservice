def chunk_text(text: str, upload_id: str, chunk_size: int, overlap: int):
    if overlap >= chunk_size:
        raise ValueError("Overlap must be less than chunk size")

    chunks = []
    start = 0
    index = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk_text = text[start:end]

        chunks.append(
            {
                "upload_id": upload_id,
                "chunk_index": index,
                "text": chunk_text,
            }
        )

        index += 1
        start = end - overlap

    return chunks
