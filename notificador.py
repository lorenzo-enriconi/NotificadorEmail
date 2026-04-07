from twilio.rest import Client
import imaplib
import os

# Dotenv
# ============

def load_env(path='.env'):
    if not os.path.exists(path):
        return
    
    with open(path) as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            os. environ[key] = value
            
# ============

# ----- // -----

load_env() #Dotenv

# ----- // -----

# Configurando email
# =========================================

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
EMAIL_SERVER = "imap.gmail.com"
TARGET_SENDER = os.getenv('TARGET_SENDER')

# =========================================

# ----- // -----

#Configurando Whats (Twilio)
# =========================================

TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_TOKEN = os.getenv('TWILIO_TOKEN')
TWILIO_ZAP_NUMBER = os.getenv('TWILIO_ZAP_NUMBER')
MEU_ZAP = os.getenv('MEU_ZAP')

# =========================================

# ----- // -----

# Conexão no Twilio e enviar mensagem
# =========================================

def enviar_whatsapp(mensagem):
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    mensagem = client.messages.create(
        from_=TWILIO_ZAP_NUMBER,
        body=mensagem,
        to=MEU_ZAP
    )
    print(f"Notificação enviada! ID {mensagem.sid}")

# =========================================

# ----- // -----

# Acesso de email, busca do remetente e lança notificação
# =========================================

def verf_email():
    try:
        print("Conexão ao servidor...")
        mail = imaplib.IMAP4_SSL(EMAIL_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")
        
        criterio_busca = f'(UNSEEN_FROM "{TARGET_SENDER}")'
        status, mensagens = mail.search(None, criterio_busca)
        
        if status == "OK":
            lista_ids = mensagens[0].split()
            
            if lista_ids:
                qtd = len(lista_ids)
                texto = f"Notificação TechDrop.\n\n Chegou {qtd} emails de {TARGET_SENDER}."
                
                enviar_whatsapp(texto)
                
            else:
                print(f"Nenhum email novo de {TARGET_SENDER} hoje.")
                
        mail.logout()
    
    except Exception as erro:
        print(f"Ocorreu um erro na execução: {erro}.")

# =========================================

# ----- // -----

if __name__ == "__main__":
    verf_email()

