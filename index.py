from flask import Flask, render_template, url_for, request
from math import sin, cos, tan, sqrt, exp, log, acosh, asinh, atanh, asin,acos

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html", home=True)

@app.route("/simple")
def simple():
    return render_template("simple.html")

@app.route("/advanced")
def advanced():
    return render_template("advanced.html")



@app.route("/calculate", methods = ["post"])
def calculate():
    first_number =  int(request.form["firstnumber" ])
    operation = request.form["operation"]
    last_number =  int(request.form["lastnumber" ])
    note = ""
    color = "alert-success"
    if operation == "plus":
        result = first_number + last_number
        note = "Addition was performed sucessfully"  
    elif operation == "minus":
        result = first_number - last_number
        note = "Subtraction was performed sucessfully"        
    elif operation == "multiply":
        result = first_number * last_number
        note = "Multiplication was performed sucessfully"        
    elif operation == "divide":
        result = first_number / last_number
        note = "Division was performed sucessfully"        
    else:
        note = "There is an Error .Plz Try again."
        color = "alert-danger"
        return  render_template("simple.html", note=note)    
    return render_template("simple.html", result=result, note=note, color=color, operation=operation)


@app.route("/calculate_advanced", methods=["post"])
def calculate_advanced():           
    first_number =  int(request.form["firstnumber" ])
    operation = request.form["operation"]  
    color ="alert-warning"
    note =""
    try:
        if operation == "sin":
            result = sin(first_number) 
            note ="sin has been calculated" 
        elif operation == "cos":
            result = cos(first_number) 
            note ="cos has been calculated"
        elif operation == "tan":
            result = tan(first_number) 
            note ="tan has been calculated"
        elif operation == "squr":
            result = sqrt(first_number)  
            note ="Square root has been calculated"  
        elif operation == "log":
            result = log(first_number)  
            note ="Log has been calculated" 
        elif operation == "exp":
            result = exp(first_number)  
            note ="exp has been calculated" 
        elif operation == "acosh":
            result = acosh(first_number)  
            note ="acosh has been calculated" 
        elif operation == "asinh":
            result = asinh(first_number)  
            note ="asinh has been calculated" 
        elif operation == "atanh":
            result = atanh(first_number)  
            note ="atanh has been calculated" 
        elif operation == "asin":
             result = asin(first_number)  
             note ="asin has been calculated" 
        elif operation == "acos":
            result = acos(first_number)  
            note ="acos has been calculated"                                                         
        else:
            note = "no function has been selected"
            color = "alert-danger"
            return render_template("advanced.html", note=note) 
            
    except ValueError:    
          return render_template("advanced.html", result=0, note="Math Error!", color="alert-danger")
    
            
    return render_template("advanced.html", result=result, note=note, color=color, operation=operation)


if __name__ == "__main__":
    app.run(debug=True)