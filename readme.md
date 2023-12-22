==> If you want to download a model from hugging face to run, follow the following steps:
    1) Open the jupyter notebook named download_model.ipynb
    2) Set the MODEL_NAME variable to the model you want to download.
    3) Set the save_dir variable to the location where you want to store the weights of the downloaded model.


==> If you want to upload your own model, make a new directory in ./models directory and save the model weights and your tokenzier in there.

==> Steps to run the webserver for text generation:
    1) Open the model.py file and change the location of the directory to the directory of your choice in the load_model() and load_tokenizer() functions.
    2) Now, run the command - python app.py
    3) You can use curl to give the input as a python dictionary.
        For example: if I want to give the sentence "Hi, my name is" as a prompt to be completed, the input would be {"text" : "Hi, my name is"}
