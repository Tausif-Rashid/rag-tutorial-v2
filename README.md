# Local OCR+RAG 

A simple Retrieval-Augmented Generation (RAG) and OCR pipeline using Python, LangChain, Chroma, tesseract and Ollama.

## Features
- OCR PDF to TXT (supports scanned/image PDFs)
- Add TXT files to a Chroma vector database with Nomic embeddings via Ollama
- Query the database using Deepseek 7B LLM via Ollama (RAG). Model can be changed.

## Setup

1. **Install dependencies:**
	```sh
	pip install -r requirements.txt
	```
	- Install [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) and [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and add them to your PATH. For Poppler , extract in C:\program files\.
    For tesseract you may download [installer](https://github.com/UB-Mannheim/tesseract/wiki)  

2. **Start Ollama and pull models:**
	```sh
	ollama pull nomic-embed-text
	ollama pull deepseek-llm-7b
	```
    ```sh
    ollama serve
	```
    

## Usage

1. **OCR PDFs:**
    - For searchable PDF and txt, place in  [`data`](data ) folder.
	- Place other PDFs in the [`ocr`](ocr ) folder.
	- Run OCR:
	  ```sh
	  python ocr_pdf_txt.py
	  ```
	- TXT files will be saved in the [`data`](data ) folder.

2. **Populate the vector database:**
	```sh
	python populate_database.py --reset
	```
    without --reset flag if you want to update existing db with new documents.
    1st time running may take a while.

3. **Query with RAG:**
	```sh
	python query_data.py "Your question here"
	```

## Acknowledgement

- Basic Rag pipeline is forked from this [Repo](https://github.com/pixegami/rag-tutorial-v2). Thanks to [Pixegami](https://github.com/pixegami).


## Notes
- Requires Ollama running locally.
- For best results, ensure all dependencies are installed and in your PATH.
 