from pyabsa import AspectPolarityClassification as APC, available_checkpoints

# you can view all available checkpoints by calling available_checkpoints()
checkpoint_map = available_checkpoints(show_ckpts=True)

classifier = APC.SentimentClassifier('english',
                                     auto_device=False,  # False means load model on CPU
                                     cal_perplexity=True,
                                     )

def entity_sentiment(entity, text):
    text = text.replace(entity, f"[B-ASP]{entity}[E-ASP]")
    prediction = classifier.predict([text],
                       save_result=False,
                       print_result=False,  # print the result
                       ignore_error=True,  # ignore the error when the model cannot predict the input
                                    )
    if prediction[0]["sentiment"][0] == "Negative":
        elo_weight = -round(prediction[0]["confidence"][0]*10, 2)
    elif prediction[0]["sentiment"][0] == "Neutral":
        elo_weight = 1
        if prediction[0]["probs"][0][0] > .22:
            elo_weight = -1
    else:
        elo_weight = round(prediction[0]["confidence"][0]*10, 2)
    
    return elo_weight

