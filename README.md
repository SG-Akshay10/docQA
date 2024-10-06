# docQA

his repository hosts a fully integrated Retrieval-Augmented Generation (RAG) system designed to provide context-aware and evidence-based responses using large language models (LLMs). This system is designed for applications where retrieving relevant knowledge and generating a conversational response is crucial. The RAG pipeline efficiently combines document ingestion, semantic retrieval, and language model generation to deliver accurate, contextual, and informative answers to user queries.

## Features

* **Data Ingestion & Processing**: Supports PDF document ingestion, extracting, cleaning, and chunking text for optimal retrieval performance.

* **Vector Embedding & Indexing**: Uses Hugging Face or OpenAI models to generate vector embeddings for semantic representation of documents.

* **Semantic Document Retrieval**: Utilizes a combination of BM25, vector retrieval, and hybrid methods to identify the most relevant information.

* **Contextual Response Generation**: Combines retrieved information with language models to produce grounded responses.

* **Interactive User Interface**: Gradio-based UI allows users to interact with the system through queries, document uploads, and dynamic streaming responses.\\

## Components of the RAG System

The RAG system consists of several core components, each playing a crucial role in providing efficient, context-aware responses. Below, we explain these components in detail:

1. **Data Ingestion and Preparation**

The Data Ingestion and Preparation component is responsible for processing raw documents into a structured format suitable for retrieval and response generation. This includes:

`Text Extraction`: Extracting content from documents (e.g., PDFs) using tools like fitz (PyMuPDF).

`Text Cleaning and Normalization`: Removing unwanted characters and normalizing text using regular expressions to ensure consistency.

`Chunking`: Splitting documents into smaller, manageable chunks (nodes) to facilitate efficient retrieval and embedding.

`Embedding Integration`: Generating vector embeddings for each chunk using Hugging Face or OpenAI models to represent the semantic content of the document.

2. **Embedding Generation and Vector Indexing**

The Embedding Generation and Vector Indexing components work together to transform the document chunks into vector representations and organize them for fast retrieval.

`Embedding Generation`: The LocalEmbedding class is used to create high-dimensional vector embeddings for each text chunk. These embeddings capture the semantic meaning of the text, enabling similarity-based retrieval.

`Vector Index Creation`: The LocalVectorStore component generates a vector index from the embeddings. This index is used to store and efficiently retrieve relevant document chunks based on user queries, enabling semantic search.

3. **Retrieval System**

The Retrieval System is responsible for finding the most relevant content from the indexed document embeddings based on a user query.

`Retrieval Methods`: The system uses a combination of vector similarity retrieval, BM25 retrieval (keyword-based), and hybrid approaches to identify the most relevant information.

`Two-Stage Retrieval and Re-ranking`: In some cases, the retrieval process involves multiple stages, including an initial retrieval followed by re-ranking using models like SentenceTransformerRerank to improve accuracy.

4. **Retrieval-Augmented Response Generation**

The Retrieval-Augmented Response Generation component is the core of the RAG system, where retrieved content is used to generate context-aware responses.

`Language Model Integration`: Retrieved document chunks are passed to a language model (e.g., Hugging Face’s Ollama or OpenAI models) for response generation. The model uses both the retrieved context and its pre-trained knowledge to generate accurate and informative answers.

`System Prompts`: Predefined prompts guide the behavior of the language model, ensuring that it uses the retrieved content effectively and provides grounded responses.

5. **Chat Engine and User Interaction**

The Chat Engine component integrates the retrieval and response generation processes to provide an interactive conversational experience.

`Chat Engine Configuration`: The LocalChatEngine class sets up either a basic conversational engine or a retrieval-augmented engine, depending on the availability of relevant content.

`User Interface`: The Gradio-based User Interface allows users to interact with the RAG system by submitting queries, uploading documents, and receiving responses in real-time. The LocalChatbotUI component manages these interactions and provides a dynamic, streaming response experience.

Chat Memory: The system maintains a conversation history using ChatMemoryBuffer, allowing follow-up questions to be contextualized based on previous interactions.

6. **Evaluation and Performance Metrics**

The Evaluation component is designed to assess the quality of both retrieval and response generation.

`Retriever Evaluation`: Metrics such as Mean Reciprocal Rank (MRR) and hit rate are used to evaluate the effectiveness of the retrieval system.

`Response Quality Evaluation`: The generated responses are evaluated based on metrics like faithfulness, relevance, and context alignment to ensure that the system provides accurate and informative answers.

## Installation Guide 


### 2.1. Clone project

```bash
git clone https://github.com/SG-Akshay10/docQA.git
cd rag-chatbot
```

### 2.2 Install

#### 2.2.1 Docker

```bash
docker compose up --build
```

#### 2.2.2 Using script (Ollama, Ngrok, python package)

```bash
source ./scripts/install_extra.sh
```

#### 2.2.3 Install manually

1. **Ollama**

   - MacOS, Windows: Download from [Ollama](https://ollama.com/).
   
   - Linux:
   
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. **Ngrok**

   - MacOS:
   
   ```bash
   brew install ngrok/ngrok/ngrok
   ```

   - Linux:
   
   ```bash
   curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
   | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
   && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
   | sudo tee /etc/apt/sources.list.d/ngrok.list \
   && sudo apt update \
   && sudo apt install ngrok
   ```

3. **Install rag_chatbot Package**

```bash
source ./scripts/install.sh
```

### 2.3 Run

```bash
source ./scripts/run.sh
```

or

```bash
python -m docQA-rag --host localhost
```

   Using Ngrok:

```bash
source ./scripts/run.sh --ngrok
```

### 3. Go to: [http://0.0.0.0:7860/](http://0.0.0.0:7860/) or use the Ngrok link after setup is completed.

## Output 

![image](https://github.com/user-attachments/assets/8514baeb-a0c2-4cf8-893d-3c832586e576)

![image](https://github.com/user-attachments/assets/a3d9178c-8673-4a79-81ee-d62515bd526e)


