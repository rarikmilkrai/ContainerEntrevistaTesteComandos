# Desafios de Linha de Comando em um Contêiner Docker (V2)

Este projeto cria um ambiente de contêiner Docker com uma série de desafios de linha de comando, agora estruturados por nível de senioridade (Júnior, Pleno e Sênior). O objetivo é que o usuário interaja com o contêiner através de uma interface web e de uma sessão SSH para resolver os desafios propostos.

## Níveis de Desafio

-   **Nível Júnior:** Focado em comandos básicos de navegação, manipulação de arquivos, usuários, grupos e pacotes.
-   **Nível Pleno:** Abrange tópicos intermediários como LVM, particionamento, serviços systemd, firewall e scripting básico.
-   **Nível Sênior:** Desafios avançados envolvendo troubleshooting, análise de performance com `strace`, segurança com AppArmor, networking e conceitos de orquestração.

## Como Usar

### Pré-requisitos

-   Docker instalado na sua máquina.

### 1. Construa a Imagem Docker

No terminal, na raiz do projeto, execute o seguinte comando para construir a imagem. Recomendamos usar uma nova tag de versão, como `2.0`.

```bash
docker build -t desafio-container:2.0 .
```

Se você estiver publicando no Docker Hub, use seu nome de usuário:
```bash
docker build -t seu-usuario/desafio-container:2.0 .
```

### 2. Execute o Contêiner

Após a construção da imagem, execute o seguinte comando para iniciar o contêiner:

```bash
docker run -p 5000:5000 -p 2222:22 --name desafio-container-v2 -d --privileged desafio-container:2.0
```

-   `--privileged`: **IMPORTANTE!** Este modo é necessário para que muitos dos desafios de nível Pleno e Sênior (como manipulação de partições, LVM, e networking avançado) funcionem corretamente.
-   `-p 5000:5000`: Mapeia a porta 5000 do contêiner (aplicação web) para a porta 5000 da sua máquina.
-   `-p 2222:22`: Mapeia a porta 22 do contêiner (SSH) para a porta 2222 da sua máquina.
-   `--name desafio-container-v2`: Dá um novo nome ao contêiner para não conflitar com versões anteriores.
-   `-d`: Executa o contêiner em modo "detached".

### 3. Acesse os Desafios

1.  **Interface Web**: Abra o seu navegador e acesse `http://localhost:5000` para ver a lista de desafios.

2.  **Acesso SSH**: Use o seguinte comando para acessar o contêiner:
    ```bash
    ssh challengeuser@localhost -p 2222
    ```
    A senha é `password`. O usuário `challengeuser` tem permissões de `sudo` sem senha para facilitar a execução dos comandos.

### 4. Parando e Removendo o Contêiner

Para parar o contêiner:
```bash
docker stop desafio-container-v2
```

Para remover o contêiner:
```bash
docker rm desafio-container-v2
```