from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
students = []


@app.route("/")
def home():
    return redirect(url_for("add_student"))


# ---------------------------------
# TODO: IMPLEMENT THIS ROUTE
# ---------------------------------
@app.route("/add", methods=["GET", "POST"])
def add_student():
    error = None

    if request.method == "POST":
        name = request.form.get("name")
        grade = request.form.get("grade")
        if not name or name == "":
            error = "A name must be entered."
        elif not grade.isdigit():
            error = "A digit grade must be entered."
        else:
            grade = int(grade)
            if grade<0 or grade>100:
                error = "Grade must be between 0 and 100."
            else:
                students.append({"name": name, "grade": grade})
                return redirect("/students")


    return render_template("add.html", error=error)


# ---------------------------------
# TODO: IMPLEMENT DISPLAY
# ---------------------------------
@app.route("/students")
def display_students():
    return render_template("students.html", students=students)


# ---------------------------------
# TODO: IMPLEMENT SUMMARY
# ---------------------------------
@app.route("/summary")
def summary():
    total_students = len(students)

    if len(students) == 0:
        return render_template(
            "summary.html",
            no_students=True,
            total_students=0,
            average=None,
            highest=None,
            lowest=None
        )
    else:
        grades = [student["grade"] for student in students]
        average = sum(grades)/ total_students
        highest = max(grades)
        lowest = min(grades)

    return render_template("summary.html",
                           total_students=total_students,
                           average=average,
                           highest=highest,
                           lowest=lowest)


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
