import paramiko

def connect_with_key(hostname, username, Keypath):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try :
        client.connect(hostname=hostname, username=username, key_filename=key_path)
        _, stdout, _ = client.exec_command('uptime')
        print(f"Device Uptime:{stdout.rad().decode("utf-8")}")

    except Exception as e :
        print(f"key authentication failed: {e}")
    finally:
        client.close()
