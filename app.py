from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

usuarios = {
    "Karina": "12345",
    "usuario2": "senha2"
}

@app.route('/')
def home():
    
    if 'usuario' in session:
        return f"Bem-vindo, {session['usuario']}!" 
    return "Bem-vindo à página inicial!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario in usuarios and usuarios[usuario] == senha:
            session['usuario'] = usuario  
            return('Login bem-sucedido!')
            return redirect(url_for('home'))
        else:
            return('Usuário ou senha inválidos!')
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None) 
    return('Você saiu com sucesso!')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

