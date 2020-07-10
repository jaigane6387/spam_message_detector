from flask import Flask,render_template,url_for,request
import pickle
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)
model = pickle.load(open('spam_classifier.pkl', 'rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = cv.transform(data).toarray()
		prediction = model.predict(vect)
	return render_template('result.html',prediction = prediction)


if __name__ == "__main__":
    app.run(debug=True)
