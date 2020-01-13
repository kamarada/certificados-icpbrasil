# Cria o banco de dados de certificados do Chrome/Chromium, caso nao exista
mkdir -p ~/.pki/nssdb
if [[ ! -f ~/.pki/nssdb/cert9.db ]]
then
    /usr/bin/instalar-icpbrasil
fi

