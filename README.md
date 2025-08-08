# Desafios de Linha de Comando em um Contêiner Docker

Este projeto cria um ambiente de contêiner Docker com uma série de desafios de linha de comando. O objetivo é que o usuário interaja com o contêiner através de uma interface web e de uma sessão SSH para resolver os desafios propostos.

## Como Usar

### Pré-requisitos

- Docker instalado na sua máquina.

### 1. Construa a Imagem Docker

No terminal, na raiz do projeto, execute o seguinte comando para construir a imagem:

```bash
docker build -t desafio-container .
```

### 2. Execute o Contêiner

Após a construção da imagem, execute o seguinte comando para iniciar o contêiner:

```bash
docker run -p 5000:5000 -p 2222:22 --name desafio-container -d desafio-container
```

- `-p 5000:5000`: Mapeia a porta 5000 do contêiner (onde a aplicação web está rodando) para a porta 5000 da sua máquina.
- `-p 2222:22`: Mapeia a porta 22 do contêiner (SSH) para a porta 2222 da sua máquina. Isso evita conflitos com um possível serviço SSH rodando na sua máquina.
- `--name desafio-container`: Dá um nome ao contêiner para facilitar o gerenciamento.
- `-d`: Executa o contêiner em modo "detached" (em segundo plano).

### 3. Acesse os Desafios

1.  **Interface Web**: Abra o seu navegador e acesse `http://localhost:5000` para ver a lista de desafios.

2.  **Acesso SSH**: O primeiro desafio requer acesso SSH. Use o seguinte comando:
    ```bash
    ssh challengeuser@localhost -p 2222
    ```
    A senha é `password`.

### 4. Resolva os Desafios

Siga as instruções na interface web para completar os desafios dentro da sessão SSH.

### 5. Parando e Removendo o Contêiner

Para parar o contêiner, execute:
```bash
docker stop desafio-container
```

Para remover o contêiner após pará-lo:
```bash
docker rm desafio-container
```