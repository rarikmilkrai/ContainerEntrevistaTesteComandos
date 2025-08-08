from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # The container's IP will be dynamically determined.
    # For now, we'll use a placeholder.
    # The user will be 'challengeuser' and the password 'password'
    challenges = [
        {
            "id": 1,
            "title": "Acesso SSH",
            "description": "Acesse a máquina via SSH com o usuário 'challengeuser' e a senha 'password'. O endereço de IP do contêiner será exibido no terminal quando você o iniciar. O comando para acessar será parecido com: ssh challengeuser@<IP_DO_CONTAINER>",
            "next_step": "Depois de acessar, você estará pronto para o próximo desafio."
        },
        {
            "id": 2,
            "title": "Criação de Grupo",
            "description": "Dentro da sessão SSH, crie um novo grupo chamado 'desafio'. O comando para isso é: sudo addgroup desafio",
            "next_step": "Após criar o grupo, verifique se ele existe com o comando: cat /etc/group | grep desafio"
        },
        {
            "id": 3,
            "title": "Listando Grupos",
            "description": "Liste todos os grupos existentes na máquina para confirmar que o seu grupo foi criado.",
            "next_step": "Parabéns, você completou os desafios!"
        }
    ]
    return render_template('index.html', challenges=challenges)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
