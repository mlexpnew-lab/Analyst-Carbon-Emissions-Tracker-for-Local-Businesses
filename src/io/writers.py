import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def to_csv(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)

def to_pdf_summary(df: pd.DataFrame, path: str):
    c = canvas.Canvas(path, pagesize=A4)
    total = df["total_co2e"].sum()
    c.drawString(72, 800, "Carbon Summary Report")
    c.drawString(72, 780, f"Total CO2e: {total:,.1f} kg")
    c.drawString(72, 760, f"Rows: {len(df)}")
    c.showPage()
    c.save()
