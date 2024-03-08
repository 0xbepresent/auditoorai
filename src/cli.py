import os

import click
from dotenv import load_dotenv
from .utils.style import rconsole

# Load environment variables from .env
load_dotenv(".env")


class Environment:

    def __init__(self):
        self.verbose = False
        self.config = {}

    def log(self, msg, *args, **kwargs):
        """Logs a message to stderr."""
        if kwargs:
            if kwargs.get('pager') == True:
                with rconsole.pager():
                    rconsole.print(msg)
        else:
            rconsole.print(msg, style='bold magenta')

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log("DEBUG: {}".format(msg), *args)


pass_environment = click.make_pass_decorator(Environment, ensure=True)


class AuditooorCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"src.commands.cmd_{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


@click.command(cls=AuditooorCLI)
@pass_environment
def cli(ctx):
    """
    Audit code using AI
    """