Demo script for mesh network
Shows programmatic usage without GUI
"""
Demo script for mesh network
Shows programmatic usage without GUI
"""
import time
import logging
from mesh_node import MeshNode
from mesh_protocol import MessageType

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def demo_basic_network():
    """Demo: Basic 3-node network with authentication and messaging"""
    print("\n" + "="*60)
    print("DEMO: Basic Mesh Network with Authentication")
    print("="*60 + "\n")

print("Creating nodes...")
    node_a = MeshNode("NodeA", network_key, port=5001)
    node_b = MeshNode("NodeB", network_key, port=5002)
    node_c = MeshNode("NodeC", network_key, port=5003)

    # Start nodes
    node_a.start()
    node_b.start()
    node_c.start()

