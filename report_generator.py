from fpdf import FPDF

sales_data = {}

with open("sales_data.txt", "r") as file:
    for line in file:
        product, value = line.strip().split(",")
        sales_data[product] = int(value)

total_sales = sum(sales_data.values())
average_sales = total_sales / len(sales_data)
best_selling = max(sales_data, key=sales_data.get)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Sales Report", ln=True, align='C')

pdf.set_font("Arial", "", 12)
pdf.ln(10)
pdf.cell(0, 10, f"Total Sales: {total_sales}", ln=True)
pdf.cell(0, 10, f"Average Sales per Product: {average_sales:.2f}", ln=True)
pdf.cell(0, 10, f"Best Selling Product: {best_selling} ({sales_data[best_selling]} units)", ln=True)

pdf.ln(10)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Product-wise Sales Data:", ln=True)

pdf.set_font("Arial", "", 12)
for product, sales in sales_data.items():
    pdf.cell(0, 10, f"{product}: {sales} units", ln=True)

pdf.output("Task2_Sales_Report.pdf")
print("PDF report generated successfully!")
