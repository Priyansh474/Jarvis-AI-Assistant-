So sir i have created the ai assistent as you instructed sir, hope my project meet your expectaions.
sorry i done this much only because of my end sem exams are starting from tuesday.
im thinking to add voice feature and some ui enchancement but cant.

I used html,css,js for frontend and python for backend data process.
and pinecone for vector database.
used llm - Meta-Llama-3-8B-Instruct (quantized: Q4_K_M);
technologies- KoboldCpp,FastAPI Backend,LLaMA Model File (.gguf).
  
---------------------------------------------------------------------------------------------------------------------------
Step 1 — Start the AI Model
In VS Code, open a New Terminal
Run this:

cd JARVIS/Llama
.\koboldcpp.exe --model "Meta-Llama-3-8B-Instruct.Q4_K_M.gguf" --usecublas --gpulayers 14 --contextsize 4096 --multiuser --port 5001

Leave this terminal running. Do not close it.

Step 2 — Start the Backend
Open another New Terminal in VS Code

Run:
cd JARVIS/backend
python -m uvicorn main:app --reload --port 8000


Leave this one running too.

Step 3 — Open the Chat UI

Go to this folder:

JARVIS/frontend


Double-click index.html

Chat with your AI 🎉

🧠 To Add Your Own Notes

Put your text file here:

JARVIS/backend/data/


Then run this in terminal:

cd JARVIS/backend
python ingest.py


Restart backend:

python -m uvicorn main:app --reload --port 8000



