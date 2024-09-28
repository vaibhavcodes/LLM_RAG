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

3)  <b style="color:red; font-size:2.0em"> PRINCIPLE-2:</b> <b style="color:green; font-size:2.0em">Give the model time to “think”:</b> <br>
    3.1. <b style="color:orange; font-size:1.2em">Specify the steps required to complete a task: </b> These delimiters will separate the text to be modified from rest of the prompt.
        
    ![alt text](/images/delimiterType.png)

       <b style="color:pink; font-size:1em"> EXAMPLE: </b>

    ![alt text](/images/delimiterTypeExample.png)

    <br><p><center><b> ========================================== </b></center></p><br>

    3.2. <b style="color:orange; font-size:1.2em">Instruct the model to work out its own solution before rushing to a conclusion: </b> Like HTML, JSON

       <b style="color:pink; font-size:1em"> EXAMPLE: </b>

    ![alt text](/images/structuredOutput.png)
 
 <HR>