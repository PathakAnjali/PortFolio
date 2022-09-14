import csv
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route("/")
def myhome():
    return render_template("index.html")


# @app.route("/about.html")
# def about():
#     return render_template("about.html")


# @app.route("/components.html")
# def components():
#     return render_template("components.html")


# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")


# @app.route("/works.html")
# def works():
#     return render_template("works.html")


# @app.route("/work.html")
# def work():
#     return render_template("work.html")


# ADDING HTML FILES DYNAMICALLY , NO NEED TO CRAETE MULTIPLE FUNCTIONS FOR EVERY HTML FILES,
# USING VARIABLE RULE : STRING


@app.route('/<string:Page_Name>')
def html_Pages(Page_Name):
    return render_template(Page_Name)


# 1. Function for contact.html ,send button action to respond , changes: added in contat file in tab action with method: post

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     return "Form is submitted!"


# 4  create a database of text type  to receive or store the information or data that server receives from the users.

def StoreData_ToFile(data):
    with open('DataBase_PortFolio.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

#    from function: submit_form >     data = request.form.to_dict()

        file = database.write(f"\n {email},{subject},{message}")


#  create a database of csv type  to receive or store the data that server receives from the users.

def StoreData_ToCSV(data):
    with open('DataPortFolio.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        # method to write in csv file

        csv_file = csv.writer(database2, delimiter=",",
                              quotechar="|", quoting=csv.QUOTE_MINIMAL)

        # writerow is a method
        csv_file.writerow([email, subject, message])

# if need to add newline in text or csv then:
# >> with open('database.csv', newline='', mode='a') as database2:


# 2. to read the data (from message section): add attribute 'name' to all the input in contact.html


# 3. Accessing data(email,subject and text from contact file) using 'request.form' method


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # request.form.to_dict() : a method to grab data in the  form of dictionary
        data = request.form.to_dict()

        # calling function StoreData_ToFile
        # StoreData_ToFile(data)
        StoreData_ToCSV(data)

        # redirect : redirects to another page
        return redirect('/ThankYou.html')
    else:
        return "Something went wrong"
