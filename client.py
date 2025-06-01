
import socket
from aes_utils import encrypt_message, decrypt_message, generate_key_from_password # 

HOST_SERVIDOR = '127.0.0.1'  
PORTA_SERVIDOR = 65432  
SENHA_COMPARTILHADA = "minhasenhasupersecreta12345678" 

CHAVE_AES = generate_key_from_password(SENHA_COMPARTILHADA)


def iniciar_cliente():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST_SERVIDOR, PORTA_SERVIDOR))
            print(f"Conectado ao servidor em {HOST_SERVIDOR}:{PORTA_SERVIDOR}")
        except ConnectionRefusedError:
            print(f"Não foi possível conectar ao servidor em {HOST_SERVIDOR}:{PORTA_SERVIDOR}. Verifique se o servidor está rodando.")
            return
        except Exception as e:
            print(f"Erro ao conectar: {e}")
            return

        try:
            while True:
                mensagem_cliente = input("Cliente: ") 
                if mensagem_cliente.lower() == 'sair':
                    print("Encerrando conexão a pedido do cliente.")
                    if CHAVE_AES: 
                        try:
                            mensagem_saida_criptografada = encrypt_message(CHAVE_AES, "Cliente encerrando.")
                            s.sendall(mensagem_saida_criptografada)
                        except Exception as e_send_exit:
                            print(f"Erro ao enviar mensagem de saída: {e_send_exit}")
                    break
                
                try:
                    mensagem_cliente_encrypted_b64 = encrypt_message(CHAVE_AES, mensagem_cliente)
                    s.sendall(mensagem_cliente_encrypted_b64)
                except Exception as e_encrypt_send:
                    print(f"Erro ao criptografar ou enviar mensagem: {e_encrypt_send}")
                    continue 

                data_encrypted_b64 = s.recv(2048) 
                if not data_encrypted_b64:
                    print("Servidor desconectado.")
                    break
                
                try:
                    resposta_servidor_bytes = decrypt_message(CHAVE_AES, data_encrypted_b64)
                    print(f"Servidor: {resposta_servidor_bytes.decode('utf-8')}")
                except Exception as e_decrypt:
                    print(f"Erro ao descriptografar mensagem do servidor: {e_decrypt}")
                    continue 

        except ConnectionResetError:
            print("Conexão perdida com o servidor.")
        except ConnectionAbortedError:
            print("Conexão abortada.")
        except BrokenPipeError:
            print("Conexão quebrada (Broken Pipe). O servidor pode ter fechado inesperadamente.")
        except Exception as e:
            print(f"Erro inesperado no cliente: {e}")
        finally:
            print("Conexão com o servidor fechada.")


if __name__ == "__main__":
    iniciar_cliente()