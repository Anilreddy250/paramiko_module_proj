import paramiko
def run_chained_commands(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try :
        client.connect(hostname, username, password)
        commad = "cd /home/root/ && mkdir -p demo_dir && cd demo_dir && touch testfile.txt && ls -l"
        _, stdout, _ = client.exec_command(command)
        print(stdout.read().decode('utf-8'))

    finally:
        client.close()
