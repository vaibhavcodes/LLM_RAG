1. There are 2 types of Large Language Models (LLMs):
    > 1.1. Base LLM

    > 1.2. Instruction tuned LLM

<hr>

2)  As can be seen from the image below, Base LLM has been trained on some data, due to which when asked `What is the capital of France?`, then instead of giving answer as Paris, it gave another questions as it might have been trained on the data which contains such questions.

    So, to get the result as answer to our question, this Base LLM needs to be trained such that it follows instruction, and gives us the pertinent response as can be seen under Instruction Tuned LLM in the image below.
        
    
    ![alt text](/images/TypesofLLM.png)

<hr>

3) How to get Instruction-Tuned LLM from Base LLM?

    Training the Base LLM can take months as it involves training the Base LLM on lot of data, but the process of going from Base LLM to Instruction trained LLM can be done in days.

    Now we have to further train the Base LLM to make it Instruction-tuned LLM:

    * Hire contractors to create examples where output follows an input instruction and then train our Base LLM over it.
    * Obtain human-ratings of the quality of different LLMs output, on different criterion like if it follows the context, accuracy, efficiency, executable code, other issues. This is known as `RLHF (Reinforcement Learning from Human Feedback)` and it will increase the probability of generation of highly rated outputs.


<hr>

4) How CHATGPT reads the information?

    CHATGPT model breaks the string into tokens i.e. group of characters, and these group 
    of characters which are tokens here are commonly occuring words.

    Let's understand this with the example shown in the image below: 

    ![alt text](/images/ChatgptReadingPattern.png)

    > When passed the string `Learning new things is fun!`, then model divided the strings 
    into commonly occuring words whi are highlighted in different colours in the image.

    > Similarly, when another string `Prompting is a powerful developer tool.` is given to the model,
    it divided the word `Prompting` into 3 different tokens as `Prompting` words has become commonly
    recently because of chatgpt otherwise it's not tha common. So, `Prom` , `pt` , and `ing` being 
    most commonly occuring are made as tokens. SImilarly done for other words.

    Now consider the following example: When it is asked by model to reverse the word `LOLLIPOP`,
    it couldn't do it properly because this word is divided into group of commonly occuring 
    group of characters- `LOLL` , `IPO` , `P`

    ![alt text](/images/lollipop.png)

    <b>NOTE: </b> For English language input, model considers `1 token` to be around `4 characters` or `3/4th of the word`.

    