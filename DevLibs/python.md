### click

```python
import click

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()
```

### logger

```python
from loguru import logger

#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple loguru
#https://github.com/Delgan/loguru
if __name__ == '__main__':
    logger.info("this is info log test")
```

### paramiko

```python
from paramiko_test import interactive
import paramiko


#add log file
paramiko.util.log_to_file('./test')
#connect with ssh
ssh=paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.65', port=22, username='sdn', password='rocks', compress=True)
#make shell
channel=ssh.invoke_shell()
#create channel
interactive.interactive_shell(channel)
#close channel
channel.close()
ssh.close()
```

