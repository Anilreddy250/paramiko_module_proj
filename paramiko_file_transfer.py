import paramiko
def transfer_files(hostname, username, password):
    client = paramiko.SSHclient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, username, password)
        sftp = client.open_sftp()
        sftp.put('Local_cofig.txt', '/tmp/config.txt')

        print("Upload successfull!")

        sftp.get('/var/log/messages','downloaded_syslog.log')
        print("Download  successfull")

        sftp.close()
    finally:
        client.close()
