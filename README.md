# LLM_RAG

1. We need an OpenAi key so got to [platform.openai.com](https://platform.openai.com) and register there. Then go to [Dashboard](https://platform.openai.com/assistants) and click on API Keys option.
<br>
<br>
2. Also, store your key as an environment variable for easy and secure access: 
    ```bash
    export RAG_OPENAI_KEY="Paste the key you have copied from the Openai dashboard"
    ```
<br>

3. There are 2 ways to work on this:<br>
3.1. Open codespaces from github, and then select "VS Code Desktop" from the bottom, and install all the libraries mentioned in requirements.txt  


    3.2. Using miniconda:
    => Open VS code and then open Terminal and run the following command:

        => Download miniconda from [here](https://repo.anaconda.com/miniconda/Miniconda3-py310_24.7.1-0-Linux-x86_64.sh)  
    
         => Install it outside your current workspace using the following command:
            > bash Miniconda3-py310_24.7.1-0-Linux-x86_64.sh

        => Install all the libraries mentioned in the requirements.txt


