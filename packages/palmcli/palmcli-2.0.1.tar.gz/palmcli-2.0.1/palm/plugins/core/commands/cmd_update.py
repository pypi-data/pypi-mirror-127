import subprocess
import shlex
import click


@click.command("update")
@click.option("--local", is_flag=True, help="attempts to install from cwd")
def cli(local: bool):
    """This updates the current version of palm. meta huh?"""

    if not click.confirm(
        f"\nAttempt to update Palm {'from cwd' if local else 'from github'}?"
    ):
        click.secho("Cancelled", fg="red")
        return

    uninstall_cmd = "python3 -m pip uninstall -y palm"
    source = " . " if local else " git+https://github.com/palmetto/palm-cli.git "
    upgrade_cmd = f"python3 -m pip install {source}"

    for cmd in (
        uninstall_cmd,
        upgrade_cmd,
    ):
        subprocess.run(shlex.split(cmd), check=True)

    click.secho("Success! Palm has been updated.", fg="green")
