from os import chdir
from os.path import dirname, realpath

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# helper function; returns True if needle (a string) is in haystack (a string)
# from Library quiz
def str_contains(haystack, needle):
    return (needle.lower() in haystack.lower())


class Course:
    def __init__(self, year, season, dept, dept_num, section, title, units,
                 time, total_seats, enrolled, reserved, reserved_open, waitlisted):
        self.semester = str(season) + ' ' + str(year)
        self.dept = dept
        self.dept_num = dept_num
        self.section = section
        self.title = title
        self.units = units
        self.instructors = []
        self.time = time
        self.core = []
        self.total_seats = total_seats
        self.enrolled = enrolled
        self.reserved = reserved
        self.reserved_open = reserved_open
        self.waitlisted = waitlisted
    def get_semester(self):
        return self.semester
    def get_dept(self):
        return self.dept
    def get_dept_num(self):
        return self.dept_num
    def get_section(self):
        return self.section
    def get_title(self):
        return self.title
    def get_units(self):
        return self.units
    def get_instructors(self):
        return self.instructors
    def get_time(self):
        return self.time
    def get_core(self):
        return self.core
    def get_total_seats(self):
        return self.total_seats
    def get_enrolled(self):
        return self.enrolled
    def get_reserved(self):
        return self.reserved
    def get_reserved_open(self):
        return self.reserved_open
    def get_waitlisted(self):
        return self.waitlisted

class Catalogue:
    def __init__(self):
        self.courses = []

    def search_by_semester(self,string):
        results = []
        for course in self.courses:
            match = False
            for semester in course.semester:
                if str_contains(semester, string):
                    match = True
                    break
            if match:
                results.append(course)

    def search_by_dept(self, string):
        results = []
        for course in self.courses:
            match = False
            for dept in course.dept:
                if str_contains(dept, string):
                    match = True
                    break
            if match:
                results.append(course)

    def search_by_title(self, string):
        results = []
        for course in self.courses:
            match = False
            for title in course.title:
                if str_contains(title, string):
                    match = True
                    break
            if match:
                results.append(course)

    def search_by_units(self, string):
        results = []
        for course in self.courses:
            match = False
            for units in course.units:
                if str_contains(units, string):
                    match = True
                    break
            if match:
                results.append(course)

    def search_by_instructors(self, search_terms):
        results = []
        for course in self.courses:
            match = True
            for term in search_terms:
                if not str_contains(course.instructors, term):
                    match = False
                    break
            if match:
                results.append(course)

    def search_by_time(self, string):
        results = []
        for course in self.courses:
            match = False
            for time in course.time:
                if str_contains(time, string):
                    match = True
                    break
            if match:
                results.append(course)

    def search_by_core(self, search_terms):
        results = []
        for course in self.courses:
            match = True
            for term in search_terms:
                if not str_contains(course.core, term):
                    match = False
                    break
            if match:
                results.append(course)


####FIX ME#####

@app.route('/')
def view_root():
    return render_template('base.html')

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
