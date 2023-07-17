import datetime

from categories import Categories

class Message(NamedTuple):
    amount: int
    category_name: str


class Expense(NamedTuple):
    id: Optional[int]
    amount: int
    category_name: str

def add_expense(row_message:str) -> Expense:
    parsed_message = _parse_message(raw_message)
    category = Categories().get_categpry(
        parsed_message.category_text)
    inserted_row_id = db.insert("expense", {
        "amount": parsed_message.amount,
        "created": _get_now_formatted(),
        "category_codename": category.codename,
        "raw_text": raw_message
    })
    return Expense(id=None,
                   amount=parsed_message.amount,
                   category_name=category.name)