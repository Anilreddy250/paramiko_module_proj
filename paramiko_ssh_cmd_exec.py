import paramiko
def check_kernel_version(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_kt_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password =password, timeout=5)
        stdin, stdout, stderr = client.exec_command('uname -a')

        output = stdout.read().decode('utf-8')
        errors = stderr.read().decode('utf-8')

        if errors:
            print(f"Error encountered:{errors}")
        else:
            print(f"Kernel version: \n{output.strip()}")
    except Exception as e:
        print(f"Connection failed:{e}")
    finally:
        client.close()

        
