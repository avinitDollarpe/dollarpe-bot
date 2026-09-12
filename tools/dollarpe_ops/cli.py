from __future__ import annotations

import json

import click

from . import client


@click.group()
def main() -> None:
    """DollarPe Bot ops helpers (sample fleet data)."""


@main.command("list-services")
def list_services() -> None:
    click.echo(json.dumps(client.list_services(), indent=2))


@main.command("get-service")
@click.argument("name")
def get_service(name: str) -> None:
    click.echo(json.dumps(client.get_service(name), indent=2))


@main.command("list-incidents")
def list_incidents() -> None:
    click.echo(json.dumps(client.list_incidents(), indent=2))


@main.command("health")
def health() -> None:
    click.echo(json.dumps(client.health_summary(), indent=2))


@main.command("playbook")
def playbook() -> None:
    click.echo(json.dumps(client.oncall_playbook(), indent=2))


if __name__ == "__main__":
    main()
