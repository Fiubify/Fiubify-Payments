# Fiubify-Payments

## Guía de instalación
Para ejecutar es necesario tener  Python 3 instalado:
<code>
sudo apt install python3
</code>
Para instalar dependencias:
<code>
sudo apt install python3-pip
sudo pip install -r requirements.txt
</code>
Para ejecutar el servidor:
<code>
uvicorn app.app:app --host=0.0.0.0 --port=${PORT}
</code>
