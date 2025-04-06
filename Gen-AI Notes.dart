- Gen-AI
    - Create new content by learning thru old data. 

    - Dataset uses:
        - Text, Images, Videos
    
    - Examples:
        - Code, Image, video and content generation.

    - Gen-AI is finding the next word based on given context.
    Identify the next word on probability with the highest rank word and other parameters.

    - This uses self supervised learning algorithm, learns from its data itself.

    - Process:
        - Predict the word
        - Compare the word with the actual word
        - Learn and Correct the model

    Tokens:
        - Gen-AI uses tokens instead of words.
        - Tokens are more efficient to process and provide full context, but in the case of word, meaning of word differ.
        - Tokens are not just words, rather they can be number, punctuation or text.

        Example Tokens:
            - bank_river, bank_rbi


- Diff b/w ML and Gen-AI
    - Make a good prediction        Generate new content
    - Input is features             Input is thru prompt
    - Ouput is Label                Ouput is new content



- LLM 
    - These models focus only on text or chat. 
    - Foundation Models of google cloud built on LLM.



- Google-Cloud AI Services
    - Vertex-AI(Tool)
        - Model Garden - There are set of pre-defined models for Language, Speech, Tabular
            
            - Foundation Models

                - Text Models
                    - text-bison: Natural language processing model, helps to classification, extraction, ideation and summarize the text. 
                    - chat-bison:  Conversational chat model
                        
                    - text embeding-gecko

                - Code Models
                    - code-bison: Generate code
                    - code-chat bison: Code assist to QA
                    - code-gecko: Provides code auto completion.

                - Image Models
                    - image generator: Thru prompt text, generate images
                    - image text: Describe the image into text.

                - Open Source Models
                    - openLLaMA: LLM from Meta, used to generate the text, images and code.

        - Generative AI Studio 
        - In dataset, we can keep the data which we want to train, validate and test models. and then we start the training the model using dataset. once model is ready, we can test thru API.



- Text Model based Features:
    - Classification: classify the content into a category. the customer feedback into categories. e.g, Positive, Negative, Neutral.  other examples are news, movie and product categories.
    - Summarize: Summarize the blob/post, pdf document data and able to provide the title.
    - Extraction: Extract the tech specification text to json data and also used for question, answer on given context or provides documents.
    - Writing: Helps to write the Email/Job/Product announcements, ad copy on different categories.
    - Ideation: Get ideas. E.g generate ideas, get advice, generate interview question and generate creative naming.


- Prompt
    - Initial instructions supplied to model
    - Frameworks: CTF, RTF, RASCEF 

    - Why prompt design?
        - Optimize the model performance.
        - To get the accurate and reliable responses.

    - Prompt design best practices :
        - Clear instructions
        - Provide examples - zero shot (no example), one shot (1 example) and few shot(>1 examples)
        - Experiment with multiple texts or different parameters.
        - Use framework for better responses

    - Frameworks:
        - RTF - Role, Task, Format - Provide all these detals in prompt
        - CTF - Context, Task, Format - Provide all these detals in prompt
        - RASCEF - Role, Action, Steps, Context, Examples, Format - Provide all these detals in prompt
    
    - Experiment with parameters:
        - Token limit: Expecting number of words from output prompt
            - 1 token = 4 chars 
         - below parameters helps to determine the next token to choose.
            - Top-K: choose next top K tokens.
            - Top-P: Sum of probabilitys for cut off to choose the tokens. 
            - Temparature: Randomness
                - 0 - Low
                - 1 - High



- Google Vertex AI Studio
    - Text generation model

    - Code models
        - code-bison: Generate code
        - code-chat bison: Code assist to QA
        - code-gecko: Provides code auto completion.

    - Chat model
        - chat-bison

    - Image models
        - Imagen - text to image
        - Imagen Captioning - generate description for image
        - Imagen Visual QA - Answer to questions on given image

    - Speech model
        - Speech to Text
        - Text to Speech
    
    - Tuning Language Models
        - If text/any model does not work as expected, we can tune/train the model and predict it.

- Embeddings
    - Multi dimensional representation of a word in each context, represented in uniform distribution ( 0 to 1).
    
    - Ex:
        - Speed of animals - Elephent (0.1), Rabbit (0.4), Cheetah(0.7)
        - Water usage of animals - Cheetah (0.2), Rabbit (0.2), Monkey(0.5), Elephent(0.9) 
        
    - Widely in NLP.
        - Finding similar sentences.
        - Recommendation system
        - Grouping similar words
        - Outing different word from group

- LangChain
    - Easily switch the models (from openAI to openLLaMA). 
    - Helps to execute the sequence of chains.
    - Provides abstractions for
        - text, chat and embedding models.
    - Also provides promptTemplate
    - Also used to long article Q & A
        - Splitting file into chuncks
        - Each chunk to embedding chunk for finding similar chunk for given question
        - searching in those similar chunks
    - Also summarazing the multiple docs thru Map-Reduce


- Building Gen-AI App in Google
    - Gen App builder
        - Search 
        - Chat
        - Recommendation
    - makersuite.google.com - play with it
    - colab

- API communication
    - init project
    - set parameters
    - create model
    - predict thru model




















