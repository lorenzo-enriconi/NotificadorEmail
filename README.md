📧 Email-to-WhatsApp Notifier
Este é um script em Python que monitora sua caixa de entrada de e-mail (via IMAP) e envia uma notificação automática para o seu WhatsApp através da API do Twilio sempre que novos e-mails de um remetente específico são detectados.

🚀 Funcionalidades
Monitoramento Seletivo: Filtra e-mails não lidos de um remetente específico.

Integração WhatsApp: Utiliza a API do Twilio para enviar alertas em tempo real.

Segurança: Gerenciamento de credenciais via variáveis de ambiente (.env).

Simplicidade: Carregador de variáveis .env nativo (sem dependências externas extras para isso).

🛠️ Pré-requisitos
Antes de começar, você precisará de:

Python 3.x instalado.

Uma conta no Twilio com um número de WhatsApp configurado (Sandbox).

Uma conta de e-mail (Ex: Gmail) com acesso IMAP liberado.

Nota para Gmail: Você precisará gerar uma Senha de App para usar no script.

📦 Instalação
Clone o repositório:

Bash
git clone https://github.com/lorenzo-enriconi/NotificadorEmail.git
cd seu-repositorio

Instale a biblioteca do Twilio:

Bash
pip install twilio
⚙️ Configuração
Crie um arquivo chamado .env na raiz do projeto e preencha com suas informações:

Snippet de código
# Configurações de Email
EMAIL_USER=seu_email@gmail.com
EMAIL_PASS=sua_senha_de_app
TARGET_SENDER=remetente@exemplo.com

# Configurações Twilio
TWILIO_SID=seu_sid_aqui
TWILIO_TOKEN=seu_token_aqui
TWILIO_ZAP_NUMBER=whatsapp:+14155238886
MEU_ZAP=whatsapp:+5511999999999
🖥️ Como usar
Basta executar o script principal:

Bash
python seu_script.py
O script irá se conectar ao servidor do Gmail, buscar por mensagens não lidas do TARGET_SENDER e, se encontrar, enviará uma mensagem formatada para o seu WhatsApp.

📂 Estrutura do Código
load_env(): Função customizada para ler o arquivo .env e carregar as chaves no sistema.

enviar_whatsapp(): Gerencia a autenticação com o Twilio e o disparo da mensagem.

verf_email(): Realiza a conexão via SSL com o servidor IMAP e faz a lógica de busca.

🤝 Contribuições
Contribuições são sempre bem-vindas!

Faça um Fork do projeto.

Crie uma Branch para sua feature (git checkout -b feature/NovaFeature).

Dê um Commit nas suas alterações (git commit -m 'Adicionando nova feature').

Dê um Push na Branch (git push origin feature/NovaFeature).

Abra um Pull Request.
