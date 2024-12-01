# AI Act Compliannce Checker Using LLMs

This repository is for the LAW4032 class final paper/project, of which I chose both. This is a working proof-of-concept for a vectorized database that provides similar embeddings from a dataset of the third chapter of the EU AI  (High Risk AI Systems) that will check a compliance document against it using a local LLM.

In this case, 3 LLMs were evaluated.

* Phi-3-mini-4k-instruct (“Phi 4K”)
* Meta-Llama-3-8B-Instruct.Q4_0.gguf (“Llama 8B”)
* vigogne-2-13b-instruct.Q5_K_M.gguf (“vigogne 13B”)

## Setup

* Clone the repository
* `virtualenev env` -- Do ensure your virtual environment is at least Python 3.11 to be safe or ChromaDB will NOT run and you will have to install a version of SQLite3 from their website manually
    * `source env/bin/activate` -- Mac users
    * `env/Scripts/activate` -- Windows users
*  `pip install -r requirements.txt`
* Under `./src/`, there is a script under `ai_act_chroma_setup.py` that will NOT set up the database as it requires you to copy and paste every single clause (yes, clause) from the EU AI Act into a list in the file. I am very sorry, I could not get it working and manually added every clause.
    * If you need me to, please email me and I will try and write an actual script. 
* To start the app, type `python ./src/main.py` in your terminal
    * On Mac, it would be `python3 ./src/main.py`
* To stop the app, use `Ctrl + C` in your terminal