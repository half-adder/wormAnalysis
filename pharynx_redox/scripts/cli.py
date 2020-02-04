"""
Analyze an experiment, end-to-end, through the command line
"""

import logging
from pathlib import Path

import click

# import experiment


@click.group()
def pharedox():
    pass


@pharedox.command()
@click.argument(
    "experiment-directory",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, writable=True, readable=True
    ),
)
def analyze_stack(experiment_directory):
    """
    Run a new analysis on EXPERIMENT_DIRECTORY

    EXPERIMENT_DIRECTORY is the directory containing the image stack from MetaMorph. It
    should contain a single image stack, which is named the same as the directory.
    """
    experiment.Experiment(experiment_dir=Path(experiment_directory)).full_pipeline()


@click.command()
def hello():
    click.echo("hello world")


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
    # pharedox()
    hello()