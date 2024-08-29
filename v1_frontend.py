############## Neil Bharwani ##############

import os
import requests
import datetime

os.system("cls" if os.name == "nt" else "clear")

os.environ["TEAM_API_KEY"] = "358bbb41895ec8afe6917f5ad7c50151ba8c9aa937c0b6466a9cc9e6fb0bc7d1"

try:
    from aixplain.factories import PipelineFactory
except ImportError as e:
    os.system("pip install aixplain")
    from aixplain.factories import PipelineFactory
    os.system("cls" if os.name == "nt" else "clear")

pipeline = PipelineFactory.get("api key")

gpa = ""
math_grade = ""
science_grade = ""
english_grade = ""
world_language = ""
ap_courses = ""
honors_courses = ""
sat_score = ""
volunteer_hours = ""
volunteer_hours = volunteer_hours + " Hours"
extracurricular_activities = ", , ,"
country = "US"

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
"""

result = pipeline.run(query)

output_url = result["data"][0]["segments"][0]["response"]
response = requests.get(output_url)
content = response.text

os.system("cls" if os.name == "nt" else "clear")

print(content)
