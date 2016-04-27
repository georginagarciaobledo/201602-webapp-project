from os import chdir
from os.path import dirname, realpath

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# FIXME write your app below
'''
DEPARTMENT_ABBREV = {
    'AMST': 'American Studies',
    'ARAB': 'Arabic',
    'ARTH': 'Art/History',
    'ARTM': 'Art/Media',
    'ARTS': 'Art/Studio',
    'BICH': 'Biochemistry',
    'BIO': 'Biology',
    'CHEM': 'Chemistry',
    'CHIN': 'Chinese',
    'COGS': 'Cognitive Science',
    'CSLC': 'Comparative Studies/Lit &amp; Cult',
    'COMP': 'Computer Science',
    'CTSJ': 'Critical Theory/Social Justice',
    'CSP': 'Cultural Studies Program',
    'DWA': 'Diplomacy and World Affairs',
    'ECON': 'Economics',
    'EDUC': 'Education',
    'ENGL': 'English',
    'FREN': 'French',
    'GEO': 'Geology',
    'GERM': 'German',
    'GRK': 'Greek',
    'HIST': 'History',
    'JAPN': 'Japanese',
    'KINE': 'Kinesiology',
    'LATN': 'Latin',
    'LLAS': 'Latino/a and Latin Amer Stud',
    'LING': 'Linguistics',
    'MATH': 'Mathematics',
    'MUSC': 'Music',
    'MUSA': 'Music Applied Study',
    'ABAR': 'Occidental-in-Argentina',
    'ABAU': 'Occidental-in-Australia',
    'ABAS': 'Occidental-in-Austria',
    'ABBO': 'Occidental-in-Bolivia',
    'ABBW': 'Occidental-in-Botswana',
    'ABBR': 'Occidental-in-Brazil',
    'ABCI': 'Occidental-in-Chile',
    'ABCH': 'Occidental-in-China',
    'ABCR': 'Occidental-in-Costa Rica',
    'ABCZ': 'Occidental-in-Czech Republic',
    'ABDE': 'Occidental-in-Denmark',
    'ABDR': 'Occidental-in-Dominican Repub',
    'ABFR': 'Occidental-in-France',
    'ABGE': 'Occidental-in-Germany',
    'ABHU': 'Occidental-in-Hungary',
    'ABIC': 'Occidental-in-Iceland',
    'ABIN': 'Occidental-in-India',
    'ABID': 'Occidental-in-Indonesia',
    'ABIR': 'Occidental-in-Ireland',
    'ABIT': 'Occidental-in-Italy',
    'ABJA': 'Occidental-in-Japan',
    'ABJO': 'Occidental-in-Jordan',
    'ABMO': 'Occidental-in-Morocco',
    'ABNZ': 'Occidental-in-New Zealand',
    'ABNI': 'Occidental-in-Nicaragua',
    'ABPE': 'Occidental-in-Peru',
    'ABRU': 'Occidental-in-Russia',
    'ABSM': 'Occidental-in-Samoa',
    'ABSE': 'Occidental-in-Senegal',
    'ABSA': 'Occidental-in-South Africa',
    'ABSP': 'Occidental-in-Spain',
    'ABSN': 'Occidental-in-Sweden',
    'ABSW': 'Occidental-in-Switzerland',
    'ABTN': 'Occidental-in-Taiwan',
    'ABNT': 'Occidental-in-the-Netherlands',
    'ABNA': 'Oxy-in-Netherlands Antilles',
    'ABUA': 'Oxy-in-United Arab Emirates',
    'ABUK': 'Oxy-in-the-United Kingdom',
    'PHIL': 'Philosophy',
    'PHAC': 'Physical Activities',
    'PHYS': 'Physics',
    'POLS': 'Politics',
    'PSYC': 'Psychology',
    'RELS': 'Religious Studies',
    'RUSN': 'Russian',
    'SOC': 'Sociology',
    'SPAN': 'Spanish',
    'OXAB': 'Study Abroad',
    'THEA': 'Theater',
    'UEP': 'Urban and Environmental Policy',
    'WRD': 'Writing and Rhetoric'}

CORE_ABBREV = {
    'CPAF': 'Core Africa & The Middle East',
    'CPAS': 'Core Central/South/East Asia',
    'CPEU': 'Core Europe',
    'CPFA': 'Core Fine Arts',
    'CFAP': 'Core Fine Arts Partial',
    'CPGC': 'Core Global Connections',
    'CPIC': 'Core Intercultural',
    'CPLS': 'Core Labratory Science',
    'CPLA': 'Core Latin America',
    'CMSP': 'Core Mathematics/Science Partial',
    'CPMS': 'Core Mathematics/Science',
    'CPPE': 'Core Pre-1800',
    'CPRF': 'Core Regional Focus',
    'CPUS': 'Core United States',
    'CPUD': 'Core United States Partial'}

YEAR_ABBREV = {
    '2010': '2010',
    '2011': '2011',
    '2012': '2012',
    '2013': '2013',
    '2014': '2014',
    '2015': '2015',
    '2016': '2016',
    '2017': '2017'}

SEASONS = {
    'spring': 'spring',
    'fall': 'fall',
    'summer': 'summer'
}
'''

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

@app.route('<semester>')
def semester_select(semester):
    results = []
    for course in get_data():
        if course.semester == semester:
            results.append(course)
    return render_template('semester.html', results = results)

@app.route('/<year>/<semester>')
def year_semester_select(year, semester):
    results = []
    for course in get_data():
        if course.year == year and course.semester == semester:
            results.append(course)
    return render_template('fall2010.html', results=results)




@app.route('/')
def view_homepage():
    return render_template('base.html')

'''
@app.route('/<semester>')
def view_course_info(semester):
    return render_template('semester.html')

@app.route('/<year>')
def view_course_info(year):
    return render_template('year.html')
'''



'''
@app.route('/fall2010')
def get_fall2010():
        fall2010options = []
        for key, value in get_data(course_data):
            fall2010options.append((key, value))
        fall2010options.sort(key=lambda  f: x[1])
        return render_template('fall2010.html', fall2010=fall2010options)






@app.route('/fall2010')
def view_course_info(year, semester, department, core):
    return render_template('fall2010.html')

@app.route('/department')
def view_alldepartment():
    listoptions = []
    for key, value in DEPARTMENT_ABBREV.items():
        listoptions.append((key, value))
    listoptions.sort(key=lambda x: x[1])
    return render_template('department2.html', department=listoptions)
'''

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
