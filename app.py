from flask import Flask, render_template, request
import pickle
app = Flask(__name__) # create instance of flask class. name refers to current file/module
#create a route
tokenizer = pickle.load(open("models/cv.pkl", "rb"))
classifier = pickle.load(open("models/clf.pkl", "rb"))
@app.route("/", methods=["GET", "POST"]) 
#Mention that GET and POST methods are accepted by home route
#Register a route(URL pattern) of home page using decorator
def home(): #define what flask application should return when a specific URL is requested 
    return render_template("home_page.html")
@app.route("/predict", methods=["POST"])
def predict():
    email_text = ""
    result = ""
    result_d = {1:"Spam", 0:"Not Spam"}
    if request.method == "POST":
        email_text = request.form.get('email-content')
    tokens = tokenizer.transform([email_text])
    prediction = classifier.predict(tokens)
    return render_template("home_page.html", result=prediction)


if(__name__) == "__main__": #ensures server only runs if script executed directly, 
    #not imported as a module 
    app.run(debug=True) 
    #MAke sure to set debug=True, 
    #so any update to home function can be reflected on flask server without stopping it.