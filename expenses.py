"""Расходы, удаления"""
import datetime
import re
from categories import Categories
import db
import exceptions

class Message(NamedTuple):
    amount: int
    category_name: str


class Expense(NamedTuple):
    id: Optional[int]
    amount: int
    category_name: str

def add_expense(row_message:str) -> Expense:
    parsed_message = _parse_message(raw_message)
    category = Categories().get_category(
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

def _parse_message(raw_message: str) -> Message:
    """Парсит вновь введённый текст"""
    regexp_result = re.match(r"([\d]+)(.*)", raw_message)
    if not regexp_result or not regexp_result.group(0) or not regexp_result.group(1) or not regexp_result.group(2):
        raise exceptions.NotCorrectMessage("Не могу понять сообщение. Напишите в формате:\n2500 метро")
    amount = regexp_result.group(1).replace(" ", "")
    category_text = regexp_result.group(2).strip().lower()
    return Message(amount=amount, category_text=category_text)