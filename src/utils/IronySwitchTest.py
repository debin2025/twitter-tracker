import tweetnlp

model = tweetnlp.load_model('irony')
def irony_switch(text):
    result = model.irony(text, return_probability=True)
    if result['label'] == "irony" and result['probability']['irony'] > 0.55:
        return -0.5
    else:
        return 1
