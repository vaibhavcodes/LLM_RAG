1. There are 3 main principles of prompting:
    > 1.1. Write clear and specific Instructions.

    > 1.2. Give model time to think

<hr>

2)  <b style="color:red; font-size:2.0em"> PRINCIPLE-1:</b> <b style="color:green; font-size:2.0em">Write clear and specific Instructions</b> <br>
        2.1. <b style="color:orange; font-size:1.2em">Use delimiters to clearly indicate distinct parts of the input: </b> These delimiters will separate the text to be modified from rest of the prompt.
        
    ![alt text](/images/delimiterType.png)

       <b style="color:pink; font-size:1em"> EXAMPLE: </b>

    ![alt text](/images/delimiterTypeExample.png)

    <br><p><center><b> ========================================== </b></center></p><br>

    2.2. <b style="color:orange; font-size:1.2em">Ask for a structured output: </b> Like HTML, JSON

       <b style="color:pink; font-size:1em"> EXAMPLE: </b>

    ![alt text](/images/structuredOutput.png)

    <br><p><center><b> ========================================== </b></center></p><br>

    2.3. <b style="color:orange; font-size:1.2em">Ask the model to check whether conditions are satisfied: </b> This will help in checking endcases as well.

       <b style="color:pink; font-size:1em"> EXAMPLE: </b>

    ![alt text](/images/conditionalPrompt.png)

    <br><p><center><b> ========================================== </b></center></p><br>

    2.4. <b style="color:orange; font-size:1.2em">"Few-shot" prompting: </b> Give `some examples of context with the required output`, then ask the model to perform the task.

       <b style="color:pink; font-size:1em"> EXAMPLE: </b>

    ![alt text](/images/FewShot.png)
<br>
<HR>

3)  <b style="color:red; font-size:2.0em"> PRINCIPLE-2:</b> <b style="color:green; font-size:2.0em">Give the model time to “think”:</b> <br> When a model is given some complex task but user asked the input in a short amount of words, then model is very likely to make an assumption to that answer which will be likely to be wrong or to keep asking question to the model untill it give you the required answer.

    3.1. <b style="color:orange; font-size:1.2em">Specify the steps required to complete a task: </b>

       <b style="color:pink; font-size:1em"> EXAMPLE: </b>

    ![alt text](/images/modelThink.png)

    <br><p><center><b> ========================================== </b></center></p><br>

    3.2. <b style="color:orange; font-size:1.2em">Instruct the model to work out its own solution before rushing to a conclusion: </b> Like HTML, JSON

       <b style="color:pink; font-size:1em"> EXAMPLE: </b>
       As you can see in the image below, that solution is wrong but model gave us that it's correct because model only looked at the final line where calculation is done but not the `Maintenance cost` line where instead of 100x, 10x should come. 

    ![alt text](/images/Wrongsoln.png)

    So, to deal with this we need to instruct the model more now as scan be seen from the following:

    ![alt text](/images/correctPrompt.png)
 
 <HR>

4)  <b style="color:red; font-size:2.0em"> Lifecycle of Prompt Development</b>


      Prompt development is an `iterative` process where you:
    * Need to try something in the prompt
    * Analyse where the results doesn't satisfy your requirements or hallucinate
    * Clarify instructions in the prompt that would give more time to the model to think.
    * Try refining the prompts by providing few examples.

      ![alt text](/images/PromptLifecycle.png)

 <HR>

5)  <b style="color:red; font-size:2.0em"> Different `role` provided in the prompt</b>

      `system` role sets the behaviour or persona of the assistant, `user` is the role of ours who provides input to the LLM model, and `assistant` is the model who gives answer to our question, but it can be considered that system whispers the answer into the assistant ears without user getting know about it.

      ![alt text](/images/roles.png)


      ```python
      messages =  [  
               {'role':'system', 
               'content':'You are an assistant that speaks like Shakespeare.'},  

               {'role':'user', 
               'content':'tell me a joke'},   

               {'role':'assistant', 
               'content':'Why did the chicken cross the road'},   

               {'role':'user', 
               'content':'I don\'t know'}  
               ]
               

<HR>

6) <b style="color:red; font-size:2.0em"> Creation of chatbot</b>


      Normally, for every prompt going into the message we are getting only one response. But for the chatbot, we need to make it recursive so that multiple roles can be passed recursively as can be seen from the following image where we need to pass multiple messages recursively.

      ![alt text](/images/continuousMessageForChatbot.png)