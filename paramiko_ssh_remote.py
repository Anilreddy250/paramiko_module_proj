import pexpect

# 1. Spawn the connection (Serial or SSH)
child = pexpect.spawn('ssh root@192.168.1.100')
child.expect('password:')
child.sendline('admin123')

# 2. Wait for the shell prompt
child.expect('# ')
child.sendline('firmware_tool --status')

# 3. Parse output using regex or string matching
idx = child.expect(['ERROR_CODE_0xEA', '# '])
if idx == 0:
    print("Target failed with specific firmware error.")
