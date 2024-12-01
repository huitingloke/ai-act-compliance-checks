import chromadb
import uuid # chromadb requires UUIDs for document uploads

chroma_client = chromadb.PersistentClient(path="./src/eu_ai_act")# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
collection = chroma_client.get_or_create_collection(name="EU_AI_ACT")
# switch `add` to `upsert` to avoid adding the same documents every time
num = 1

documents = [
] #Input each clause as a list item
for document in documents:

    stringed_number = str(num)
    collection.upsert(
        documents=[
            document
        ],
        metadatas=[
            {"chapter": "ANNEX 3: High-Risk AI Systems Referred to in Article 6(2)",
            "section": "",
            "article": "",
            "clause": stringed_number}
        ],
        ids=[str(uuid.uuid4())] #ID is required for upserting
    )

    num += 1

print("------------------------------")
results = collection.query(
    query_texts=["quality management system, risk, danger"],
    n_results=7 
)

print(results)