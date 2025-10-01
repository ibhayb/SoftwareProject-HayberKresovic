import graphviz
from PIL import Image
from io import BytesIO

dot: graphviz.Digraph = graphviz.Digraph()
dot.attr("graph", center="True", dpi="300", label="Sample Graph", labelloc = "t")
dot.fomar = "png"

dot.node("node_a", "A")
dot.node("node_b", "B")
dot.edge("node_a", "node_b", label="5")

# PNG-Bytes direkt aus Graphviz
graph_binary = dot.pipe(format="png")

# Direkt in PIL laden und anzeigen
img = Image.open(BytesIO(graph_binary))
img.show()  # Öffnet Vorschau/Preview auf macOS
