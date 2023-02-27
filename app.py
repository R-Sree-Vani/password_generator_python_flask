from flask import Flask,render_template,request,redirect
import secrets
import string


app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/generate",methods=['GET','POST'])
def password():
    if request.method=='POST':
        l=string.ascii_letters
        d=string.digits
        s=string.punctuation
        al=l+d+s
        pwd_length=12
        pwd=""
        for i in range(pwd_length):
            pwd+=''.join(secrets.choice(al))
    return render_template("home.html",pwd=pwd)

@app.route("/clear",methods=['GET','POST'])
def clear():
    if request.method=='POST':
        value=request.form.get("prespass")
        value=""
        return redirect("/")
    return render_template("home.html")



if __name__ == '__main__':
    app.run(debug=True)