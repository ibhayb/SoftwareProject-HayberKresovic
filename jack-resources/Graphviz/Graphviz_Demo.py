"""Requirements:
pip install graphviz
pip install Pillow

You also have to install the Graphviz application itself. Please follow the steps here:
https://graphviz.org/download/

If you are using Windows, you may have to add the path to the Graphviz binary to your PATH environment variable if it is not set automatically.
"""

from io import BytesIO
import base64


def test_graphviz():
    """Checks whether Graphviz is correctly configured on the system.
    This function does not produce any output."""
    dot: graphviz.Digraph = graphviz.Digraph()
    dot.attr("graph", center="True", dpi="300",
             label="Test", labelloc="t")
    dot.format = "png"
    # Get image as binary
    tree_binary = dot.pipe()
    # Encode binary image as Base64
    b64_image = base64.b64encode(tree_binary).decode("utf-8")
    # Do not display image. Just check whether there were any exceptions.


try:
    import graphviz
    try:
        test_graphviz()
    except:
        print("The Graphviz program was not properly installed. Please visit:")
        print("https://graphviz.org/download/")
except:
    print("Graphviz package is not installed. Please run:")
    print("pip install graphviz")

try:
    from PIL import Image
except:
    print("Pillow package is not installed. Please run:")
    print("pip install Pillow")


def create_single_graph_example():
    # Create graph. Here is the documentation with way more configuration options: https://graphviz.readthedocs.io/en/stable/manual.html
    # Digraph = Directional graph
    dot: graphviz.Digraph = graphviz.Digraph()
    dot.attr("graph", center="True", dpi="300",
             label="Sample Graph", labelloc="t")
    dot.format = "png"

    # Add nodes to graph
    # You can either create it using dot.node(node_label) or dot.node(node_id, node_label).
    # If you just provide label, then automatically id == label.
    # Or you can set id explicity. Useful if you have multiple nodes with same label,
    # then you can just give them different ids and the edges will connect the correct nodes.
    dot.node("node_a", "A")
    dot.node("node_b", "B")
    dot.node("node_c", "C")

    # Add edges to graph
    # e.g. from id "node_a" to id "node_b" with label "5".
    dot.edge("node_a", "node_b", label="5")
    dot.edge("node_c", "node_a", label="10")
    dot.edge("node_b", "node_c", label="1")

    # Get image as binary
    graph_binary = dot.pipe()
    # Encode binary image as Base64
    b64_image = base64.b64encode(graph_binary).decode("utf-8")
    img = Image.open(BytesIO(base64.b64decode(b64_image)))
    img.show()


def create_subgraphs_example():
    # Alternatively, create one image with multiple graphs
    # IMPORTANT: The name of the subgraphs seems to have to be "cluster_1", "cluster_2", etc.
    dot: graphviz.Digraph = graphviz.Digraph()
    dot.attr("graph", center="True", dpi="300",
             label="Multiple Graphs", labelloc="t")
    dot.format = "png"

    with dot.subgraph(name="cluster_1") as sub:
        sub.attr(label="Subgraph with border", labelloc="b")
        sub.node("A", shape="ellipse")
        sub.node("B", shape="octagon", color="red", fontcolor="blue")
        sub.node("C")

        sub.edge("A", "B", color="red", style="dotted")
        sub.edge("C", "B")

    with dot.subgraph(name="cluster_2") as sub:
        sub.attr(label="Subgraph without border",
                 labelloc="b", color="transparent")
        sub.node("1")
        sub.node("2")
        sub.node("3")

        sub.edge("1", "2", "10")

    graph_binary = dot.pipe()
    b64_image = base64.b64encode(graph_binary).decode("utf-8")
    img = Image.open(BytesIO(base64.b64decode(b64_image)))
    img.show()


create_single_graph_example()
create_subgraphs_example()
