from flask import Flask , render_template #modules will have always lowercase
#Flask - classs
#flask - module.33


app = Flask(__name__) #app -object
#__name__ = main it will consider as main

@app.route("/") #"/" show hello vineeth / refers to route
def helloworld():
    return render_template ('home.html')

#need to give access for the app to run 
if __name__ == "__main__" :
    app.run(host='0.0.0.0' , debug=True)