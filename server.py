
import socket
from aes_utils import encrypt_message, decrypt_message, generate_key_from_password # 
HOST = '0.0.0.0' 
PORT = 65432   
SENHA_COMPARTILHADA = "minhasenhasupersecreta12345678" 

CHAVE_AES = generate_key_from_password(SENHA_COMPARTILHADA)

def iniciar_servidor():

    while True:
        print(f"Aguardando nova conexão em {HOST}:{PORT}...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            try:
                s.bind((HOST, PORT))
                s.listen()
            except OSError as e:
                print(f"Erro ao iniciar o servidor (bind/listen): {e}")
                print("Verifique se a porta já está em uso ou se há problemas de permissão.")
                break 

            try:
                conn, addr = s.accept()
            except Exception as e_accept:
                print(f"Erro ao aceitar conexão: {e_accept}")
                continue

            with conn:
                print(f"Conectado por {addr}")
                try:
                    while True:
                        data_encrypted_b64 = conn.recv(2048) 
                        if not data_encrypted_b64:
                            print(f"Cliente {addr} desconectado.")
                            break 
                        
                        try:
                            mensagem_recebida_bytes = decrypt_message(CHAVE_AES, data_encrypted_b64)
                            print(f"Cliente ({addr[0]}:{addr[1]}): {mensagem_recebida_bytes.decode('utf-8')}")
                        except Exception as e_decrypt:
                            print(f"Erro ao descriptografar mensagem do cliente ({addr[0]}:{addr[1]}): {e_decrypt}")

                            continue 

                        mensagem_servidor = input("Servidor: ") 
                        if mensagem_servidor.lower() == 'sair':
                            print("Encerrando conexão com este cliente a pedido do servidor.")
                            if CHAVE_AES:
                                try:
                                    mensagem_saida_criptografada = encrypt_message(CHAVE_AES, "Servidor encerrando.")
                                    conn.sendall(mensagem_saida_criptografada)
                                except Exception as e_send_exit_server:
                                    print(f"Erro ao enviar mensagem de saída do servidor: {e_send_exit_server}")
                            break 
                        try:
                            mensagem_servidor_encrypted_b64 = encrypt_message(CHAVE_AES, mensagem_servidor)
                            conn.sendall(mensagem_servidor_encrypted_b64)
                        except Exception as e_encrypt_send:
                            print(f"Erro ao criptografar ou enviar mensagem do servidor: {e_encrypt_send}")
                            continue

                except ConnectionResetError:
                    print(f"Conexão perdida com o cliente {addr}.")
                except ConnectionAbortedError:
                    print(f"Conexão com o cliente {addr} foi abortada.")
                except BrokenPipeError:
                    print(f"Conexão com o cliente {addr} quebrada (Broken Pipe).")
                except Exception as e_comm_loop:
                    print(f"Erro inesperado na comunicação com {addr}: {e_comm_loop}")
                finally:
                    print(f"Conexão com o cliente {addr} fechada.")

if __name__ == "__main__":
    try:
        iniciar_servidor()
    except KeyboardInterrupt:
        print("\nServidor encerrado pelo usuário (Ctrl+C).")
    except Exception as e_main:
        print(f"Erro fatal no servidor: {e_main}")