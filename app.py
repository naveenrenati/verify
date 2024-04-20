from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample data
students_data = [
    {
        "Title": "DATA ENGINEERING USING PYTHON PROGRAMMING INTERNSHIP WITH CERTIFICATION",
        "Student User ID": "STU6452571cef7351683117852",
        "Student ID": "20121A0534",
        "Student Institute Name": "SREE VIDYANIKETHAN ENGINEERING COLLEGE",
        "Verification": "verified",
        "Duration": "JAN - MAR"
    },
    {
        "Title": "DATA ENGINEERING USING PYTHON PROGRAMMING INTERNSHIP WITH CERTIFICATION",
        "Student User ID": "STU660cc7dc72f121712113628",
        "Student ID": "Y23CA054",
        "Student Institute Name": "R.V.R.& J.C.COLLEGE OF ENGINEERING",
        "Verification": "verified",
        "Duration": "JAN - MAR"
    },
    {
        "Title": "DATA ENGINEERING USING PYTHON PROGRAMMING INTERNSHIP WITH CERTIFICATION",
        "Student User ID": "STU661d3b119a79f1713191697",
        "Student ID": "22551A4205",
        "Student Institute Name": "GODAVARI INSTITUTE OF ENGINEERING & TECHNOLOG",
        "Verification": "verified",
        "Duration": "JAN - MAR"
    },
    {
        "Title": "DATA ENGINEERING USING PYTHON PROGRAMMING INTERNSHIP WITH CERTIFICATION",
        "Student User ID": "STU61cc4b3d5f9931640778557",
        "Student ID": "20121A0550",
        "Student Institute Name": "SREE VIDYANIKETHAN ENGINEERING COLLEGE",
        "Verification": "verified",
        "Duration": "JAN - MAR"
    },
    {
        "Title": "DATA ENGINEERING USING PYTHON PROGRAMMING INTERNSHIP WITH CERTIFICATION",
        "Student User ID": "STU61bddfd240c9c1639833554",
        "Student ID": "20121A1570",
        "Student Institute Name": "SREE VIDYANIKETHAN ENGINEERING COLLEGE",
        "Verification": "verified",
        "Duration": "JAN - MAR"
    },
    {
        "Title": "DATA ENGINEERING USING PYTHON PROGRAMMING INTERNSHIP WITH CERTIFICATION",
        "Student User ID": "STU64de4346e510b1692287814",
        "Student ID": "20121A0592",
        "Student Institute Name": "SREE VIDYANIKETHAN ENGINEERING COLLEGE",
        "Verification": "verified",
        "Duration": "JAN - MAR"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_student_info', methods=['GET'])
def get_student_info():
    student_user_id = request.args.get('student_user_id')
    student_info = next((student for student in students_data if student["Student User ID"] == student_user_id), None)
    if student_info:
        return jsonify({
            "Student ID": student_info["Student ID"],
            "Title": student_info["Title"],
            "Student Institute Name": student_info["Student Institute Name"],
            "Verification": student_info["Verification"],
            "Duration": student_info["Duration"]
        })
    else:
        return jsonify({"message": "Student not found!"}), 404

if __name__ == '__main__':
    app.run(debug=True)
