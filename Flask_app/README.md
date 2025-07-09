# Flask Multi-Route Application

## Directory Structure

Create the following directory structure:

```
Flask_app/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── service_detail.html
│   ├── contact.html
│   ├── contact_success.html
│   ├── user_profile.html
│   └── blog_post.html
└── requirements.txt
```

## Installation Steps

### 1. Create Virtual Environment

```bash
python -m venv flask-env
source flask-env/bin/activate  # On Windows: flask-env\Scripts\activate
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Key Features Demonstrated

### Task 01: Multiple Routes & Navigation

✅ **Multiple routes**: `/about`, `/contact`, `/services`  
✅ **Route parameters**: `/services/<service_type>`, `/user/<username>`  
✅ **Navigation menu**: Fully functional navigation with all routes  
✅ **URL generation**: Uses `url_for()` for dynamic URL generation  

### Task 02: Contact Form with POST

✅ **Contact form**: Complete form with name, email, and message fields  
✅ **POST handling**: Processes form data via POST method  
✅ **Data display**: Shows submitted data on success page  
✅ **Form validation**: Basic validation with flash messages  
✅ **Error handling**: Redirects back to form with error messages  

## Route Examples

### Static Routes

- `/` - Home page
- `/about` - About page
- `/contact` - Contact form (GET) and form handler (POST)
- `/services` - Services listing

### Dynamic Routes with Parameters

- `/services/<service_type>` - Service detail page
- `/user/<username>` - User profile page
- `/blog/<int:year>/<int:month>/<slug>` - Blog post with multiple parameters

## Advanced Features

### 1. Template Inheritance

- Base template (`base.html`) with common layout
- Child templates extend the base template
- Consistent navigation and styling

### 2. Form Handling

- GET request displays the form
- POST request processes form data
- Flash messages for user feedback
- Data validation and error handling

### 3. URL Parameters

- String parameters: `<username>`
- Integer parameters: `<int:year>`
- Multiple parameters in single route
- Optional parameters with default values

### 4. Template Context

- Passing data from routes to templates
- Using Jinja2 template engine features
- Conditional rendering based on parameters

## Testing the Application

### Test Static Routes

- Visit `http://localhost:5000/` (Home)
- Visit `http://localhost:5000/about` (About)
- Visit `http://localhost:5000/services` (Services)
- Visit `http://localhost:5000/contact` (Contact)

### Test Dynamic Routes

- Visit `http://localhost:5000/user/alice` (Alice's Profile)
- Visit `http://localhost:5000/blog/2024/1/flask-tutorial` (Blog Post)

### Test Form Submission

- Go to `/contact`
- Fill out the form
- Submit and verify data appears on success page
- Test validation by submitting empty form

## Code Explanation

### Route Definitions

```python
@app.route('/services/<service_type>')
def services(service_type=None):
    # Handle both /services and /services/<type>
    # service_type parameter is passed to template
```

### POST Form Handling

```python
@app.route('/contact', methods=['POST'])
def contact_post():
    # Extract form data
    name = request.form.get('name')
    # Validate and process
    # Redirect or render template
```

### Template Rendering

```python
return render_template('template.html', 
                      variable=value,
                      data=data_dict)
```

---

### 📹 Demo Video

Watch the complete demonstration of this Flask application:

🎥 **[Flask Multi-Route Application Demo](https://drive.google.com/file/d/1WeO37USf0L5AZQ0bx5uIA_UNzFCr7zcA/view?usp=sharing)**

This application demonstrates all the core Flask concepts for routing, request handling, and template rendering!
