from settings.state import BookingState
from settings.config import model

def understand(state: BookingState):
    prompt = f"""
    Extract booking intent, date, and location from:
    "{state['user_input']}"
    Return JSON.
    """
    res = model.generate_content(prompt)
    state["intent"] = "booking"
    state["date"] = "tomorrow"
    state["location"] = "Dhaka"
    return state
