import pandas as pd
from fpdf import FPDF

# Read the CSV file
data = pd.read_csv("data.csv")

# Analyze the data
average_marks = data["Marks"].mean()
max_marks = data["Marks"].max()
min_marks = data["Marks"].min()

# Create PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", 'B', 14)
pdf.cell(200, 10, txt="Student Marks Report", ln=True, align='C')

pdf.set_font("Arial", size=12)
pdf.ln(10)

# Add table header
pdf.cell(100, 10, txt="Name", border=1)
pdf.cell(40, 10, txt="Marks", border=1)
pdf.ln()

# Add table rows
for index, row in data.iterrows():
    pdf.cell(100, 10, txt=row["Name"], border=1)
    pdf.cell(40, 10, txt=str(row["Marks"]), border=1)
    pdf.ln()

# Summary
pdf.ln(10)
pdf.cell(200, 10, txt=f"Average Marks: {average_marks:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Highest Marks: {max_marks}", ln=True)
pdf.cell(200, 10, txt=f"Lowest Marks: {min_marks}", ln=True)

# Save PDF
pdf.output("sample_report.pdf")

print("✅ Report generated as sample_report.pdf")
