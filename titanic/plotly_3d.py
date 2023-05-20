from pathlib import Path
import xlwings as xw
import plotly.express as px
import plotly
import pandas as pd


# pip install plotly-express plotly pandas

def plot_scatter_3d():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    df = sheet.range("A1").expand().options(pd.DataFrame, index=False).value

    fig = px.scatter_3d(df, x='PassengerId', y='Sex', z='Age',
                        color='Age', title="Task Overview")

    file_path = str(Path(__file__).parent / "scatter_3d.html")
    plotly.offline.plot(fig, filename=file_path, auto_open=False)
