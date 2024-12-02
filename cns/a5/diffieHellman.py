# Legitimate Diffie-Hellman Key Exchange
def diffie_hellman_key_exchange(p, g, client, server):
    print("\n### Legitimate Key Exchange ###")
    
    a = 15  # private key for client
    # Server's private key
    b = 13  # private key for server

    A = pow(g, a, p)  # Client's public key
    B = pow(g, b, p)  # Server's public key

    shared_secret_client = pow(B, a, p)
    shared_secret_server = pow(A, b, p)

    print(f"{client}'s Public Key (A): {A}")
    print(f"{server}'s Public Key (B): {B}")
    print(f"{client}'s Shared Secret: {shared_secret_client}")
    print(f"{server}'s Shared Secret: {shared_secret_server}")

    return shared_secret_client, shared_secret_server

def diffie_hellman_mitm_attack(p, g, client, server, attacker):
    print("\n### Man-in-the-Middle Attack ###")
    
    # Client's and Server's private keys
    a = 15
    b = 13
    
    # Attacker's private keys
    e1 = 7  # For client
    e2 = 11  # For server

    # Legitimate public keys (g^a mod p, g^b mod p)
    A = pow(g, a, p)  # Client's public key
    B = pow(g, b, p)  # Server's public key

    E1 = pow(g, e1, p)  # Attacker's public key to client
    E2 = pow(g, e2, p)  # Attacker's public key to server

    shared_secret_client = pow(E1, a, p)
    shared_secret_server = pow(E2, b, p)
    
    shared_secret_attacker_client = pow(A, e1, p)
    shared_secret_attacker_server = pow(B, e2, p)

    print(f"{client}'s Public Key (A): {A}")
    print(f"{server}'s Public Key (B): {B}")
    print(f"{attacker}'s Public Key to {client} (E1): {E1}")
    print(f"{attacker}'s Public Key to {server} (E2): {E2}")
    
    print(f"{client}'s Shared Secret (with {attacker}): {shared_secret_client}")
    print(f"{server}'s Shared Secret (with {attacker}): {shared_secret_server}")
    print(f"{attacker}'s Shared Secret with {client}: {shared_secret_attacker_client}")
    print(f"{attacker}'s Shared Secret with {server}: {shared_secret_attacker_server}")

p = 23
g = 5

client_name = input("Enter the name for the Client (e.g., Alice): ")
server_name = input("Enter the name for the Server (e.g., Bob): ")
attacker_name = input("Enter the name for the Attacker (e.g., Eve): ")

diffie_hellman_key_exchange(p, g, client_name, server_name)

diffie_hellman_mitm_attack(p, g, client_name, server_name, attacker_name)
