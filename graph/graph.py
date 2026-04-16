from langgraph.graph import StateGraph
from settings.state import BookingState
from node import understand, book, confrom

graph = StateGraph(BookingState)

graph.add_node("understand",understand)
graph.add_node("confrom",confrom)
graph.add_node("book",book)

graph.set_entry_point("understand")
graph.add_edge("understand", "confirm")
graph.add_edge("confirm", "book")

booking_agent = graph.compile()


# Save the graph

booking_agent.get_graph().draw_mermaid_png(output_file_path="graph.png")
