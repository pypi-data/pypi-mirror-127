"""Sub command to manage authentication.

  Run `electric auth --help` for usage.
"""

import click

from .. import interpolate
from .. import validators


@click.group(cls=click.Group)
@click.pass_obj
def auth(obj):
    """Sign up, log in and manage authentication status."""


@auth.command()
@click.pass_obj
def signup(obj):
    """Signup for an ElectricDB account.

          electric auth signup

      This will open a web page where you can enter your details.
    """

    raise NotImplementedError


@auth.command()
@click.option('--email', prompt='Email',
                         metavar='ADDRESS',
                         help='Your email address.')
@click.option('--expires-in', metavar='DURATION', default='2 weeks',
                              callback=validators.Duration(),
                              help='How long do you want to stay logged in for?',
                              show_default=True)
@click.pass_obj
@interpolate.docstring(validators.Duration.docs_url)
def login(obj, email, expires_in):
    """Login to your ElectricDB account.

          electric auth login

      This will open a web page where you can enter your email and password.

      Alternatively, you can provide `--email` and enter your password
      when prompted to login directly from the command line:

          electric auth login --email YOUR_EMAIL

      Durations are written in human friendly string format as documented here:
      {0}
    """

    if email:
        password = click.prompt('Password', hide_input=True)

        return login_with_password(email, expires_in, password)

    raise NotImplementedError


def login_with_password(email, expires_in, password):
    """Authenticate against the web service with the email and password.

      If successful, store the resulting access token in `~/.netrc`.
    """

    # msg = 'Forbidden. Have you logged in with the right credentials?'
    # click.secho(msg, fg='red')
    # raise click.Abort()
    raise NotImplementedError


@auth.command()
@click.pass_obj
def logout(obj):
    """Logout of your ElectricDB account."""

    raise NotImplementedError


@auth.command()
@click.pass_obj
def whoami(obj):
    """Display the current logged in user."""

    raise NotImplementedError

