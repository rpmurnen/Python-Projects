import os
import time
import win32com.client as win32
from PIL import ImageGrab

# === Paths ===
excel_path = os.path.expanduser(r"~\MD2\Finance - General\00 Financials\2025\04-2025\04-25 CLINIC FINANCIALS2.xlsm")
image_output_folder = os.path.expanduser(r"~\MD2\Finance - General\00 Financials\2025\04-2025\Clinics\Clinic_ScreenShots")
os.makedirs(image_output_folder, exist_ok=True)

# === Excel setup ===
excel = win32.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open(excel_path)

# === Read clinic list from Control!B6:B34 ===
clinic_range = wb.Sheets("Control").Range("B6:B34")
clinic_names = [cell.Value for cell in clinic_range if cell.Value]

print(f"📋 Found {len(clinic_names)} clinics")

# === Helper: capture range to image ===
def capture_range(sheet_name, cell_range, img_path):
    ws = wb.Sheets(sheet_name)
    ws.Activate()
    ws.Range(cell_range).Select()
    excel.ActiveWindow.ScrollRow = 1
    excel.ActiveWindow.Zoom = 100
    time.sleep(0.2)

    try_formats = [win32.constants.xlPicture, win32.constants.xlBitmap]

    for fmt in try_formats:
        print(f"📋 Trying format {fmt} for {sheet_name}!{cell_range}")
        ImageGrab.grabclipboard()  # Clear
        ws.Range(cell_range).CopyPicture(Format=fmt)
        time.sleep(0.5)  # Let Excel populate clipboard

        for attempt in range(20):  # Try for 4s
            img = ImageGrab.grabclipboard()
            if img:
                img.save(img_path)
                print(f"✅ Saved: {img_path}")
                return
            print(f"⏳ Attempt {attempt+1}/20 — clipboard still empty")
            time.sleep(0.2)

        if os.path.exists(img_path):
            print(f"✅ (Late save detected): {img_path}")
            return
        else:
            print(f"❌ Clipboard failed after 20 attempts (format {fmt}) — skipping {sheet_name}")


# === Loop through clinics ===
for clinic in clinic_names:
    print(f"\n🏥 Processing: {clinic}")

    # Set dropdowns
    wb.Sheets("PL").Range("D3").Value = clinic
    wb.Sheets("BS").Range("E3").Value = clinic

    time.sleep(0.5)  # Let Excel update any formulas

    # Capture PL and BS tables
    pl_img = os.path.join(image_output_folder, f"{clinic}_PL.png")
    bs_img = os.path.join(image_output_folder, f"{clinic}_BS.png")

    capture_range("PL", "D3:U83", pl_img)
    capture_range("BS", "E3:K23", bs_img)

# === Cleanup ===
wb.Close(False)
excel.Quit()
del wb
del excel

print("\n🎉 All clinic images saved.")
