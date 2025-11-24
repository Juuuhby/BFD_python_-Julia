def enviar_email(email):
    print(f"--- Email '{email}' foi enviado ---")
    return True

def sms(funcao_principal):
    def wrapper_sms(*args,**kwargs):
        resultado = funcao_principal(*args,**kwargs)
        print(f"--- O SMS foi enviado ---")
        return resultado
    return wrapper_sms

def whatsapp(funcao_principal):
    def wrapper_whats(*args,**kwargs):
        resultado = funcao_principal(*args,**kwargs)
        print("--- A mensagem foi enviado no Whatsapp---")
        return resultado
    return wrapper_whats

enviar_email("Fatura")
print("-"*20)

@sms
def sms(email):
    enviar_email(email)

@whatsapp
def whatsapp(email):
    enviar_email(email)

sms("Fatura do Inter")
print("-"*20)
whatsapp("Fatura da Nubank")
print("-"*20)
