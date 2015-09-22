# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask(name)

#The first line uses a special decorator (signified by the ’@’ sign) to establish
#a route for incoming messages to reach the server. The function you declare right 
#after this decorator will execute every time a request is sent to this route, and 
#whatever is returned from the function will be sent back to the user making the request. 
#In this case we will make a simple function that just returns a basic webpage. T
#o do this you just return the render_template() function, with the name of the webpage 
#(which should be in your templates folder) as the single argument.

@app.route("/")
def index():
    return render_template("index.html")

#The conditional on the first line checks to make sure that the script is running
#on the main thread (as opposed to being imported by another process). Although 
#this will not be an issue in our particular case, this check is a best practice 
#that will prevent the server from being unintentionally launched in case someone 
#references our code from within another process. Within this conditional is the 
#code to launch the server. We use the app.run() function, and into it pass 
#parameters to specify the address we want the server to run on, the port it should
#use, and some optional parameters about debugging and threading.

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True,threaded=True)