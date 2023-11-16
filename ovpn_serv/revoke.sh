#!/bin/bash

keys_index_file=/etc/openvpn/server/easy-rsa/pki/index.txt
fileline="$(grep "/CN=$1" $keys_index_file | tail -n 1)"
columns_number="$(echo $fileline | awk -F' ' '{print NF;}')"

if [[ $columns_number -eq 5 ]] && [[ $fileline == V* ]]; then

    # source /etc/openvpn/server/easy-rsa/pki/vars
    cd /etc/openvpn/server/easy-rsa/
	./easyrsa revoke $1

    {
        sleep 3
        echo kill $1
        sleep 3
        echo exit
    } | telnet localhost 7505

	./easyrsa gen-crl
	systemctl restart openvpn-server@server.service 
	#ДОБАВИТЬ: Отложенный рестарт сервиса. По подтверждению через админку

    echo "Client certificate revoked successfully."
    exit 0;

elif [[ $columns_number -eq 6 ]] && [[ $fileline == R* ]]; then

    echo "Client certificate is already revoked."
    exit 0;

else

    echo "Error; key index file may be corrupted."
    exit 1;
fi