from flask import Flask,render_template,request
from scripts.validate.validate import validationDictionary

app=Flask(__name__)

app.config['DEBUG']=True


    
def validation(parameters):
    error={}
    for index, field in enumerate(parameters.form):
        
        if field in validationDictionary():
            if (validationDictionary()[field](field,parameters.form))==False:
                error[field]= False
        
       
    if len(error)>0:
        return error
    
    return True

def main():
    app.run()

@app.route('/',methods=['GET','POST'])
def index():
    
    
    if (request.method =='GET'):
         return render_template('sections/index.html',validate=[])
    if (request.method)=='POST':
        if validation(request)==True:
            return render_template('sections/protected/home.html',username=request.form['username'])
        else:
            return render_template('sections/index.html',validate=validation(request),username=request.form['username'],email=request.form['email'])
        


if __name__=="__main__":
    main()
    