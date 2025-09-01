import click
from cryptography.fernet import Fernet
import base64

@click.group()
def cli():
    """ksec: A tool to encrypt secrets for Kubernetes YAML files."""
    pass

@cli.command()
@click.option('--value', prompt='Secret value', hide_input=True, confirmation_prompt=False, help='The secret value to encrypt.')
@click.option('--key', prompt='Encryption key (base64-encoded)', hide_input=True, help='The base64-encoded symmetric key (generate one with ksec generate-key).')
@click.option('--output-format', default='plain', type=click.Choice(['plain', 'base64', 'yaml-snippet']), help='Output format: plain (encrypted token), base64 (extra base64 wrap), or yaml-snippet (ready for YAML).')
def encrypt(value, key, output_format):
    """Encrypt a secret value."""
    try:
        fernet = Fernet(key)
        encrypted = fernet.encrypt(value.encode())
        
        if output_format == 'base64':
            output = base64.b64encode(encrypted).decode()
        elif output_format == 'yaml-snippet':
            output = f"encryptedSecret: {encrypted.decode()}"
        else:
            output = encrypted.decode()
        
        click.echo(output)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)

@cli.command()
def generate_key():
    """Generate a new encryption key."""
    key = Fernet.generate_key()
    click.echo(key.decode())

if __name__ == '__main__':
    cli()
