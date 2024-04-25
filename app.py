from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        print(f'Username: {username}, Email: {email}, Password: {password}')
        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f'Name: {name}, Email: {email}, Message: {message}')

        return redirect(url_for('index'))

  
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
 
        username = request.form.get('username')
        password = request.form.get('password')

        print(f'Username: {username}, Password: {password}')

        return redirect(url_for('index'))


    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)


