import os
import time
from datetime import datetime
import calendar
from docx import Document
from docx.shared import Pt
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

try:
    import xlwings as xw
except ImportError:
    raise ImportError("The 'xlwings' module is required. Please install it using: pip install xlwings")

wb = None  # Predefine workbook variable so it always exists

# === CONFIGURATION ===

EXCEL_PATH = os.path.expanduser(r"~\MD2\Finance - General\00 Financials\2025\04-2025\04-25 CLINIC FINANCIALS2.xlsm")
WORD_TEMPLATE_PATH = os.path.expanduser(r"~\MD2\Finance - General\00 Financials\ME_Reporting_Python_Scripting\memo_template.docx")
DEST_FOLDER_BASE = os.path.expanduser(r"~\MD2\Finance - General\00 Financials\2025\04-2025\Clinics\MEMO COVER PAGE")
TODAY_FOLDER = datetime.today().strftime("%Y-%m-%d")
DEST_FOLDER = os.path.join(DEST_FOLDER_BASE, TODAY_FOLDER)
os.makedirs(DEST_FOLDER, exist_ok=True)

CONTROL_SHEET = "Control"
AR_SHEET = "AR_Patient_Report"
CLINIC_LIST_RANGE = "B6:B34"
DROPDOWN_CELL = "B2"
TABLE1_RANGE = "C11:G15"
TABLE2_RANGE = "C18:G28"

PLACEHOLDER_1 = "<<INSERT EXCEL SECTION 1 HERE>>"
PLACEHOLDER_2 = "<<INSERT EXCEL SECTION 2 HERE>>"

def get_doctor_names_xlwings(xlwb, clinic_name):
    md_list_sheet = xlwb.sheets["MD_List"]
    data = md_list_sheet.range("A2:D100").value  # adjust size as needed

    for row in data:
        if row[0] and str(row[0]).strip().lower() == clinic_name.strip().lower():
            doc1 = str(row[2]).strip() if row[2] else ""
            doc2 = str(row[3]).strip() if row[3] else ""
            return [doc for doc in (doc1, doc2) if doc]

    return []

def get_previous_month_year(month_offset=1):
    today = datetime.today()
    month = today.month - month_offset
    year = today.year
    if month <= 0:
        month += 12
        year -= 1
    month_name = calendar.month_name[month]
    return month_name, year

def set_font(run):
    run.font.name = 'Aptos Narrow'
    run.font.size = Pt(11)
    run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Aptos Narrow')

# ... [imports and config remain unchanged above this point]

def insert_table_at_placeholder(doc, placeholder, table_data):
    print(f"\n🔍 Looking for placeholder: {placeholder}")
    found = False

    for i, para in enumerate(doc.paragraphs):
        text = para.text.strip()
        print(f"👀 Paragraph {i}: '{text}'")

        if placeholder in text:
            print(f"✅ Found placeholder in paragraph {i}")
            para.text = para.text.replace(placeholder, "")
            found = True

            # Cleanup logic for Table 1
            if placeholder == PLACEHOLDER_1:
                if len(table_data) > 1:
                    second_row = table_data[1]
                    if isinstance(second_row[1], str) and "Primary" in second_row[1]:
                        print("🚹 Removing duplicate header row (row 2) from Table 1")
                        table_data = [table_data[0]] + table_data[2:]

            table = doc.add_table(rows=0, cols=len(table_data[0]))
            table.style = 'Table Grid'

            for row_idx, row_data in enumerate(table_data):
                row_cells = table.add_row().cells
                if row_idx == 0 and placeholder == PLACEHOLDER_1:
                    print("🔧 Merging and centering header row (cols 1–4) for Table 1")
                    
                    # Merge columns 1 to 4
                    merged_cell = row_cells[1]
                    for col in range(2, 5):
                        merged_cell = merged_cell.merge(row_cells[col])
                    
                    # Center and style the merged cell
                    merged_paragraph = merged_cell.paragraphs[0]
                    merged_paragraph.alignment = 1  # Center
                    merged_paragraph.clear()
                    run = merged_paragraph.add_run(str(table_data[0][1]) if table_data[0][1] else "")
                    set_font(run)
                    run.bold = True

                for col_idx, cell_val in enumerate(row_data):
                    if row_idx == 0 and placeholder == PLACEHOLDER_1 and col_idx >= 1:
                        continue  # Skip all merged cells: 1, 2, 3, 4


                    cell = row_cells[col_idx]
                    # Format values
                    if isinstance(cell_val, (int, float)):
                        text = f"{cell_val:,.0f}"
                        is_numeric = True
                    elif isinstance(cell_val, datetime):
                        text = cell_val.strftime("%#m/%#d/%y")
                        is_numeric = False
                    elif cell_val is None:
                        text = ""
                        is_numeric = False
                    else:
                        text = str(cell_val)
                        is_numeric = False

                    paragraph = cell.paragraphs[0]
                    run = paragraph.add_run(text)
                    set_font(run)
                    if is_numeric:
                        paragraph.alignment = 2

                    if row_idx == 0 or row_idx == len(table_data) - 1:
                        run.bold = True

            tbl_element = table._tbl
            para_element = para._element
            para_element.addnext(tbl_element)

            print(f"✅ Table inserted directly after paragraph {i} for: {placeholder}")
            return

    if not found:
        print(f"⚠️ Placeholder not found: {placeholder}")

print("🔄 Launching Excel...")
app = xw.App(visible=False)
app.display_alerts = False
app.screen_updating = False

try:
    print("📂 Opening workbook...")
    wb = app.books.open(EXCEL_PATH)
    control_ws = wb.sheets[CONTROL_SHEET]
    ar_ws = wb.sheets[AR_SHEET]

    print("📋 Fetching clinic list...")
    raw_clinics = control_ws.range(CLINIC_LIST_RANGE).value
    clinic_list = [name for name in raw_clinics if name]

    print(f"✅ Found {len(clinic_list)} clinics.")

    for clinic in clinic_list:
        print(f"\n🩺 Processing clinic: {clinic}")
        ar_ws.range(DROPDOWN_CELL).value = clinic
        time.sleep(0.25)
        _ = ar_ws.range("C11").value
        ar_ws.api.Calculate()

        table1 = ar_ws.range(TABLE1_RANGE).value
        table2 = ar_ws.range(TABLE2_RANGE).value

        print(f"📋 Clinic: {clinic}")
        for row in table1:
            print(row)

        doc = Document(WORD_TEMPLATE_PATH)

        doctor_names = get_doctor_names_xlwings(wb, clinic)
        greeting_line = "Hello " + " and ".join(doctor_names) + "," if doctor_names else "Hello,"
        to_line = "To: " + " and ".join(doctor_names) if doctor_names else "To: [Doctor Name]"
        from_line = "From: Russ Murnen"
        month_name, year = get_previous_month_year()
        date_line = datetime.today().strftime("%B %d, %Y")
        re_line = f"Re: {month_name} Financial Performance"
        open_line = f"I’m pleased to share your financial results for {month_name} {year}."

        for text in [open_line, "", greeting_line, "", re_line, from_line, to_line, "", date_line]:
            para = doc.paragraphs[0].insert_paragraph_before("")
            run = para.add_run(text)
            set_font(run)

        insert_table_at_placeholder(doc, PLACEHOLDER_1, table1)
        insert_table_at_placeholder(doc, PLACEHOLDER_2, table2)

        filename = f"{clinic} review.docx"
        output_path = os.path.join(DEST_FOLDER, filename)
        doc.save(output_path)
        print(f"📏 Saved: {output_path}")

finally:
    print("\n🛑 Closing Excel...")
    if wb is not None:
        wb.close()
    app.quit()

print("\n✅ All memos generated.")
