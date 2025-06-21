# Mensageiro Criptografado com AES em Python

## 📖 Visão Geral

Este projeto consiste em um sistema de chat simples via linha de comando (CLI) que permite a troca de mensagens criptografadas entre um cliente e um servidor. A criptografia é realizada utilizando o algoritmo AES (Advanced Encryption Standard).

Este trabalho foi desenvolvido como parte da avaliação da disciplina de **Biohacking, Criptografia e Deep Web** da **Faculdade Paraíso**. O objetivo é demonstrar a aplicação prática de conceitos de criptografia simétrica em uma comunicação básica.

## ✨ Funcionalidades

* Comunicação cliente-servidor utilizando sockets TCP/IP.
* Criptografia das mensagens transferidas usando AES no modo CBC.
* Utilização de uma chave secreta pré-compartilhada (derivada de uma senha no código) para as operações de criptografia e descriptografia.
* Interface de linha de comando para interação do usuário (envio e visualização de mensagens).

## ⚙️ Pré-requisitos

* Python 3.6 ou superior.
* `pip` (gerenciador de pacotes do Python, geralmente incluído na instalação do Python).

## 🚀 Configuração e Instalação

Siga os passos abaixo para configurar o ambiente e executar o projeto:

1.  **Copie os Arquivos do Projeto:**
    Certifique-se de que os arquivos `server.py`, `client.py`, e `aes_utils.py` estejam na mesma pasta no seu computador.

2.  **Navegue até a Pasta do Projeto:**
    Abra o seu terminal ou prompt de comando e use o comando `cd` para navegar até a pasta onde você salvou os arquivos.
    ```bash
    cd caminho/para/sua/pasta/do/projeto
    ```

3.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    Um ambiente virtual isola as dependências do seu projeto, evitando conflitos com outros pacotes Python instalados no seu sistema.
    ```bash
    # Crie o ambiente virtual (ex: chamado 'venv')
    python3 -m venv venv

    # Ative o ambiente virtual
    # No Linux ou macOS:
    source venv/bin/activate
    # No Windows (Prompt de Comando):
    # venv\Scripts\activate.bat
    # No Windows (PowerShell):
    # venv\Scripts\Activate.ps1
    ```
    Você saberá que o ambiente está ativo pois o nome dele (ex: `(venv)`) aparecerá no início do seu prompt do terminal.

4.  **Instale a Biblioteca `cryptography`:**
    Com o ambiente virtual ativo, instale a biblioteca necessária:
    ```bash
    pip install cryptography
    ```

## 🛠️ Como Usar

1.  **Verifique a Senha Compartilhada:**
    É crucial que a variável `SENHA_COMPARTILHADA` nos arquivos `server.py` e `client.py` seja **exatamente a mesma**. Esta senha é usada para gerar a chave de criptografia.
    ```python
    # Exemplo (presente em server.py e client.py)
    SENHA_COMPARTILHADA = "minhasenhasupersecreta12345678"
    ```
    Altere esta senha para uma de sua preferência, mas garanta que seja idêntica em ambos os arquivos.

2.  **Execute o Servidor:**
    * Abra um terminal (com o ambiente virtual ativado).
    * Navegue até a pasta do projeto.
    * Execute o script do servidor:
        ```bash
        python server.py
        ```
    * O servidor iniciará e aguardará conexões. Você deverá ver uma mensagem como: `Aguardando nova conexão em 0.0.0.0:65432...`

3.  **Execute o Cliente:**
    * Abra **outro** terminal (também com o ambiente virtual ativado).
    * Navegue até a pasta do projeto.
    * Execute o script do cliente:
        ```bash
        python client.py
        ```
    * O cliente tentará se conectar ao servidor. Se a conexão for bem-sucedida, você verá: `Conectado ao servidor em 127.0.0.1:65432`.

## 💬 Exemplo de Uso Básico

Uma vez que o servidor está rodando e o cliente está conectado:

1.  **No terminal do Cliente:**
    * O prompt `Cliente:` aparecerá. Digite sua mensagem e pressione Enter.
        ```
        Cliente: Olá servidor, tudo bem? Essa é uma mensagem de teste!
        ```

2.  **No terminal do Servidor:**
    * A mensagem enviada pelo cliente aparecerá descriptografada:
        ```
        Cliente (127.0.0.1:<porta_do_cliente>): Olá servidor, tudo bem? Essa é uma mensagem de teste!
        ```
    * O prompt `Servidor:` aparecerá. Digite sua resposta e pressione Enter.
        ```
        Servidor: Olá cliente! Recebi sua mensagem.
        ```

3.  **No terminal do Cliente:**
    * A resposta do servidor aparecerá descriptografada:
        ```
        Servidor: Olá cliente! Recebi sua mensagem.
        ```

4.  **Para Encerrar a Conversa:**
    * Digite `sair` no prompt do cliente ou do servidor para encerrar a conexão daquele lado. O outro lado será notificado.
    * Para parar completamente o script do servidor (se ele estiver em loop para aceitar novas conexões), você pode pressionar `Ctrl+C` no terminal onde o servidor está rodando.

## ⚠️ Notas Importantes e Limitações

* **Segurança da Chave:** A chave de criptografia é derivada diretamente de uma senha fixa no código. **Este método não é seguro para aplicações reais e serve apenas para fins didáticos.** Em um cenário real, seriam necessárias técnicas mais robustas para derivação, gerenciamento e troca de chaves (ex: KDFs como PBKDF2, e protocolos como Diffie-Hellman).
* **Propósito Educacional:** Este projeto é uma demonstração simplificada para ilustrar o conceito de criptografia em comunicação. Não implementa todas as camadas de segurança (autenticação, integridade de mensagens avançada, etc.) necessárias para um mensageiro de produção.
* **Robustez:** O tratamento de erros é básico. Aplicações reais necessitam de um tratamento de exceções mais abrangente e detalhado.

---

**Desenvolvido para:** Faculdade Paraíso  
**Disciplina:** Biohacking, Criptografia e Deep Web  
**Autor:** [Marcos Victor Dantas de Souza]

# Em inglês 🇺🇸

# AES Encrypted Messenger in Python

## 📖 Overview

This project is a simple command-line interface (CLI) messenger that allows the exchange of encrypted messages between a client and a server using the AES (Advanced Encryption Standard) algorithm.

This work was developed as part of the coursework for the **Biohacking, Criptografia e Deep Web** discipline at **Faculdade Paraíso**. The main objective is to practically demonstrate the concepts of symmetric encryption in a basic communication application.

## ✨ Features

* Client-server communication using TCP/IP sockets.
* Encryption of transferred messages using AES in CBC mode.
* Use of a pre-shared secret key (derived from a password in the code) for encryption and decryption operations.
* Command-line interface for user interaction (sending and viewing messages).

## ⚙️ Prerequisites

* Python 3.6 or higher.
* `pip` (Python package manager, usually included with Python installation).

## 🚀 Setup and Installation

Follow the steps below to set up the environment and run the project:

1.  **Copy the Project Files:**
    Ensure that the `server.py`, `client.py`, and `aes_utils.py` files are in the same folder on your computer.

2.  **Navigate to the Project Folder:**
    Open your terminal or command prompt and use the `cd` command to navigate to the folder where you saved the files.
    ```bash
    cd path/to/your/project/folder
    ```

3.  **Create and Activate a Virtual Environment (Recommended):**
    A virtual environment isolates your project's dependencies, avoiding conflicts with other Python packages installed on your system.
    ```bash
    # Create the virtual environment (e.g., named 'venv')
    python3 -m venv venv

    # Activate the virtual environment
    # On Linux or macOS:
    source venv/bin/activate
    # On Windows (Command Prompt):
    # venv\Scripts\activate.bat
    # On Windows (PowerShell):
    # venv\Scripts\Activate.ps1
    ```
    You will know the environment is active because its name (e.g., `(venv)`) will appear at the beginning of your terminal prompt.

4.  **Install the `cryptography` Library:**
    With the virtual environment active, install the required library:
    ```bash
    pip install cryptography
    ```

## 🛠️ How to Use

1.  **Verify the Shared Password:**
    It is crucial that the `SENHA_COMPARTILHADA` (Shared Password) variable in both `server.py` and `client.py` files is **exactly the same**. This password is used to generate the encryption key.
    ```python
    # Example (present in server.py and client.py)
    SENHA_COMPARTILHADA = "minhasenhasupersecreta12345678" # This example means "my super secret password" in Portuguese.
    ```
    Change this password to one of your preference, but ensure it is identical in both files.

2.  **Run the Server:**
    * Open a terminal (with the virtual environment activated).
    * Navigate to the project folder.
    * Execute the server script:
        ```bash
        python server.py
        ```
    * The server will start and wait for connections. You should see a message like: `Waiting for new connection on 0.0.0.0:65432...`

3.  **Run the Client:**
    * Open **another** terminal (also with the virtual environment activated).
    * Navigate to the project folder.
    * Execute the client script:
        ```bash
        python client.py
        ```
    * The client will attempt to connect to the server. If the connection is successful, you will see: `Connected to server at 127.0.0.1:65432`.

## 💬 Basic Usage Example

Once the server is running and the client is connected:

1.  **In the Client's terminal:**
    * The `Cliente:` (Client:) prompt will appear. Type your message and press Enter.
        ```
        Cliente: Hello server, how are you? This is a test message!
        ```

2.  **In the Server's terminal:**
    * The message sent by the client will appear decrypted:
        ```
        Cliente (127.0.0.1:<client_port>): Hello server, how are you? This is a test message!
        ```
    * The `Servidor:` (Server:) prompt will appear. Type your response and press Enter.
        ```
        Servidor: Hello client! I received your message.
        ```

3.  **In the Client's terminal:**
    * The server's response will appear decrypted:
        ```
        Servidor: Hello client! I received your message.
        ```

4.  **To End the Conversation:**
    * Type `sair` (which means "exit" in Portuguese, as used in the current code) at the client or server prompt to close the connection on that side. The other side will be notified.
    * To completely stop the server script (if it is looping to accept new connections), you can press `Ctrl+C` in the terminal where the server is running.

## ⚠️ Important Notes and Limitations

* **Key Security:** The encryption key is derived directly from a hardcoded password in the code. **This method is not secure for real-world applications and serves only for didactic purposes.** In a real scenario, more robust techniques for key derivation (e.g., KDFs like PBKDF2, scrypt, Argon2) and key management/exchange (e.g., protocols like Diffie-Hellman) would be necessary.
* **Educational Purpose:** This project is a simplified demonstration to illustrate the concept of cryptography in communication. It does not implement all security layers (authentication, advanced message integrity, etc.) required for a production-ready messenger.
* **Robustness:** Error handling is basic. Real-world applications require more comprehensive and detailed exception handling.

---

**Developed for:** Faculdade Paraíso  
**Course:** Biohacking, Criptografia e Deep Web  
**Author:** [Marcos Victor Dantas de Souza]

