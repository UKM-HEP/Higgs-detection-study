import itertools

# You can use LHE files from scikit-hep-testdata
#from skhep_testdata import data_path

import pylhe
#lhe_file = data_path("pylhe-testlhef3.lhe")

lhe_file = "/home/shoh/Works/DM-detection-study/production-study/MG5_aMC_v2_9_15/dh_zprime_jj/Events/run_01/unweighted_events.lhe.gz"
events = pylhe.read_lhe_with_attributes(lhe_file)
print(f"Number of events: {pylhe.read_num_events(lhe_file)}")

# Get event 1
event = next(itertools.islice(events, 1, 2))

# A DOT language graph of the event can be inspected as follows
print(event.graph.source)

# The graph is nicely displayed as SVG in Jupyter notebooks
event

# To save a DOT graph render the graph to a supported image format
# (refer to the Graphviz documentation for more)
event.graph.render(filename="test", format="png", cleanup=True)
event.graph.render(filename="test", format="pdf", cleanup=True)
