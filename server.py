from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")

@app.route('/about')    
def about():
  return render_template("about.html")

#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "OK"

@app.route('/test',methods = ['POST', 'GET'])
def tests():
    parametri = ["IQ","Augums","Kājas izmērs"]
    images = ["https://pixabay.com/photos/newborn-baby-baby-feet-infant-2579144/","https://pixabay.com/photos/bird-saffron-finch-ornithology-7071662/","https://pixabay.com/photos/elephant-baby-elephant-animals-7036431/"]
    return render_template("test.html", parametri=parametri)
 

if __name__ == '__main__':
  app.run(debug="true")
