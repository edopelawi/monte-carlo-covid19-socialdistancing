# Monte Carlo Simulation of Social Distancing to Prevent Coronavirus Infection, CMU DASE S20

This repository holds the Jupyter Notebook files to do Monte Carlo Simulation on the effectiveness of Social Distancing to prevent COVID-19 infection during the outbreak. The result of the notebook is utilized for CMU's [Decision Analysis and Engineering Economics for Software Engineers class](https://courses.ece.cmu.edu/18657SV), Spring 2020.

## Setup

### Jupyter Notebook

There are plenty of ways to setup Jupyter Notebook locally. Here's one of them, assuming you already have Python 3.x installed:

1. Setup virtualenv folder to prevent the installation meddles with the libraries in main machine, e.g `python3 -m venv <path_to_virtualenv>`
2. Activate the virtualenv, e.g. `source <path_to_virtualenv>/bin/activate`
3. Upgrade pip version, `pip3 install --upgrade pip`
4. Install the dependencies, `pip3 install -r requirements.txt`
5. Run Jupyter Notebook locally, `jupyter notebook --port=8888`
	- This command will allow us to open Jupyter in browser through `localhost:8888`.
6. After stopping the notebook, deacticate the virtualenv, `deactivate`


### Google Colab

Since running the whole simulation might take a long time, we would suggest you to try running this [Google Colab](https://colab.research.google.com). You could create multiple Jupyter Notebooks in the Colab and run them with different parameters to allow simultaneous run.

## How to use

This project mainly divided into two parts, simulation and analysis. Both of them are doable through the main notebook of this project, [monte-carlo-sim.ipynb](monte-carlo-sim.ipynb).

### Simulation

A single simulation runs the whole model using parameters that represents the population and infection. However, we differentiate the percentage of stationary population (those who self-isolate / practicing social distancing) from 0% up to 100%. The complete simulation runs each percentage 10.000 times and then gather the whole data into a single Dataframe. This is available on the first half of the main notebook.

Since the whole simulation takes a long time, we stored our latest run in Pickle format. We have two folders that stores these, [picklefiles](picklefiles) that stores the simulation result with default parameters, and [picklefiles_duration10](picklefiles_duration10) that stores the simulation with prolonged infection duration.

### Analysis 

The analysis part takes the second half of the project, where you can either use the data from your in-memory result from recent simulation or use the saved Pickle files to build your Dataframes. You might want to do the latter if you utilize Google Colab to parallelize your simulation run, too.

In general, the analysis part utilizes the Dataframe to gather the data along with generating some plots. You can either see the plots through the notebook's display result or check the stored images inside the [images](images) folder, which will be generated each time the plot-generating code is run.

## Authors

- Ricardo Suranta (rsuranta@andrew.cmu.edu)
- Gaurav Shegokar (gshegoka@andrew.cmu.edu)

## License

Copyright 2020 Ricardo Suranta, Gaurav Shegokar

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
