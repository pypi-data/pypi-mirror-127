import typer
from pathlib import Path
from typing import List, Union
from datetime import datetime
import webbrowser

import sys

import importlib_metadata as lib_metadata
from typing import Optional
import subprocess

from ausdex.seifa_vic.seifa_vic import Metric
from ausdex import calc_inflation

app = typer.Typer()


def version_callback(value: bool):
    if value:
        version = lib_metadata.version("ausdex")
        typer.echo(version)
        raise typer.Exit()


@app.command()
def repo():
    """
    Opens the repository in a web browser.
    """
    typer.launch("https://github.com/rbturnbull/ausdex")


@app.command()
def docs(live: bool = True):
    """Builds the documentation.

    Args:
        live (bool, optional): Whether or not to use sphinx-autobuild to automatically build the documentation as files are edited. Defaults to True.
    """
    root_dir = Path(__file__).parent.parent.resolve()
    docs_dir = root_dir / "docs"
    docs_build_dir = docs_dir / "_build/html"

    if live:
        command = f"sphinx-autobuild {docs_dir} {docs_build_dir} --open-browser"
    else:
        command = f"sphinx-build -b html {docs_dir} {docs_build_dir}"

    subprocess.run(command, shell=True)

    if not live:
        index_page = docs_build_dir / "index.html"
        print(f"Open the index page at {index_page}")
        webbrowser.open_new("file://" + str(index_page))


@app.command()
def inflation(
    value: float,
    original_date: str,
    evaluation_date: str = None,
):
    """Adjusts Australian dollars for inflation.

    Prints output to stdout.

    Args:
        value (float): The dollar value to be converted.
        original_date (str): The date that the value is in relation to.
        evaluation_date (str, optional): The date to adjust the value to. Defaults to the current date.
    """

    result = calc_inflation(
        value=value, original_date=original_date, evaluation_date=evaluation_date
    )
    typer.echo(f"{result:.2f}")


@app.command()
def seifa_vic(year_value: str, suburb: str, metric: Metric, fill_value: str = "null"):
    """
    Interpolates suburb aggregated socioeconomic indices for a given year for a given suburb.

    inputs
    year_value (int, float): Year values in decimal years or in a datetime format convertable by pandas.to_datetime function\n
        suburb (str): The name of the suburb that you want the data interpolated for\n
                metric (str): the name of the seifa_score variable, options are include\n
                `irsd_score` for index of relative socio economic disadvantage,\n
                `ieo_score` for the index of education and opportunity,\n
                `ier_score` for an index of economic resources, `irsad_score` for index of socio economic advantage and disadvantage,\n
                `uirsa_score` for the urban index of relative socio economic advantage,\n
                `rirsa_score` for the rural index of relative socio economic advantage\n
                fill_value (str): can be "extrapolate" to extraplate past the extent of the dataset or "boundary_value" to use the closest datapoint, or \n
                or an excepted response for scipy.interpolate.interp1D fill_value keyword argument\n
    outputs
        interpolated score (float)

    """
    import warnings

    warnings.filterwarnings("ignore")

    from .seifa_vic import interpolate_vic_suburb_seifa

    result = interpolate_vic_suburb_seifa(
        year_value, suburb.upper(), metric.value, fill_value=fill_value
    )
    typer.echo(f"{result:.2f}")


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, "--version", "-v", callback=version_callback, is_eager=True
    ),
):
    """Adjusts Australian dollars for inflation or returns interpolated socio-economic indices for Victorian suburbs."""
    pass
