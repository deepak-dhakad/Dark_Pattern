from flask import Flask, jsonify, request
from flask_cors import CORS
from joblib import load
from transformers import BertTokenizer, BertForSequenceClassification
import torch



category_classifier = load('C:/dark-patterns-recognition-master/api/category_classifier.joblib')
category_vect = load('C:/dark-patterns-recognition-master/api/category_vectorizer.joblib')
bert_model = BertForSequenceClassification.from_pretrained('C:/dark-patterns-recognition-master/api/bert_fine_tuned_model')

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        output = []
        data = request.get_json().get('tokens')

        for token in data:
          
            tokenized_input = tokenizer(token, return_tensors='pt',  truncation=True, padding=True)
            tokenized_input = {key: value.to(bert_model.device) for key, value in tokenized_input.items()}
      
            
            with torch.no_grad():
                logits = bert_model(**tokenized_input).logits
            result = torch.argmax(logits, dim=1).item()
            
            
            if result == 0:
                 result = 'Not Dark'
            else:
                 result = 'Dark'
           

            if result == 'Dark':
                cat = category_classifier.predict(category_vect.transform([token]))
                output.append(cat[0])
            else:
                output.append(result)

        dark = [data[i] for i in range(len(output)) if output[i] == 'Dark']
        for d in dark:
            print(d)
        print()
        print(len(dark))

        message = '{ \'result\': ' + str(output) + ' }'
        print(message)

        json = jsonify(message)

        return json

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
