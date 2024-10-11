from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Валідація - проста перевірка на наявність даних
        if username and password:
            # Формат запису: username і password
            data = f"Username: {username} | Password: {password}\n"
            
            # Відкриваємо файл для запису, або створюємо новий, якщо його не існує
            with open('user_data.txt', 'a') as file:
                file.write(data)
                
            # Підтверджуємо успішний запис
            return "Login successful. Data saved!"
        else:
            return "Please fill in both username and password."
    
    # HTML форма
    return render_template_string('''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
