from settings.state import BookingState

def confirm(state: BookingState):
    if not state.get("confirmed"):
        state["response"] = f"Confirm booking in {state['location']} on {state['date']}? (yes/no)"
    return state