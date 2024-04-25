"""Bosco runs benchmarks to assess the performance of Python functions."""

import plotly.graph_objs as go
import typer
from plotly.subplots import make_subplots
from rich.console import Console
from tabulate import tabulate

from bosco import benchmark, generate

cli = typer.Typer()
console = Console()


@cli.command()
def bosco(
    starting_size: int = typer.Option(100),
    number_doubles: int = typer.Option(5),
    file: str = typer.Option("./bosco/sorting.py"),
    function_name: str = typer.Option("bubble_sort"),
) -> None:
    """Conduct a doubling experiment to measure the performance of list sorting for a specific algorithm."""
    console.print(
        "\n:dog: Bosco is fetching our results!\n"
    )
    console.print(f"Path to the desired file: {file}\n")
    console.print(f"Name of the desired function: {function_name}\n")
    console.print(f"Starting size of the data container: {starting_size}\n")
    console.print(f"Number of doubles to execute: {number_doubles}\n")
    console.print("📈 Here are the results from running the experiment!\n")

    all_results = []

    for i in range(number_doubles):
        size = starting_size * (2**i)
        data_to_sort = generate.generate_random_container(size)
        performance_data = benchmark.run_sorting_algorithm(
            file, function_name, data_to_sort
        )

        (
            best_time,
            worst_time,
            average_time,
        ) = performance_data  # best, worst, and average times

        all_results.append([best_time, worst_time, average_time])

    header = ["Input Size", "Best Case", "Worst Case", "Average Case"]
    data = [
        [starting_size * 2**i, *results]
        for i, results in enumerate(all_results)
    ]

    table = tabulate(
        data, headers=header, tablefmt="fancy_grid", floatfmt=".5f"
    )
    console.print(table)

    # plot
    fig = make_subplots(rows=1, cols=1)

    x_values = [starting_size * (2**i) for i in range(number_doubles)]
    best_case = [results[0] for results in all_results]
    worst_case = [results[1] for results in all_results]
    average_case = [results[2] for results in all_results]

    trace_best = go.Scatter(
        x=x_values,
        y=best_case,
        mode="lines+markers",
        name="Best Case",
    )
    trace_worst = go.Scatter(
        x=x_values,
        y=worst_case,
        mode="lines+markers",
        name="Worst Case",
    )
    trace_average = go.Scatter(
        x=x_values,
        y=average_case,
        mode="lines+markers",
        name="Average Case",
    )

    fig.add_trace(trace_best)
    fig.add_trace(trace_worst)
    fig.add_trace(trace_average)

    fig.update_layout(
        title=f"Evaluating the Performance of {function_name}",
        xaxis_title="Input Size",
        yaxis_title="Execution Time (s)",
        showlegend=True,
        margin=dict(l=20, r=20, t=60, b=20),
        title_x=0.5,
    )

    fig.show()
