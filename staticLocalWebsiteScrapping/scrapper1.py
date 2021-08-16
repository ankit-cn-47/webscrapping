from bs4 import BeautifulSoup

with open('theTestFile.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    courses = soup.find_all("div", class_="card")
    for course in courses:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f"{course_name} costs {course_price}")
    # for course in courses:
    #     print(course.text)