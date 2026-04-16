from settings.state import BookingState

def book(state: BookingState):
    if state["confirmed"]:
        state["response"] = f"✅ Booking confirmed in {state['location']} on {state['date']}"
    return state