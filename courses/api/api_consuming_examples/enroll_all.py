import requests
base_url = 'http://127.0.0.1:8000/api/'
res = requests.get(f'{base_url}courses/')
courses = res.json()
avail_courses = ' , '.join([course['title'] for course in courses])
print(f'available courses :{avail_courses}')

username = 'gaju'
password = '12345'

for course in courses:
    course_id = course['id']
    course_title = course['title']
    res = requests.post(
        f'{base_url}courses/{course_id}/enroll/', auth=(username, password))
    if res.status_code == 200:
        print(f'Successfully enrolled in {course_title}')
