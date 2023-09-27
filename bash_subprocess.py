import subprocess

def main() -> None:
    list_files = subprocess.run(["sudo", "bash", "/root/openvpn-install.sh"])
    list_files = subprocess.run(["ls"])

if __name__ == "__main__":
    main()

