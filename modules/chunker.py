from typing import List, Dict
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    return splitter.split_text(text)

def chunk_pages(pages: List[Dict], chunk_size: int = 500, chunk_overlap: int = 50) -> List[Dict]:
    all_chunks = []
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )

    for page in pages:
        raw_text = page.get("text", "")
        page_num = page.get("page_num", None)
        source = page.get("source", None)

        if not raw_text.strip():
            continue

        chunks = splitter.split_text(raw_text)
        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "text": chunk,
                "metadata": {
                    "page_num": page_num,
                    "chunk_index": i,
                    "source": source
                }
            })
    return all_chunks
