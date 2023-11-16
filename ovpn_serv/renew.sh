#!/bin/bash

./mv_crt.sh `./serial_by_CN.sh $1` $1

cd /etc/openvpn/server/easy-rsa/
./easyrsa renew $1

echo "Client certificate renewed successfully."