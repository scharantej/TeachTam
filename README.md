## Flask Application Design for Tamil Learning Website

### HTML Files

- **index.html**
  - The homepage of the website.
  - Contains a brief introduction to the website and a link to the lessons page.
- **lessons.html**
  - Lists all the available Tamil lessons.
  - Each lesson includes a title, a description, and a link to the lesson content.
- **lesson_content.html**
  - Contains the content of a specific Tamil lesson.
  - Includes text, audio, and interactive exercises to teach the lesson material.

### Routes

- **@app.route('/')**
  - Defines the route for the homepage.
  - Renders the index.html template.
- **@app.route('/lessons')**
  - Defines the route for the lessons page.
  - Renders the lessons.html template.
- **@app.route('/lesson/<int:lesson_id>')**
  - Defines the route for a specific lesson.
  - Renders the lesson_content.html template with the content for the specified lesson.