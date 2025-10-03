import graphviz
from PIL import Image
from io import BytesIO

dot: graphviz.Digraph = graphviz.Digraph()
dot.attr("graph", center="True", dpi="300", label="Sample Graph", labelloc = "t")
dot.fomart = "png"

dot.node("node_a", "A\n(Start)", shape="circle", penwidth="4", fixedsize="true", width="0.75", height="0.75")
dot.node("node_b", "B\n(End)", shape="doublecircle", fixedsize="true", width="0.75", height="0.75")
dot.node("node_c", "C", shape="circle", fixedsize="true", width="0.75", height="0.75")
dot.node("node_d", "D\n(End)", shape="doublecircle", fixedsize="true", width="0.75", height="0.75")
dot.edge("node_a", "node_b", label="5")
dot.edge("node_a", "node_c", label="1", color="blue")
dot.edge("node_c", "node_d", label="2", color="blue")

# PNG-Bytes direkt aus Graphviz
graph_binary = dot.pipe(format="png")

# Direkt in PIL laden und anzeigen
img = Image.open(BytesIO(graph_binary))
img.show()  # Öffnet Vorschau/Preview auf macOS
img.save("example_graph.png")
