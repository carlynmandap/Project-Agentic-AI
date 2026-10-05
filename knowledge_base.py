import os
import re
import chromadb
import ollama


# -----------------------------
# Configuration
# -----------------------------

KB_FOLDER = "knowledge"
CHROMA_PATH = "./chroma_db"

CHAT_MODEL = "qwen3:4b"
EMBEDDING_MODEL = "nomic-embed-text"


# -----------------------------
# ChromaDB
# -----------------------------

chroma_client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

collection = chroma_client.get_or_create_collection(
    name="home_knowledge"
)


# -----------------------------
# Read Markdown files
# -----------------------------

def load_markdown_files():

    documents = []

    for filename in os.listdir(KB_FOLDER):

        if filename.endswith(".md"):

            filepath = os.path.join(
                KB_FOLDER,
                filename
            )

            with open(
                filepath,
                "r",
                encoding="utf-8"
            ) as file:

                text = file.read()

            documents.append({
                "filename": filename,
                "text": text
            })

    return documents


# -----------------------------
# Split document into chunks
# -----------------------------

def chunk_text(text, max_chars=800):

    # Split based on Markdown headings
    sections = re.split(
        r"\n(?=## |### )",
        text
    )

    chunks = []

    for section in sections:

        section = section.strip()

        if not section:
            continue

        # If section is small enough, keep it together
        if len(section) <= max_chars:

            chunks.append(section)

        else:

            # Split larger sections into smaller pieces
            words = section.split()

            current_chunk = ""

            for word in words:

                if len(current_chunk) + len(word) + 1 <= max_chars:

                    current_chunk += " " + word

                else:

                    chunks.append(
                        current_chunk.strip()
                    )

                    current_chunk = word

            if current_chunk:
                chunks.append(
                    current_chunk.strip()
                )

    return chunks


# -----------------------------
# Create embedding
# -----------------------------

def create_embedding(text):

    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=text
    )

    return response["embeddings"][0]


# -----------------------------
# Build Knowledge Base
# -----------------------------

def build_knowledge_base():

    documents = load_markdown_files()

    if not documents:

        print("No Markdown files found.")

        return

    total_chunks = 0

    for document in documents:

        filename = document["filename"]
        text = document["text"]

        chunks = chunk_text(text)

        print(
            f"{filename}: "
            f"{len(chunks)} chunks"
        )

        for index, chunk in enumerate(chunks):

            embedding = create_embedding(chunk)

            chunk_id = (
                f"{filename}_chunk_{index}"
            )

            collection.upsert(
                ids=[chunk_id],

                documents=[chunk],

                embeddings=[embedding],

                metadatas=[{
                    "source": filename,
                    "chunk": index
                }]
            )

            total_chunks += 1

    print()
    print(
        f"Knowledge base built successfully."
    )

    print(
        f"Total chunks: {total_chunks}"
    )


# -----------------------------
# Search Knowledge Base
# -----------------------------

def search_knowledge(
    question,
    number_of_results=3
):

    question_embedding = create_embedding(
        question
    )

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=number_of_results
    )

    documents = results.get(
        "documents",
        [[]]
    )[0]

    return documents

if __name__ == "__main__":
    build_knowledge_base()