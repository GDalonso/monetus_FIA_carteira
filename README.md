# Rentabilidade diaria
Calcula rentabilidade diaria de alguns fundos

deploying with cloud functions

    With your terminal with gcloud sdk setup used
    gcloud functions deploy get_stat --trigger-http --runtime python38    
    
    where
        - functions = google cloud functions
        - hello_get = name of the function in the main.py file i want to deploy
        - trigger-http = trigers the function when get a request
        -- runtime = python version

Running it locally and debugging
    ![alt text](https://hackultura.s3.amazonaws.com/Public/debug_cloud_functions.png "how to use it in pycharm")

    