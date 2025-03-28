# Automação de Envio de Convites no LinkedIn

Este projeto é uma automação desenvolvida em Python para enviar convites de conexão no LinkedIn para pessoas com base em um cargo especificado. A automação utiliza o Selenium WebDriver para controlar o navegador Chrome, realizar pesquisas de cargos e enviar convites de forma automática.

## Funcionalidades

- **Pesquisa de Cargos:** O script permite que você insira um cargo e realiza uma busca no LinkedIn para encontrar perfis relacionados.
- **Envio de Convites:** A automação envia convites de conexão para os perfis encontrados, sem incluir uma mensagem de convite personalizada.
- **Navegação entre Páginas:** Caso não haja mais botões de "Conectar" na página atual, o script navega para a próxima página de resultados.
- **Controle de Limite de Convites:** O número de convites a serem enviados pode ser especificado, garantindo que o script não envie mais convites do que o desejado.
  
## Tecnologias Utilizadas

- **Python:** A principal linguagem utilizada para a automação.
- **Selenium WebDriver:** Biblioteca usada para controlar o navegador e interagir com os elementos da página.
- **WebDriver Manager:** Gerencia o driver do Chrome automaticamente.
- **Random e Sleep:** Usados para adicionar um tempo de espera entre ações, imitando um comportamento humano.

## Requisitos

Antes de rodar o projeto, você precisa garantir que tenha os seguintes pacotes instalados:

1. **Python 3.x**
2. **Bibliotecas necessárias:**
   - `selenium`
   - `webdriver_manager`
   
Você pode instalar as dependências executando o seguinte comando:

```bash
pip install selenium webdriver_manager
```
## Como Usar

### 1. Inicializando o Script
Primeiro, execute o script principal, que irá solicitar que você insira o número de convites e o cargo desejado para pesquisa:

```bash
python main.py
```

### Passos do Script
O script realizará os seguintes passos:

Iniciar o navegador e acessar o LinkedIn.

Aguardar 60 segundos para você fazer login na sua conta do LinkedIn.

Pesquisar pelo cargo especificado.

Enviar convites de conexão para os perfis encontrados.

Navegar entre as páginas de resultados, caso necessário, até atingir o limite de convites.

### Exemplo de Entrada
O script solicitará as seguintes entradas do usuário:

```bash
quantos convites deseja enviar?: 10
qual o cargo quer pesquisar?: Desenvolvedor Python
```

### Observações
- O script irá enviar convites para as pessoas que aparecerem nos resultados de pesquisa.

- Os convites serão enviados sem mensagem.

- Certifique-se de estar logado na sua conta do LinkedIn dentro do prazo de 60 segundos, caso contrário, o script não poderá enviar os convites.

- O script realiza ações automaticamente e pode demorar alguns minutos, dependendo do número de convites e resultados.

### Futuras Melhorias
- Adicionar a opção de enviar convites com uma mensagem personalizada.

- Implementar a opção de enviar convites somente para perfis de uma localização específica.

- Melhorar o controle de tempo entre ações para simular um comportamento mais realista.

- Implementar logs para acompanhar a execução do script e falhas.

- Implementar uma interface gráfica que irá mostrar o feedback das ações atuais

### Aviso Legal
Este projeto é uma automação criada para fins educacionais. Use com responsabilidade e esteja ciente das políticas do LinkedIn sobre automações. O uso excessivo ou inadequado pode resultar em restrições à sua conta.

