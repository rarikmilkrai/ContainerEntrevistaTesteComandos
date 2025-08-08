from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    junior_challenges = [
        {
            "id": "J1",
            "title": "Criar Usuário",
            "description": "Crie um novo usuário chamado 'operador' com um diretório home.",
            "correction": "sudo useradd -m operador"
        },
        {
            "id": "J2",
            "title": "Alterar Senha",
            "description": "Altere a senha do usuário 'operador' para 'Senha123'.",
            "correction": "echo 'operador:Senha123' | sudo chpasswd"
        },
        {
            "id": "J3",
            "title": "Criar Grupo",
            "description": "Crie um novo grupo chamado 'projetos'.",
            "correction": "sudo groupadd projetos"
        },
        {
            "id": "J4",
            "title": "Adicionar Usuário a Grupo",
            "description": "Adicione o usuário 'operador' ao grupo 'projetos'.",
            "correction": "sudo usermod -aG projetos operador"
        },
        {
            "id": "J5",
            "title": "Verificar Espaço em Disco",
            "description": "Verifique o espaço disponível em disco em um formato legível para humanos.",
            "correction": "df -h"
        },
        {
            "id": "J6",
            "title": "Listar Usuários",
            "description": "Liste o nome de todos os usuários do sistema a partir do arquivo /etc/passwd.",
            "correction": "cut -d: -f1 /etc/passwd"
        },
        {
            "id": "J7",
            "title": "Alterar Hostname",
            "description": "Altere o hostname da máquina para 'vm-analista'.",
            "correction": "sudo hostnamectl set-hostname vm-analista"
        },
        {
            "id": "J8",
            "title": "Configurar Timezone",
            "description": "Configure o timezone do sistema para 'America/Sao_Paulo'.",
            "correction": "sudo timedatectl set-timezone America/Sao_Paulo"
        },
        {
            "id": "J9",
            "title": "Criar Diretório com Permissões",
            "description": "Crie um diretório '/backups', defina o grupo 'projetos' como dono e dê permissão total para o usuário dono e para o grupo.",
            "correction": "sudo mkdir /backups && sudo chgrp projetos /backups && sudo chmod 770 /backups"
        },
        {
            "id": "J10",
            "title": "Localizar Arquivos",
            "description": "Localize todos os arquivos com a extensão '.log' dentro do diretório '/var/log'.",
            "correction": "sudo find /var/log -name '*.log'"
        },
        {
            "id": "J11",
            "title": "Editar Arquivo /etc/hosts",
            "description": "Adicione a seguinte entrada ao arquivo /etc/hosts: '192.168.1.50 servidor1'.",
            "correction": "echo '192.168.1.50 servidor1' | sudo tee -a /etc/hosts"
        },
        {
            "id": "J12",
            "title": "Instalar um Pacote",
            "description": "Instale o pacote 'wget'.",
            "correction": "sudo apt-get update && sudo apt-get install -y wget"
        },
        {
            "id": "J13",
            "title": "Verificar Status de Serviço",
            "description": "Verifique se o serviço 'sshd' está ativo.",
            "correction": "sudo systemctl status sshd"
        },
        {
            "id": "J14",
            "title": "Listar Portas de Rede",
            "description": "Verifique quais serviços estão escutando em portas de rede (TCP e UDP).",
            "correction": "ss -tuln"
        },
        {
            "id": "J15",
            "title": "Encontrar PID de Processo",
            "description": "Descubra o ID do processo (PID) do serviço 'sshd'.",
            "correction": "pgrep sshd"
        },
        {
            "id": "J16",
            "title": "Criar um Alias",
            "description": "Crie um alias permanente chamado 'atualiza' que execute a atualização dos pacotes do sistema.",
            "correction": "echo \\\"alias atualiza='sudo apt-get update && sudo apt-get upgrade -y'\\\" >> ~/.bashrc && source ~/.bashrc"
        },
        {
            "id": "J17",
            "title": "Criar um Script Simples",
            "description": "Crie um script executável em '/usr/local/bin/showdate' que exiba a data e a hora atuais.",
            "correction": "echo -e '#!/bin/bash\\ndate' | sudo tee /usr/local/bin/showdate > /dev/null && sudo chmod +x /usr/local/bin/showdate"
        },
        {
            "id": "J18",
            "title": "Editar Mensagem do Dia",
            "description": "Edite o arquivo '/etc/motd' para que exiba a mensagem 'Bem-vindo ao sistema!' no login.",
            "correction": "echo 'Bem-vindo ao sistema!' | sudo tee /etc/motd"
        }
    ]

    pleno_challenges = [
        {
            "id": "P1",
            "title": "Particionamento com fdisk",
            "description": "Crie um arquivo de 1GB em '/disk.img' para simular um disco. Associe-o a um dispositivo de loop (ex: /dev/loop0). Use 'fdisk' para criar uma nova partição primária neste disco e formate-a com o sistema de arquivos 'ext4'. (Nota: use 'sudo losetup -f' para achar um loop livre)",
            "correction": "sudo fallocate -l 1G /disk.img && LOOP_DEV=$(sudo losetup -f) && sudo losetup $LOOP_DEV /disk.img && echo -e 'n\\np\\n1\\n\\n\\nw' | sudo fdisk $LOOP_DEV && sudo mkfs.ext4 ${LOOP_DEV}p1"
        },
        {
            "id": "P2",
            "title": "Gerenciamento com LVM",
            "description": "Usando dois dispositivos de loop de 500MB cada, crie um Volume Group (VG) chamado 'vgdata' e um Logical Volume (LV) de 800MB chamado 'lvdata'. Formate-o com 'ext4' e monte-o em '/mnt/data'.",
            "correction": "# Criar discos e VG: sudo fallocate -l 500M /disk1.img && sudo fallocate -l 500M /disk2.img && ... && sudo vgcreate vgdata /dev/loop0 /dev/loop1 && sudo lvcreate -L 800M -n lvdata vgdata && sudo mkfs.ext4 /dev/vgdata/lvdata && sudo mkdir /mnt/data && sudo mount /dev/vgdata/lvdata /mnt/data"
        },
        {
            "id": "P3",
            "title": "Redimensionar um LVM",
            "description": "Aumente o tamanho do LV 'lvdata' em mais 200MB e expanda o sistema de arquivos para ocupar o novo espaço.",
            "correction": "sudo lvextend -L+200M /dev/vgdata/lvdata && sudo resize2fs /dev/vgdata/lvdata"
        },
        {
            "id": "P4",
            "title": "Script de Verificação de Serviço",
            "description": "Crie um script que verifique se o serviço 'apache2' está ativo. Se não estiver, o script deve iniciá-lo.",
            "correction": "echo -e '#!/bin/bash\\nif ! systemctl is-active --quiet apache2; then\\n    sudo systemctl start apache2\\nfi' > check_apache.sh && chmod +x check_apache.sh"
        },
        {
            "id": "P5",
            "title": "Agendamento com Cron",
            "description": "Agende uma tarefa no cron para que, todo dia à 1h da manhã, o sistema apague arquivos com a extensão '.tmp' no diretório '/tmp'.",
            "correction": "(crontab -l 2>/dev/null; echo '0 1 * * * find /tmp -name \\\"*.tmp\\\" -delete') | sudo crontab -"
        },
        {
            "id": "P6",
            "title": "Regra de Firewall (UFW)",
            "description": "Usando o 'ufw', crie uma regra que permita o acesso à porta 22 (SSH) apenas para a rede '192.168.10.0/24'.",
            "correction": "sudo ufw allow from 192.168.10.0/24 to any port 22 proto tcp"
        },
        {
            "id": "P7",
            "title": "Serviço Customizado com SystemD",
            "description": "Crie um serviço systemd chamado 'meu-servico.service' que executa o script '/usr/local/bin/showdate' (criado no nível júnior). Habilite e inicie o serviço.",
            "correction": "echo -e '[Unit]\\nDescription=Meu Servico\\n\\n[Service]\\nExecStart=/usr/local/bin/showdate\\n\\n[Install]\\nWantedBy=multi-user.target' | sudo tee /etc/systemd/system/meu-servico.service && sudo systemctl enable --now meu-servico.service"
        },
        {
            "id": "P8",
            "title": "Manipulação de Texto com 'sed'",
            "description": "Crie um arquivo 'log.txt' com a palavra 'erro' repetida várias vezes. Use o 'sed' para substituir todas as ocorrências de 'erro' por 'falha' diretamente no arquivo.",
            "correction": "echo 'erro erro erro' > log.txt && sed -i 's/erro/falha/g' log.txt"
        },
        {
            "id": "P9",
            "title": "Manipulação de Texto com 'awk'",
            "description": "Use 'awk' para listar o nome de todos os usuários do sistema que possuem um UID (User ID) igual ou superior a 1000.",
            "correction": "awk -F: '$3 >= 1000 {print $1}' /etc/passwd"
        },
        {
            "id": "P10",
            "title": "Configurar Virtual Hosts no Apache",
            "description": "Configure dois virtual hosts no Apache: 'site1.desafio.com' e 'site2.desafio.com'. Cada um deve ter seu próprio arquivo de índice em diretórios separados dentro de '/var/www/'. Teste o acesso a eles usando 'curl' com o cabeçalho 'Host'.",
            "correction": "# Criar dirs: sudo mkdir -p /var/www/site1.desafio.com && sudo mkdir -p /var/www/site2.desafio.com ... criar arquivos de conf em /etc/apache2/sites-available/ e usar a2ensite"
        },
        {
            "id": "P11",
            "title": "Restringir Acesso SSH",
            "description": "Crie um grupo chamado 'restrito'. Adicione uma configuração ao 'sshd_config' para proibir o login SSH de qualquer usuário que pertença a este grupo.",
            "correction": "sudo groupadd restrito && echo -e '\\nMatch Group restrito\\n    PasswordAuthentication no' | sudo tee -a /etc/ssh/sshd_config.d/60-custom.conf && sudo systemctl reload sshd"
        },
        {
            "id": "P12",
            "title": "Análise de Logs de Acesso",
            "description": "Gere um relatório a partir do '/var/log/apache2/access.log' que mostre uma contagem de quantos requests cada endereço IP fez.",
            "correction": "sudo awk '{print $1}' /var/log/apache2/access.log | sort | uniq -c | sort -nr"
        }
    ]

    senior_challenges = [
        {
            "id": "S1",
            "title": "Troubleshooting com SystemD",
            "description": "Um serviço chamado 'servico-quebrado.service' foi criado, mas falha ao iniciar. Investigue o log do sistema com 'journalctl' para descobrir a causa do erro, corrija o problema e inicie o serviço com sucesso.",
            "correction": "# O serviço aponta para um script inexistente. O candidato deve criar o script ou corrigir o .service. journalctl -u servico-quebrado.service"
        },
        {
            "id": "S2",
            "title": "Análise de Processos com 'strace'",
            "description": "Use o 'strace' para monitorar o processo 'sshd' e descobrir quais arquivos de configuração ele lê durante a inicialização. Salve a saída em um arquivo.",
            "correction": "sudo strace -o /tmp/sshd_trace.txt -f $(pgrep -f /usr/sbin/sshd | head -1)"
        },
        {
            "id": "S3",
            "title": "Segurança com AppArmor",
            "description": "Crie um perfil AppArmor para confinar um script '/usr/local/bin/meu_script' para que ele só possa ler o arquivo '/etc/hosts' e nada mais. Coloque o perfil em modo 'enforce'.",
            "correction": "# Criar perfil em /etc/apparmor.d/usr.local.bin.meu_script e usar apparmor_parser."
        },
        {
            "id": "S4",
            "title": "Networking com 'iproute2'",
            "description": "Crie uma nova interface de rede do tipo 'bridge' chamada 'br0'. Atribua a ela o endereço IP '10.20.30.1/24' e ative-a.",
            "correction": "sudo ip link add name br0 type bridge && sudo ip addr add 10.20.30.1/24 dev br0 && sudo ip link set br0 up"
        },
        {
            "id": "S5",
            "title": "Scripting Avançado em Bash",
            "description": "Escreva um script em Bash que aceite um nome de usuário como argumento. O script deve verificar se o argumento foi fornecido. Se sim, deve verificar se o usuário existe no sistema. Se existir, deve listar todos os processos pertencentes a esse usuário. O script deve ter tratamento de erros para cada etapa.",
            "correction": "# O script deve usar if [ -z $1 ], id $1, e ps -u $1."
        },
        {
            "id": "S6",
            "title": "Conceitos de Orquestração",
            "description": "Em um arquivo de texto em '/root/resposta.txt', explique a principal diferença entre um 'Deployment' e um 'StatefulSet' no Kubernetes e dê um exemplo de caso de uso para cada um.",
            "correction": "# Resposta textual. Deployment para apps stateless (web server), StatefulSet para apps stateful (banco de dados)."
        },
        {
            "id": "S7",
            "title": "Ajuste de Performance do Kernel",
            "description": "Use 'sysctl' para alterar o parâmetro do kernel 'net.core.somaxconn' para '1024'. A alteração deve ser persistente após reinicializações.",
            "correction": "sudo sysctl -w net.core.somaxconn=1024 && echo 'net.core.somaxconn = 1024' | sudo tee /etc/sysctl.d/99-custom.conf"
        },
        {
            "id": "S8",
            "title": "Backup com 'tar' e Exclusões",
            "description": "Crie um arquivo de backup compactado de todo o diretório '/var', mas exclua o subdiretório '/var/log'.",
            "correction": "sudo tar --exclude='/var/log' -czvf /tmp/backup_var.tar.gz /var"
        },
        {
            "id": "S9",
            "title": "Análise de Segurança com Trivy",
            "description": "Instale a ferramenta de scanner de vulnerabilidades 'Trivy' e execute uma varredura na imagem base do próprio contêiner ('ubuntu:22.04') para encontrar vulnerabilidades críticas.",
            "correction": "# A correção envolve instalar o Trivy (via wget/dpkg) e executar 'trivy image ubuntu:22.04 --severity CRITICAL'"
        }
    ]

    return render_template('index.html', junior_challenges=junior_challenges, pleno_challenges=pleno_challenges, senior_challenges=senior_challenges)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
