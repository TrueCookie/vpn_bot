#!/bin/bash

keys_index_file=/etc/openvpn/server/easy-rsa/pki/index.txt
fileline="$(grep "/CN=$1" $keys_index_file | tail -n 1)"
columns_number="$(echo $fileline | awk -F' ' '{print NF;}')"

if [[ $columns_number -eq 5 ]] && [[ $fileline == V* ]]; then

	serial="$(echo $fileline | awk -F' ' '{print $3;}')"
    # echo "Client is active. Serial:" 
	echo $serial
	
    exit 0;

elif [[ $columns_number -eq 6 ]] && [[ $fileline == R* ]]; then

	serial="$(echo $fileline | awk -F' ' '{print $4;}')"
    # echo "Client is revoked. Serial:"
	echo $serial
    
	exit 0;

else

    echo "Error; key index file may be corrupted."
    exit 1;
fi
