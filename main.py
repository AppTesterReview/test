
def get_incomes(sum_str: str) -> int | None:
  """Приводим сумму строкой к числу"""
  sum_str.replace(" ", "")

  if sum_str.isdigit():
    return int(sum_str)
