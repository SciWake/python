import xlwings as xw


def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[3]
    if sheet["A1"].value == "Hello xlwings!":
        sheet["A1"].value = "Bye xlwings!"
    else:
        sheet["A1"].value = "Hello xlwings!"


@xw.func
def hello(name):
    return f"Hello {name}!"


@xw.sub
def my_macro():
    """Writes the name of the Workbook into Range("A1") of Sheet 1"""
    wb = xw.Book.caller()
    wb.sheets[3].range('A10').value = 1231231


if __name__ == "__main__":
    xw.Book("titanic.xlsm").set_mock_caller()
    main()
