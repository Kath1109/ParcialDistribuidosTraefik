# Segundo Parcial - Sistemas Distribuidos

- Andrea Katherine Bello Sotelo
- Cristian Andrés Basto Largo

--- 

## Etapa 1

- Primero se configura los hosts en /etc/hosts así:

<img width="826" height="604" alt="ConfiguraciónHost" src="https://github.com/user-attachments/assets/f23262be-827d-404d-99a3-b252ecc9cfab" />

- Se define el docker-compose.yml para los dominios y subdominios de los pokemones Charizard, Bulbasur y Pikachu:

services:
  traefik:
    image: traefik:v2.10
    container_name: traefik_proxy
    command:
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--entrypoints.web.address=:80"
    ports:
      - "80:80"
      - "8080:8080"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    networks:
      - poke_net
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.pikachu.rule=Host(`pikachu.localhost`)"
      - "traefik.http.routers.charizard.rule=Host(`charizard.localhost`)"
      - "traefik.http.routers.mewtwo.rule=Host(`bulbasur.localhost`)"

networks:
  poke_net:
    driver: bridge


- Diagrama:

<img width="1024" height="508" alt="image" src="https://github.com/user-attachments/assets/63d23f7c-b790-4df0-8235-27f1fb38445b" />

---

## Etapa 2

