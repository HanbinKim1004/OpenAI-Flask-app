import os
import openai
from flask import Flask, render_template, request

app = Flask(__name__)
port__ = 5000

@app.route('/')
def home():
    return render_template('index.html', data = port__)

@app.route('/QuestionLog', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      val = request.form #index.html에서 name을 통해 submit한 값들을 val 객체로 전달
      return render_template("QuestionLog.html", result = val) #name은 key, name에 저장된 값은 value
 
@app.route('/ChatGPT',methods = ['POST', 'GET'])
def ChatGPT():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    query = list(request.form.values())[0]

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt = query,
    temperature=1, # 무작위성 제어
    max_tokens=4000, #최대 토큰이 4000
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    answer__ = response["choices"][0]["text"].strip()

    return render_template("ChatGPT.html", answer = answer__)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = port__ , debug = True)
