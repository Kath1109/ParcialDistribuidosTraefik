# Segundo Parcial - Sistemas Distribuidos

- Andrea Katherine Bello Sotelo
- Cristian Andrés Basto Largo

--- 

## Etapa 1

- Primero se configura los hosts en /etc/hosts así:

<img width="826" height="604" alt="ConfiguraciónHost" src="https://github.com/user-attachments/assets/f23262be-827d-404d-99a3-b252ecc9cfab" />

- Se define el docker-compose.yml para los dominios y subdominios de los pokemones Charizard, Bulbasur y Pikachu.

<img width="733" height="599" alt="image" src="https://github.com/user-attachments/assets/23bf92ea-26ba-4730-92dd-56b83586e220" />

networks:
  poke_net:
    driver: bridge


- Diagrama:

<img width="1024" height="508" alt="image" src="https://github.com/user-attachments/assets/63d23f7c-b790-4df0-8235-27f1fb38445b" />

---

## Etapa 2

Se cambia el docker-compose.yml.

Se verifica:

<img width="1704" height="828" alt="image" src="https://github.com/user-attachments/assets/82756262-a6b4-4a63-a252-e4c352986b13" />

Se ejecuta docker compose logs traefik:

<img width="1784" height="891" alt="image" src="https://github.com/user-attachments/assets/d0956810-774b-49d7-a78a-4c199eeb82ec" />

---

## Etapa 3

- Analogía:
BasicAuth en Neo4j = Aduana en el aeropuerto
Así como en el aeropuerto los pasajeros deben mostrar pasaporte o identificación antes de entrar a la zona internacional, Neo4j pide credenciales de usuario/contraseña antes de permitir el acceso.

RateLimit en la API = Control de seguridad
Igual que en seguridad se controla el flujo de pasajeros (no entran todos a la vez para evitar congestión), el rateLimit limita cuántas solicitudes entran por segundo para proteger la API de abusos.

