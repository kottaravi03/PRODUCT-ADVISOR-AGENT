from langgraph.graph import (
    START,
    END,
    StateGraph
)
from langgraph.prebuilt import tools_condition

from state import AdvisorState

from nodes import (
    assistant,
    get_tool_node,
    capture_customer_info,
    all_tools
)


def create_graph():
    """
    Create and compile the Product Advisor Agent graph.
    """

    state_graph = StateGraph(AdvisorState)

    # Nodes
    state_graph.add_node("assistant", assistant)
    state_graph.add_node("tools", get_tool_node())

    # Edges
    state_graph.add_edge(START, "assistant")

    state_graph.add_conditional_edges(
        "assistant",
        tools_condition
    )

    state_graph.add_edge("tools", "assistant")

    # Compile the graph
    return state_graph.compile()


# Export the compiled graph for LangGraph CLI
graph = create_graph()