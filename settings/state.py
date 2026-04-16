from typing import TypedDict, Optional

class BookingState(TypedDict):
    user_input: str
    intent: Optional[str]
    date: Optional[str]
    location: Optional[str]
    confirmed: Optional[bool]
    response: Optional[str]