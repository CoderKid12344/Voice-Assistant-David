import os
import random
import json
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
from Listen import Listen
import sys
from Speak import Say
from Task import NonInputExecution, InputExecution

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json", "r") as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

Name = "David"
def Main():
    sentence = Listen()
    result = str(sentence)

    if "stop" in sentence:
        Say('Ok sir! Bye!')

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])
                if "time" in reply:
                    NonInputExecution(reply)
                elif "date" in reply:
                    NonInputExecution(reply)
                elif "wikipedia" in reply:
                    InputExecution(tag, result)
                elif "google" in reply:
                    InputExecution(tag, result)
                elif "youtube" in reply:
                    InputExecution(tag, result)
                elif "apps" in reply:
                    InputExecution(tag, result)
                elif "temperature" in reply:
                    NonInputExecution(reply)
                elif "ip" in reply:
                    NonInputExecution(reply)
                elif "how to" in reply:
                    InputExecution(tag, result)
                elif "corona" in reply:
                    InputExecution(tag, result)
                elif "trans" in reply:
                    InputExecution(tag, result)
                elif "location" in reply:
                    InputExecution(tag, result)
                elif "whatsapp" in reply:
                    NonInputExecution(reply)
                elif "news" in reply:
                    NonInputExecution(reply)
                elif "joke" in reply:
                    NonInputExecution(reply)
                elif "pause" in reply:
                    NonInputExecution(reply)
                elif "resume" in reply:
                    NonInputExecution(reply)
                elif "online" in reply:
                    NonInputExecution(reply)
                elif "where is" in reply:
                    InputExecution(tag, result)
                elif "battery" in reply:
                    NonInputExecution(reply)
                elif "calculate" in reply:
                    NonInputExecution(reply)
                elif "sleep" in reply:
                    NonInputExecution(reply)
                elif "shut down" in reply:
                    NonInputExecution(reply)
                elif "restart" in reply:
                    NonInputExecution(reply)
                elif "close" in reply:
                    InputExecution(tag, result)
                elif "call" in reply:
                    InputExecution(tag, result)
                else:
                    Say(reply)

while True:
    Main()
