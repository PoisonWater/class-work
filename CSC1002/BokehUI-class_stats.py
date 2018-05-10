### python3 -m bokeh serve --show ui_assWhole.py
import pyodbc
from functools import partial
from bokeh.io import output_file, show
from bokeh.layouts import row, column, layout, widgetbox
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider, TextInput
from bokeh.models.widgets import RadioGroup, CheckboxGroup, MultiSelect, Dropdown
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn, Panel, Tabs
from bokeh.models.widgets import Paragraph
from bokeh.events import ButtonClick
from bokeh.palettes import Spectral6
from datetime import date
from random import randint
import string
from bokeh.core.properties import value

attr = dict(
    server = '10.20.213.10',
    database = 'csc1002',
    username = 'csc1002',
    password = 'csc1002',
    port = 1433,
    driver = 'ODBC Driver 13 for SQL Server'
)

conn_str = 'DRIVER={driver};'\
    'SERVER={server};'\
    'PORT={port};'\
    'DATABASE={database};'\
    'UID={username};'\
    'PWD={password}'

conn_str = conn_str.format(**attr)
def obdcConnection():
    try:
        return pyodbc.connect(conn_str)
    except Exception as e:
        print(e)
        quit()
        
cursor = obdcConnection().cursor()

getDept = 'SELECT dept_name FROM lgu.student'
tsql = 'SELECT * FROM lgu.course'
gpa = ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
years = ["2015", "2016", "2017"]
colors = ["#c9d9d3", "#718dbf", "#e84d60"]

refresh = Button(label="Refresh")
btnGroupTitle = RadioButtonGroup(name='title', labels=["begins with...", "...contains...", "...ends with"], active=1)
btnGroupDept = RadioButtonGroup(name='dept', labels=["begins with...", "...contains...", "...ends with"], active=1)
paragraph = Paragraph(text="option")
optionGroup = RadioGroup(labels=["and", "or"], active=0, width=100, inline=True)
btnGroupLetters = RadioButtonGroup(labels=list(string.ascii_uppercase), active=-1)
title_input = TextInput(value="", title="Title:", placeholder="contains....")
dept_input = TextInput(value="", title="Department:", placeholder="contains....")

with cursor:    # get dept names
    rows = cursor.execute(getDept).fetchall()
    deptList = []
    for row in rows:
        if row.dept_name not in deptList:
            deptList.append(row.dept_name)
    deptList.sort()
select = Select(title="Department:", value=deptList[0], options=deptList)
deptname = widgetbox(select)

###data table
columns = [
    TableColumn(field = 'id', title = 'Course ID'),
    TableColumn(field = 'title', title = 'Title'),
    TableColumn(field = 'dept', title = 'Department'),
    TableColumn(field = 'credit', title = 'Credit'),
    TableColumn(field = 'instructor', title = 'Instructor')
]
table_master = DataTable(source=ColumnDataSource(), columns = columns, width = 800, height = 200)
data = dict(
    id = [],
    title = [],
    dept = [],
    credit = [],
    instructor = []
)
with cursor:
    rows = cursor.execute(tsql).fetchall()
    for row in rows:
        data['id'].append('{id}'.format(id = row.course_id))
        data['title'].append('{title}'.format(title = row.title))
        data['dept'].append('{dept}'.format(dept = row.dept_name))
        data['credit'].append('{credit}'.format(credit = row.credits))
        data['instructor'].append('{instructor}'.format(instructor = row.instructor))

table_master.source.data = data

def select_handler(attr, old, new):
    global data1, source 
    print('Select value changed from {} to {}'.format(old, new))
    data1 = {'gpa' : gpa,
        '2015'   : [],
        '2016'   : [],
        '2017'   : []}
    with cursor:    # get related gpa
        for i in ['2015','2016','2017']:
            rows = cursor.execute('SELECT dept_name, gpa, year FROM lgu.student WHERE year = \'{}\' and dept_name = \'{}\''.format(i, new)).fetchall()
            p0, p1, p2, p3, p4, p5, p6, p7, p8 = 0,0,0,0,0,0,0,0,0
            for row in rows:
                if row.gpa == 'A+':
                    p0 += 1
                elif row.gpa == 'A':
                    p1 += 1
                elif row.gpa == 'B+':
                    p2 += 1
                elif row.gpa == 'B':
                    p3 += 1
                elif row.gpa == 'C+':
                    p4 += 1
                elif row.gpa == 'C':
                    p5 += 1
                elif row.gpa == 'D+':
                    p6 += 1
                elif row.gpa == 'D':
                    p7 += 1
                elif row.gpa == 'F':
                    p8 += 1
            for t in [p0, p1, p2, p3, p4, p5, p6, p7, p8]:
                data1[i].append(t)
    source.data = data1

select.on_change('value',select_handler)

placeholder = {0:"begins with...", 1: "...contains...",2: "...ends with"}

def UpdatePlaceHolderT(idx):
    print(idx, placeholder[idx])
    title_input.placeholder = placeholder[idx]
def UpdatePlaceHolderD(idx):
    print(idx, placeholder[idx])
    dept_input.placeholder = placeholder[idx]

btnGroupTitle.on_click(UpdatePlaceHolderT)
btnGroupDept.on_click(UpdatePlaceHolderD)
data1 = {'gpa' : gpa,
    '2015'   : [],
    '2016'   : [],
    '2017'   : []}

with cursor:    # get related gpa
    for i in ['2015','2016','2017']:
        rows = cursor.execute('SELECT dept_name, gpa, year FROM lgu.student WHERE year = \'{}\' and dept_name = \'{}\''.format(i, deptList[0])).fetchall()
        p0, p1, p2, p3, p4, p5, p6, p7, p8 = 0,0,0,0,0,0,0,0,0
        for row in rows:
            if row.gpa == 'A+':
                p0 += 1
            elif row.gpa == 'A':
                p1 += 1
            elif row.gpa == 'B+':
                p2 += 1
            elif row.gpa == 'B':
                p3 += 1
            elif row.gpa == 'C+':
                p4 += 1
            elif row.gpa == 'C':
                p5 += 1
            elif row.gpa == 'D+':
                p6 += 1
            elif row.gpa == 'D':
                p7 += 1
            elif row.gpa == 'F':
                p8 += 1
        for t in [p0, p1, p2, p3, p4, p5, p6, p7, p8]:
            data1[i].append(t)
source = ColumnDataSource(data=data1)
source.data = data1

def OnLetterSelected(idx):
    letter = string.ascii_uppercase[idx]
    data = dict(
        id = [],
        title = [],
        dept = [],
        credit = [],
        instructor = []
    )
    with cursor:
        tsql1 = "SELECT * FROM lgu.course WHERE title like '{}%'"
        rows = cursor.execute(tsql1.format(string.ascii_uppercase[idx])).fetchall()
        for row in rows:
            data['id'].append('{id}'.format(id = row.course_id))
            data['title'].append('{title}'.format(title = row.title))
            data['dept'].append('{dept}'.format(dept = row.dept_name))
            data['credit'].append('{credit}'.format(credit = row.credits))
            data['instructor'].append('{instructor}'.format(instructor = row.instructor))
    table_master.source.data = data
    print(idx, letter)

btnGroupLetters.on_click(OnLetterSelected)

def OnRefreshClick():
    title = title_input.value
    dept = dept_input.value
    active = optionGroup.active
    if active == 0:
        active = 'and'
    else:
        active = 'or'
    if title_input.placeholder == placeholder[0]:
        title = title + '%'
    elif title_input.placeholder == placeholder[2]:
        title = '%' + title
    else:
        title = '%' + title + '%'
    if dept_input.placeholder == placeholder[0]:
        dept = dept + '%'
    elif dept_input.placeholder == placeholder[2]:
        dept = '%' + dept
    else:
        dept = '%' + dept + '%'
    data = dict(
        id = [],
        title = [],
        dept = [],
        credit = [],
        instructor = []
    )
    with cursor:
        tsql1 = "SELECT * FROM lgu.course WHERE title like '{}' {} dept_name like '{}'"
        rows = cursor.execute(tsql1.format(title,active,dept)).fetchall()
        for row in rows:
            data['id'].append('{id}'.format(id = row.course_id))
            data['title'].append('{title}'.format(title = row.title))
            data['dept'].append('{dept}'.format(dept = row.dept_name))
            data['credit'].append('{credit}'.format(credit = row.credits))
            data['instructor'].append('{instructor}'.format(instructor = row.instructor))
    table_master.source.data = data
    print('refresh title: {} Dept: {} Option:{}'.format(title,dept,active))

refresh.on_click(OnRefreshClick)

layout_query = layout(
    [
        [widgetbox(btnGroupLetters, width=1000)],
        [widgetbox(btnGroupTitle), widgetbox(btnGroupDept)],
        [widgetbox(title_input), widgetbox(paragraph, optionGroup, width=100), widgetbox(dept_input)],
        [widgetbox(refresh, width=100)],
        [widgetbox(table_master)]
    ]
)

s1 = figure(x_range=gpa, plot_height=350, title="GPA situations by Year",
        toolbar_location=None, tools="")

s1.vbar_stack(years, x='gpa', width=0.9, color=colors, source=source, legend=[value(x) for x in years], name=years)

layout_chart = layout (
    [[widgetbox(select),s1]]
)

tab1 = Panel(child=layout_query, title="Course Info")
tab2 = Panel(child=layout_chart, title="Statistics")
tabs = Tabs(tabs=[tab1, tab2])

curdoc().add_root(tabs)