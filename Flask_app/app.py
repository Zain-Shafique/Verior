from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact route (GET - display form)
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Contact route (POST - handle form submission)
@app.route('/contact', methods=['POST'])
def contact_post():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Basic validation
    if not name or not email or not message:
        flash('All fields are required!', 'error')
        return redirect(url_for('contact'))
    
    # Store the data (in a real app, you'd save to database)
    contact_data = {
        'name': name,
        'email': email,
        'message': message
    }
    
    return render_template('contact_success.html', data=contact_data)

# Services route with parameter
@app.route('/services')
@app.route('/services/<service_type>')
def services(service_type=None):
    service_list = {
        'web': 'Web Development',
        'mobile': 'Mobile App Development',
        'design': 'UI/UX Design',
        'consulting': 'Technical Consulting'
    }
    
    if service_type:
        service_name = service_list.get(service_type, 'Service Not Found')
        return render_template('service_detail.html', 
                             service_type=service_type, 
                             service_name=service_name)
    
    return render_template('services.html', services=service_list)

# Dynamic route with parameter
@app.route('/user/<username>')
def user_profile(username):
    return render_template('user_profile.html', username=username)

# Route with multiple parameters
@app.route('/blog/<int:year>/<int:month>/<slug>')
def blog_post(year, month, slug):
    return render_template('blog_post.html', year=year, month=month, slug=slug)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)