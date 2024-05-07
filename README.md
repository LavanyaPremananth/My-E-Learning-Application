# My-E-Learning-Website

**Description:**
The Educational Resource Management System is a web application built using Django, Django REST Framework, and WebSocket technology. It provides a platform for managing educational resources such as courses, texts, quizzes, and questions, facilitating collaboration between teachers and students.

**Features:**
1. **User Authentication:** Users can create accounts, log in, and log out. Teachers have additional privileges for managing courses and students.
2. **Course Management:** Teachers can create, edit, and delete courses. They can upload course materials, add quizzes, and manage course content.
3. **Real-Time Chat:** Users can engage in real-time chat discussions within course-specific chat rooms, enhancing collaboration and communication.
4. **Enrollment System:** Students can enroll themselves in available courses, gaining access to course materials and modules.
5. **Feedback System:** After completing a course, students can leave feedback and suggestions for course improvement.
6. **File Management:** Teachers can upload teaching materials/files to their accounts, making them accessible via the course home page for enrolled students.
7. **RESTful API:** The application provides a RESTful API for managing educational resources, allowing programmatic access to course data and functionalities.
8. **WebSocket Integration:** Real-time chat functionality is implemented using WebSocket technology, enabling instant communication between users within the application.

**Installation:**
1. Navigate to the project directory
2. Install dependencies: `pip install -r requirements.txt`
3. Apply migrations: `python manage.py migrate`
4. Run the development server: `python manage.py runserver`

**Create SuperUser:**
1. TO Create SuperUser: `python manage.py createsuperuser`

**Usage:**
1. Access the application through the browser: `http://localhost:8000`
2. Access the Admin Site through the browser: `http://127.0.0.1:8000/admin/`
3. Create a new account or log in with existing credentials.
4. Explore available courses, enroll in courses, and access course materials.
5. Engage in real-time chat discussions with other users within course-specific chat rooms.
6. Leave feedback and suggestions for courses upon completion.
7. Teachers can manage courses, upload materials, and interact with students through the admin panel.

**Acknowledgments:**
Special thanks to the Django community and contributors to Django REST Framework and WebSocket libraries for their invaluable contributions to open-source software development.
