"""
This file contains the template for the prompt to be used for injecting the context into the model.

With this technique we can use different plugin for different type of question and answer.
Like :
- Internet
- Data
- Code
- PDF
- Audio
- Video

"""

from datetime import datetime
now = datetime.now()

def prompt4conversation(prompt,context):
    final_prompt = f""" GENERAL INFORMATION : ( today is {now.strftime("%d/%m/%Y %H:%M:%S")} , You is built by Bhashyam Sravan Kumar, YOU ARE A TEXT SUMMARIZER TOOL THAT GENERATES CONCISE SUMMARIES OF TEXT INPUTS.
                        ISTRUCTION : IN YOUR ANSWER, PROVIDE A BRIEF AND ACCURATE SUMMARY WITHOUT INCLUDING THE USER'S QUESTION OR MESSAGE.
                        PREVIUS MESSAGE : ({context})
                        NOW THE USER ASK : {prompt} . 
                        WRITE THE ANSWER :"""
    return final_prompt

def prompt4conversationInternet(prompt,context, internet, resume):
    final_prompt = f""" GENERAL INFORMATION : ( today is {now.strftime("%d/%m/%Y %H:%M:%S")} , YOU ARE A TEXT SUMMARIZER TOOL THAT GENERATES CONCISE SUMMARIES OF TEXT INPUTS.
                        ISTRUCTION : IN YOUR ANSWER, PROVIDE A BRIEF AND ACCURATE SUMMARY WITHOUT INCLUDING THE USER'S QUESTION OR MESSAGE.
                        PREVIUS MESSAGE : ({context})
                        NOW THE USER ASK : {prompt}.
                        INTERNET RESULT TO USE TO ANSWER : ({internet})
                        INTERNET RESUME : ({resume})
                        NOW THE USER ASK : {prompt}.
                        WRITE THE ANSWER BASED ON INTERNET INFORMATION :"""
    return final_prompt