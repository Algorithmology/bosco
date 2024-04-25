# How to Use the Bosco Tool

To run the Bosco tool, you can call it from the main directory using a poetry command formatted like
`poetry run bosco --starting-size 100 --number-doubles 5 --file bosco/sorting.py --function-name bubble_sort`.
The command should use the inputs `--starting-size` for the initial list size to start the doubling experiment,
`--number-doubles` for the number of times the input size will be doubled during the doubling experiment,
`--file` for the path to the file containing the sorting algorithm you want to run the doubling experiment on,
and `--function-name` for the name of the function containing the sorting algorithm you want to test.

## Example of command and output

### Command

```terminal
poetry run bosco --starting-size 100 --number-doubles 5 --file bosco/sorting.py --function-name quick_sort
```

### Output

```terminal
🐶 Bosco is fetching our results!

Path to the desired file: bosco/sorting.py

Name of the desired function: quick_sort

Starting size of the data container: 100

Number of doubles to execute: 5

📈 Here are the results from running the experiment!

╒══════════════╤═════════════╤══════════════╤════════════════╕
│   Input Size │   Best Case │   Worst Case │   Average Case │
╞══════════════╪═════════════╪══════════════╪════════════════╡
│          100 │     0.00058 │      0.00061 │        0.00060 │
├──────────────┼─────────────┼──────────────┼────────────────┤
│          200 │     0.00129 │      0.00155 │        0.00139 │
├──────────────┼─────────────┼──────────────┼────────────────┤
│          400 │     0.00268 │      0.00374 │        0.00305 │
├──────────────┼─────────────┼──────────────┼────────────────┤
│          800 │     0.00578 │      0.00656 │        0.00610 │
├──────────────┼─────────────┼──────────────┼────────────────┤
│         1600 │     0.01312 │      0.01414 │        0.01372 │
╘══════════════╧═════════════╧══════════════╧════════════════╛
```

### Graph Produced from Output

![example_graph](https://github.com/Algorithmology/bosco/assets/70417208/0be0e695-f06c-490a-98df-cb3eaaf5ca07)

