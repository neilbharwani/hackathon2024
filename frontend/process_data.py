from flask import Flask, request, render_template, jsonify, redirect, url_for, make_response, session
import os
import requests
import markdown
import datetime
from aixplain.factories import PipelineFactory
import html
import re
pipeline = PipelineFactory.get("668f8415223429092ea2082f")

os.environ["TEAM_API_KEY"] = "api key"

app = Flask(__name__)
app.secret_key = 'secret '

ai_context = {}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    print(request.cookies.get('session'))
    data = request.form

    # Extract data from the form
    gpa = data.get('gpa')
    math_grade = data.get('math_grade')
    science_grade = data.get('science_grade')
    english_grade = data.get('english_grade')
    world_language = data.get('world_language')
    ap_courses = data.get('ap_courses')
    honors_courses = data.get('honors_courses')
    sat_score = data.get('sat_score')
    volunteer_hours = data.get('volunteer_hours')
    extracurricular_activities = data.get('extracurricular_activities')
    country = data.get('country')

    # Grade pattern for validation (A-F or 0-100)
    grade_pattern = lambda x: x.isdigit() and 0 <= int(x) <= 100 or x.upper() in 'ABCDF'

    # Validation
    try:
        if not 0.0 <= float(gpa) <= 4.0:
            raise ValueError('GPA must be between 0.0 and 4.0.')
        if not grade_pattern(math_grade) or not grade_pattern(science_grade) or not grade_pattern(english_grade):
            raise ValueError('Grades must be A-F or 0-100.')
        if not (400 <= int(sat_score) <= 1600):
            raise ValueError('SAT score must be between 400 and 1600.')
        if not int(volunteer_hours) >= 0:
            raise ValueError('Volunteer hours must be non-negative.')
    except ValueError as e:
        return jsonify({'status': 'error', 'message': str(e)})

    # print(f"GPA: {gpa}, Math Grade: {math_grade}, Science Grade: {science_grade}, English Grade: {english_grade}")
    # print("Form data recieved")

    query = f"""
    What colleges can I apply to with these grades:
    GPA: {gpa}
    Math Grade: {math_grade}
    Science Grade: {science_grade}
    English Grade: {english_grade}
    World Language: {world_language}
    AP Courses: {ap_courses}
    Honors Courses: {honors_courses}
    SAT Score: {sat_score}
    Volunteer Hours: {volunteer_hours}
    Extracurricular Activities: {extracurricular_activities}

    Use the {country} college system.

    At the end make a paragraph, provide some future steps to help me get into some better colleges.

    Use this final format with good markdowns:
    1. College 1
    [Information About College 1] (Advantages and Disadvatages)
    2. College 2
    [Information About College 2] (Advantages and Disadvatages)
    3. College 3
    [Information About College 3] (Advantages and Disadvatages)

    [Paragraph about how to get into better colleges using my grades.]

    AI Note: Format in HTML, only generate the body. Left align all the HTML.
    """

    result = pipeline.run(query)

    output_url = result["data"][0]["segments"][0]["response"]
    response = requests.get(output_url)
    content = response.text
    content = content.replace('```html', '')
    content = content.replace('```', '')
    # session.permanent = True
    # session["ai_content"] = content
    ai_context['context'] = content
    render = render_template('student_info.html',
                            gpa=gpa,
                           math_grade=math_grade,
                           science_grade=science_grade,
                           english_grade=english_grade,
                           world_language=world_language,
                           ap_courses=ap_courses,
                           honors_courses=honors_courses,
                           sat_score=sat_score,
                           volunteer_hours=volunteer_hours,
                           extracurricular_activities=extracurricular_activities,
                           country=country,
                           Resp=content
    )
    response = make_response(html.unescape(render))
    response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
    response.headers['Content-Type'] = 'text/html'

    return response



@app.route('/result2', methods=['POST'])
def result2():
    print(request.cookies.get('session'))
    data = list(request.form.listvalues())
    content = ai_context['context']
    # print(session['ai_content'])
    # print(ai_context['context'])
    # print(content)
    # print(data)
    query = f"""
      referring to {content}, could you please answer this:
      {data}

    AI Note: Dont markdown the response.
    """

    result = pipeline.run(query)


    output_url = result["data"][0]["segments"][0]["response"]
    response = requests.get(output_url)
    content = response.text

    response = make_response(html.unescape(content))
    response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
    response.headers['Content-Type'] = 'text/html'

    return response



if __name__ == '__main__':
    app.run(debug=True)
