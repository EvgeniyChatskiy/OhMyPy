import os
import paramiko


def ssh_checkout(host, user, passwd, cmd, text, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname=host, username=user, password=passwd, port=port)
    stdin, stdout, stderr = client.exec_command(cmd)
    exit_code = stdout.channel.recv_exit_status()
    out = (stdout.read() + stderr.read()).decode("utf-8")
    client.close()
    if text in out and exit_code == 0:
        return True
    else:
        return False


def ssh_negative_checkout(host, user, passwd, cmd, text, port=22):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname=host, username=user, password=passwd, port=port)
    stdin, stdout, stderr = client.exec_command(cmd)
    exit_code = stdout.channel.recv_exit_status()
    out = (stdout.read() + stderr.read()).decode("utf-8")
    client.close()
    if text in out and exit_code != 0:
        return True
    else:
        return False


def upload_files(host, user, passwd, local_path, remote_path, port=22):
    print(f'File loading {local_path} to {remote_path}')
    transport = paramiko.Transport((host, port))
    transport.connect(None, username=user, password=passwd)
    sftp = paramiko.SFTPClient.from_transport(transport)

    # Change the directory permission before uploading the file
    try:
        sftp.chdir(os.path.dirname(remote_path))
        sftp.chmod(os.path.dirname(remote_path), 0o755)
    except Exception as e:
        print(f'Error changing directory permission: {e}')

    try:
        sftp.put(local_path, remote_path)
    except Exception as e:
        print(f'Error uploading file: {e}')
        return False

    if sftp:
        sftp.close()
    if transport:
        transport.close()
    return True
