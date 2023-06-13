# Todo List Project 

This repository contains a Todo List application developed using Django and React. The backend is built with Django and Django REST Framework, while the frontend is implemented using React.

## Features
- Create, update, and delete tasks.
- Mark tasks as complete or incomplete.
- Rate limiting using Redis to prevent excessive API requests.

## Prerequisites
Before running the project, make sure you have the following installed on your system:
- Python
- Django
- Django REST Framework
- Node.js
- npm 
- Redis

# Setup Django Instructions
Clone this repository to your local machine or download the ZIP file.
1. Clone this repository to your local machine or download the ZIP file.
```bash
git clone https://github.com/ziau-h/test.git
```
2. Navigate to the project directory.
```bash
cd test
```
3. Create Virtual environment and activate it
```bash
python -m venv env
source env/Scripts/activate
```
4. Install the required dependencies using pip.
```bash
pip install -r requirements.txt
```
4. Navigate to the project directory.

```bash
cd api
```
5. Apply database migrations.
```bash
python manage.py migrate
```
6. Start the Django development server.
```bash
python manage.py runserver
```

## Setup React Instructions
1. Navigate to the frontend directory.
```bash
cd frontend
```

2. Install the project dependencies.
```bash
npm install
```

3. Start the development server.
```bash
npm start
```

4. Open your web browser and visit `http://localhost:3000/`.

5. You should now be able to access and interact with the project.

## Contributing
Contributions are welcome! Please follow the guidelines in the CONTRIBUTING.md file.
