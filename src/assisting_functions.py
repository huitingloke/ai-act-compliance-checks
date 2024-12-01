import gradio as gr
from pypdf import PdfReader
import chromadb
from gpt4all import GPT4All
import docx

client = chromadb.PersistentClient(path="./src/eu_ai_act")
collection = client.get_or_create_collection(name="EU_AI_ACT")

model_selection = {
    "phi4kmodel": "Phi-3-mini-4k-instruct.Q4_0.gguf",
    "llama8bmodel": "Meta-Llama-3-8B-Instruct.Q4_0.gguf",
    "vigogne13bmodel": "vigogne-2-13b-instruct.Q5_K_M.gguf",
}
one_shot_prompt = """
    Above are the relevant statutes from the EU Artificial Intelligence Act, on High-Risk AI Systems. 
    Only determine your answers based on the context provided above. 
    You are an assistant which detects compliance issues. If there are no issues within the following documents, tell the user what they are complying with.
    For instance: 

    If there are issues, list them in a bullet point format. Your reply should be no longer than five hundred words. 

    Here is an example of a reply you should provide: 

    "The following documents are compliant with the EU AI Act:
    * This policy applies to all employees, contractors, and third-party vendors involved in the development, deployment, and use of the AI system for employee selection
    * Regularly monitor the AI model for bias and take corrective action. 

    However, these have not complied:
    * Incident Reporting: Establish procedures for reporting incidents related to the AI system, such as bias, discrimination, or security breaches. -- You should do more to abide by these rules. Give examples for procedures.
    * Transparency: Be transparent about the use of AI in the hiring process. -- As per the Act, you are additionally required to have a person of contact. 
    "

    Below are the relevant policies from the user. 
"""

def test_models(compliance_query):

    final_result =[]
    relevant_documents = ""

    results = collection.query(
        query_texts=[compliance_query], # Chroma automatically embeds this
        n_results=2 # How many results to return
    )

    print(results)
    for document in results["documents"][0]:
        relevant_documents += document

    for model in model_selection:

        model = GPT4All(
            model_name=model_selection[model],
            verbose=True,
            device="cuda" # Using NVIDIA GeForce RTX3070 GPU for testing purposes, 8GB VRAM (I think.)
        )
        with model.chat_session():

            final_prompt = str(relevant_documents) + str(one_shot_prompt) + str(compliance_query)
            final_result += model.generate(final_prompt, max_tokens=4096)

            final_result += "\n-----------------------\n"
    
    with open("OUTPUT.txt", "w") as my_file:
        for item in final_result:
            
            my_file.write(str(item))

    return "".join([str(ch) for ch in final_result])

def get_docx_text(filename): #credit: https://stackoverflow.com/questions/25228106/
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def process_file(file:gr.File) -> str:

    transcribed_words = str()
    reader = PdfReader(file)

    for page in reader.pages:
        transcribed_words += page.extract_text()

    return transcribed_words