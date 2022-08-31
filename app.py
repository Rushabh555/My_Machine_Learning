from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/student', methods = ['POST'])
def get_data():

    student_data = request.form
    print(student_data)
    print(type(student_data))

    student_name = request.form['student_name']
    print(f"{student_name=}")
    student_dict = {"name":student_name}

    return render_template('result.html',result=student_dict)


if __name__ == '__main__':
    app.run(debug=True)