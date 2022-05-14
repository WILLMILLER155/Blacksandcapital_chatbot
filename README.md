# Blacksandcapital_chatbot
Chatbot project files 
Requirements outside of Python dependencies 

Need to have Docker installed and running before chat bot on port 8000. This is for Spacy and Duckling NLP extraction. 

 

Use Ngrok to connect to the open internet sometimes the port changes which is a hassle, and you must change the Api port as well to make sure things are talking. 

 

To store data in the Wix database you need my Api key. I will not provide this as this is related to my business. However, I made an account on an online database company to show how my bot stores info in the same way with a different website, so my business is not compromised.  

 

Custom actions must be in actions folder and imported with the actions.name of action for the m to run correctly 

Version and dependencies needed 

Rasa Version 3.1 

API Tests 

Ask for weather in any city (London, Sacramento, New York) 

Ask for the quote or price of a stock (MSFT, NVDA, etc) 

Database tests 

	After going through a conversation your name and email should have been saved. After you say goodbye my bot sends the name and email to an online database through a custom action. The only way to test this is to look at the code. 

 

Conversational flows suggested 

 

Greetings 

As for help with credit issues 

Go through flow 

Switch to financial education 

Go through flow 

 

 

Known Bugs 

 

Sometimes my bot does not respond, this is from all the multiple checkpoints I put in. Therefore, you must expand or say something to get it unstuck. 

 

Sometimes if you say you are an existing customer the bot just does not know what to do, just say you are a new customer, and this is usually fixed. 

 

Sometimes the bot just out of nowhere proclaims goodbye. 

 

Those are all the bugs found so far there may be more. I implemented a lot of conversational flows because I was trying to make this production ready for my own business. After working on it I see that it would take a lot more work to be production ready and better conversational management. 

 
