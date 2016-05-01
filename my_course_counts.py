from os import chdir
from os.path import dirname, realpath

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# helper function; returns True if needle (a string) is in haystack (a string)
# from Library quiz
def str_contains(haystack, needle):
    return (needle.lower() in haystack.lower())

class Course:
    def __init__(self, year, semester, department, course_number, section, class_title, unit, instructor, time, core,
                 seats, enrolled, reserved, reserved_open, waitlisted):
        self.year = year
        self.semester = semester
        self.department = department
        self.course_number = course_number
        self.section = section
        self.class_title = class_title
        self.unit = unit
        self.instructor = instructor
        self.time = time
        self.core = core
        self.seats = seats
        self.enrolled = enrolled
        self.reserved = reserved
        self.reserved_open = reserved_open
        self.waitlisted = waitlisted

def get_data():
    course_data = []
    with open('counts.tsv') as fd:
        for line in fd.read().splitlines():
            year, semester, department, course_number, section, class_title, unit, instructor, time, core, seats, enrolled,reserved, reserved_open, waitlisted = line.split('\t')
            course_data.append(Course(year, semester, department, course_number, section, class_title, unit, instructor, time, core, seats, enrolled, reserved, reserved_open, waitlisted))
    return course_data

@app.route('/')
def view_homepage():
    return render_template('base.html')


@app.route('/department/<department>/')
def department_select(department):
    results = []
    for course in get_data():
        if course.department == department:
            results.append(course)
    return render_template('department.html', results = results)


@app.route('/department/<department>/core/<core>/')
def department_core_select(department, core):
    results = []
    for course in get_data():
        if course.department == department:
            match = False
            if str_contains(course.core, core):
                match = True
            if match:
                results.append(course)
    return render_template('department_core.html', results = results)

@app.route('/core/<core>/')
def core_select(core):
    results = []
    for course in get_data():
        match = False
        if str_contains(course.core, core):
            match = True
        if match:
            results.append(course)
    return render_template('core.html', results = results)

@app.route('/core/<core>/department/<department>/')
def core_dept_select(core, department):
    results = []
    for course in get_data():
        if course.department == department:
            match = False
            if str_contains(course.core, core):
                match = True
            if match:
                results.append(course)
    return render_template('core_department.html', results = results)


@app.route('/<year>/<semester>/')
def year_semester_select(year, semester):
    results = []
    for course in get_data():
        if course.year == year and course.semester == semester:
            results.append(course)
    return render_template('year_semester.html', results=results)


@app.route('/<year>/<semester>/department/<department>/')
def year_semester_department_select(year, semester, department):
    results = []
    for course in get_data():
        if ((course.year == year and course.semester == semester) and course.department == department):
            results.append(course)
    return render_template('year_semester_department.html', results=results)


@app.route('/<year>/<semester>/core/<core>/')
def year_semester_core_select(year, semester, core):
    results = []
    for course in get_data():
        if course.year == year and course.semester == semester:
            match = False
            if str_contains(course.core, core):
                match = True
            if match:
                results.append(course)
    return render_template('year_semester_core.html', results=results)

@app.route('/<year>/<semester>/department/<department>/core/<core>/')
def year_semester_department_core_select(year, semester, department, core):
    results = []
    for course in get_data():
        if (course.year == year and course.semester == semester) and course.department == department:
            match = False
            if str_contains(course.core, core):
                match = True
            if match:
                results.append(course)
    return render_template('year_semester_department_core.html', results=results)

@app.route('/<year>/<semester>/core/<core>/department/<department>/')
def year_semester_core_department_select(year, semester, department, core):
    results = []
    for course in get_data():
        if (course.year == year and course.semester == semester) and course.department == department:
            match = False
            if str_contains(course.core, core):
                match = True
            if match:
                results.append(course)
    return render_template('year_semester_core_department.html', results=results)


# The functions below lets you access files in the css, js, and images folders.
# You should not change them unless you know what you are doing.

@app.route('/images/<file>')
def get_image(file):
    return send_from_directory('images', file)

@app.route('/css/<file>')
def get_css(file):
    return send_from_directory('css', file)

@app.route('/js/<file>')
def get_js(file):
    return send_from_directory('js', file)

if __name__ == '__main__':
    chdir(dirname(realpath(__file__)))
    app.run(debug=True)
