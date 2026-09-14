"""
AuditDrop - Backend API Service
Built for AI Immersion Assignment (BE.CSE 2nd Year)
Framework: FastAPI + Uvicorn
"""

import os
import random
from datetime import datetime, timedelta
from typing import Dict, Any

from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AuditDrop API",
    description="AI-powered document drop & audit extraction portal for CA firms",
    version="1.0.0"
)

# Enable CORS for cross-origin frontend integrations if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def simulate_ai_vision_analysis(client_name: str, filename: str, file_size_bytes: int) -> Dict[str, Any]:
    """
    Simulates Google Gemini / AI Vision API extraction on an uploaded bill, receipt, or Excel ledger.
    Extracts Vendor Name, Invoice Date, Total Amount, Tax Category, Line Items, and Audit Verification details.
    """
    name_lower = filename.lower()
    
    # File size formatting
    if file_size_bytes < 1024:
        size_str = f"{file_size_bytes} B"
    elif file_size_bytes < 1024 * 1024:
        size_str = f"{round(file_size_bytes / 1024, 1)} KB"
    else:
        size_str = f"{round(file_size_bytes / (1024 * 1024), 2)} MB"

    # Base dates
    today = datetime.now()
    inv_date = (today - timedelta(days=random.randint(1, 15))).strftime("%Y-%m-%d")
    due_date = (today + timedelta(days=random.randint(5, 20))).strftime("%Y-%m-%d")

    # Smart mock extraction based on file extension & filename patterns
    if any(ext in name_lower for ext in ['.xlsx', '.xls', '.csv']):
        category = "Ledger Audit & Payroll Sheet"
        vendor = "Multiple Vendors (Ledger Aggregation)"
        inv_no = f"LEDGER-{random.randint(1000, 9999)}"
        subtotal = 125000.00
        tax_rate_str = "18%"
        cgst = 11250.00
        sgst = 11250.00
        total_amount = 147500.00
        confidence = 0.992
        line_items = [
            {"item": "Monthly Vendor Payouts Batch A", "qty": 1, "unit_price": 75000.00, "total": 75000.00},
            {"item": "Subcontractor Services - Tax Deducted at Source (TDS)", "qty": 1, "unit_price": 35000.00, "total": 35000.00},
            {"item": "Office Rent & Utilities Month-End", "qty": 1, "unit_price": 15000.00, "total": 15000.00}
        ]
        audit_note = "High Integrity Ledger. 100% mathematical reconciliation verified across 48 entries."

    elif any(kw in name_lower for kw in ['fuel', 'petrol', 'diesel', 'travel', 'cab']):
        category = "Travel & Conveyance"
        vendor = "Bharat Petroleum / Shell India"
        inv_no = f"BPCL-{random.randint(10000, 99999)}"
        subtotal = 2500.00
        tax_rate_str = "12%"
        cgst = 150.00
        sgst = 150.00
        total_amount = 2800.00
        confidence = 0.978
        line_items = [
            {"item": "Speed Diesel / Fuel Refill - Fleet Vehicle KA-01-MJ-8821", "qty": 35, "unit_price": 80.00, "total": 2800.00}
        ]
        audit_note = "Valid Tax Fuel Receipt. Eligible for Business Expense Tax Deduction."

    elif any(kw in name_lower for kw in ['stationery', 'office', 'paper', 'supplies']):
        category = "Office Supplies & Consumables"
        vendor = "Lotus Office Essentials Pvt Ltd"
        inv_no = f"INV-{random.randint(2000, 7000)}"
        subtotal = 8500.00
        tax_rate_str = "18%"
        cgst = 765.00
        sgst = 765.00
        total_amount = 10030.00
        confidence = 0.986
        line_items = [
            {"item": "A4 Copier Paper Boxes (5 Reams)", "qty": 5, "unit_price": 900.00, "total": 4500.00},
            {"item": "Ergonomic Desk Accessories & Filing Trays", "qty": 4, "unit_price": 1000.00, "total": 4000.00}
        ]
        audit_note = "Standard Business Purchase. Vendor GSTIN active & matched."

    elif any(kw in name_lower for kw in ['software', 'cloud', 'aws', 'saas', 'hosting']):
        category = "IT Software & Cloud Hosting"
        vendor = "AWS Cloud India / Google Cloud"
        inv_no = f"AWS-IN-{random.randint(100000, 999999)}"
        subtotal = 18000.00
        tax_rate_str = "18%"
        cgst = 1620.00
        sgst = 1620.00
        total_amount = 21240.00
        confidence = 0.995
        line_items = [
            {"item": "Production Compute Instances (EC2 / Compute Engine)", "qty": 1, "unit_price": 12000.00, "total": 12000.00},
            {"item": "Managed Database Storage & Backup Snapshots", "qty": 1, "unit_price": 6000.00, "total": 6000.00}
        ]
        audit_note = "Verified SaaS Invoice with valid Reverse Charge / GST details."

    else:
        # Default generic invoice scenario
        category = "Professional & General Expenses"
        vendor = "Apex Enterprise Logistics Pvt Ltd"
        inv_no = f"INV-2026-{random.randint(100, 999)}"
        subtotal = 14500.00
        tax_rate_str = "18%"
        cgst = 1305.00
        sgst = 1305.00
        total_amount = 17110.00
        confidence = 0.984
        line_items = [
            {"item": "Monthly Freight & Courier Services", "qty": 1, "unit_price": 9500.00, "total": 9500.00},
            {"item": "Warehouse Handling & Packaging Charges", "qty": 1, "unit_price": 5000.00, "total": 5000.00}
        ]
        audit_note = "Valid Commercial Tax Invoice. Zero discrepancies found."

    gstin_mock = f"29AAACA{random.randint(1000, 9999)}A1Z{random.randint(1, 9)}"

    return {
        "status": "success",
        "processed_at": datetime.now().isoformat(),
        "client_info": {
            "client_name": client_name,
            "uploaded_filename": filename,
            "file_size": size_str,
        },
        "ai_extraction": {
            "vendor_name": vendor,
            "invoice_number": inv_no,
            "vendor_gstin": gstin_mock,
            "invoice_date": inv_date,
            "due_date": due_date,
            "category": category,
            "currency": "INR (₹)",
            "tax_details": {
                "subtotal": subtotal,
                "gst_rate": tax_rate_str,
                "cgst": cgst,
                "sgst": sgst,
                "igst": 0.00,
                "total_tax": cgst + sgst
            },
            "total_amount": total_amount,
            "payment_status": "Pending Tax Audit Approval",
            "confidence_score": confidence,
            "line_items": line_items,
            "audit_flags": {
                "is_gstin_valid": True,
                "duplicate_detected": False,
                "math_reconciled": True,
                "audit_note": audit_note
            }
        }
    }


@app.get("/", response_class=HTMLResponse)
async def serve_index():
    """Serves the single page frontend UI."""
    index_path = os.path.join(os.path.dirname(__file__), "index.html")
    if not os.path.exists(index_path):
        raise HTTPException(status_code=404, detail="index.html file not found.")
    
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)


@app.post("/upload")
async def upload_document(
    client_name: str = Form(..., description="Name of the client firm or business"),
    file: UploadFile = File(..., description="Uploaded bill, receipt, or Excel ledger")
):
    """
    Endpoint accepting client document upload and performing simulated AI Vision parsing.
    Returns structured extraction data in JSON format.
    """
    if not client_name or not client_name.strip():
        raise HTTPException(status_code=400, detail="Client Name is required.")
    
    if not file or not file.filename:
        raise HTTPException(status_code=400, detail="No valid file uploaded.")

    # Read bytes to verify content length & file presence
    file_bytes = await file.read()
    file_size = len(file_bytes)

    if file_size == 0:
        raise HTTPException(status_code=400, detail="Uploaded file is empty (0 bytes).")

    # Simulate AI vision / OCR processing
    result = simulate_ai_vision_analysis(
        client_name=client_name.strip(),
        filename=file.filename,
        file_size_bytes=file_size
    )

    return JSONResponse(content=result)
