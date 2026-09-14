# AuditDrop 📄⚡

> **AI-Powered Client Document Drop & Automated Tax Ledger Extraction Portal for Chartered Accountant (CA) Firms**

---

## 📌 Project Overview & Problem Statement

Chartered Accountant (CA) firms face a monthly bottleneck before tax due dates (such as GST filing windows, TDS submissions, and advance tax dates). Clients frequently submit bills, receipts, and Excel ledgers at the last minute in chaotic formats (scanned PDFs, smartphone photos, CSVs, and spreadsheets). 

Manual data entry leads to missing documents, calculation errors, delayed filings, and compliance penalties.

**AuditDrop** solves this document collection and pre-audit bottleneck by offering:
1. **Unified Client Drop Zone**: A simple, mobile-responsive portal where clients input their business name and drop monthly bills, receipts, or Excel ledgers.
2. **Automated AI Vision Extraction**: Simulates an advanced Google Gemini / AI Vision OCR engine that parses unstructured documents to extract key tax entities:
   - **Vendor Name** & **GSTIN**
   - **Invoice Date** & **Invoice Number**
   - **Total Amount** & **Tax Breakdowns** (CGST, SGST, IGST)
   - **Expense Category** (Travel, Office Supplies, IT Cloud, Ledger Audits)
   - **Line Items Breakdown** & **Math Integrity Reconciliation**
3. **Structured JSON Output & Audit Report**: Instantly produces structured JSON payloads ready for ERP/Tally integration alongside a user-friendly UI preview.

---

## 🎓 Academic Context

* **Course / Assignment**: AI Immersion Assignment
* **Level**: BE.CSE 2nd Year Student Project
* **Purpose**: Demonstrating web application integration with simulated AI Vision extraction pipelines for financial automation.

---

## 🛠️ Technology Stack

* **Backend**: Python 3.9+ with **FastAPI**
* **Frontend**: Single-Page HTML with **Tailwind CSS** (via CDN) & Vanilla JavaScript (Fetch API)
* **Server**: **Uvicorn** ASGI server

---

## 📁 File Structure

```text
AuditDrop/
├── requirements.txt   # Python project dependencies (FastAPI, Uvicorn, python-multipart)
├── main.py            # FastAPI backend server with / and /upload endpoints
├── index.html         # Responsive single-page frontend UI with Tailwind CSS
└── README.md          # Project documentation and setup guide
```

---

## 🚀 Quickstart & Setup Guide

Follow these exact terminal commands to set up and run the AuditDrop project locally on your machine.

### Step 1: Open Terminal & Navigate to Project Directory

```bash
cd /Users/rohith/Desktop/AuditDrop
```

### Step 2: (Optional but Recommended) Create & Activate Virtual Environment

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate
```

---

### Step 3: Install Required Dependencies

Install FastAPI, Uvicorn, and Python-Multipart via `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### Step 4: Run the Application Server

Start the Uvicorn ASGI server with live reloading enabled:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

---

### Step 5: Access the Web Portal

Open your browser and navigate to:

👉 **`http://127.0.0.1:8000`** (or `http://localhost:8000`)

---

## 🔌 API Endpoints Documentation

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Serves the `index.html` frontend web application |
| `POST` | `/upload` | Accepts `client_name` (Form field) and `file` (Multipart UploadFile). Returns AI extraction JSON |

### Sample `POST /upload` JSON Response

```json
{
  "status": "success",
  "processed_at": "2026-09-14T13:15:00.000000",
  "client_info": {
    "client_name": "Apex Enterprises Pvt Ltd",
    "uploaded_filename": "stationery_bill.pdf",
    "file_size": "1.2 MB"
  },
  "ai_extraction": {
    "vendor_name": "Lotus Office Essentials Pvt Ltd",
    "invoice_number": "INV-4821",
    "vendor_gstin": "29AAACA4921A1Z4",
    "invoice_date": "2026-09-10",
    "due_date": "2026-09-25",
    "category": "Office Supplies & Consumables",
    "currency": "INR (₹)",
    "tax_details": {
      "subtotal": 8500.0,
      "gst_rate": "18%",
      "cgst": 765.0,
      "sgst": 765.0,
      "igst": 0.0,
      "total_tax": 1530.0
    },
    "total_amount": 10030.0,
    "payment_status": "Pending Tax Audit Approval",
    "confidence_score": 0.986,
    "line_items": [
      {
        "item": "A4 Copier Paper Boxes (5 Reams)",
        "qty": 5,
        "unit_price": 900.0,
        "total": 4500.0
      },
      {
        "item": "Ergonomic Desk Accessories & Filing Trays",
        "qty": 4,
        "unit_price": 1000.0,
        "total": 4000.0
      }
    ],
    "audit_flags": {
      "is_gstin_valid": true,
      "duplicate_detected": false,
      "math_reconciled": true,
      "audit_note": "Standard Business Purchase. Vendor GSTIN active & matched."
    }
  }
}
```

---

## 💡 Key Features Implemented

* **Drag-and-Drop File Upload Zone**: Supports image files (PNG/JPG), PDF invoices, and Excel spreadsheets (`.xlsx`, `.csv`).
* **Live AI Analysis Indicator**: Simulated multi-step processing animation (OCR Scanning, Entity Extraction, Tax Check).
* **Dynamic Results Dashboard**: Displays extracted Vendor, Date, Total Amount, Tax Breakdown, Category, and Line Items without reloading the page.
* **Raw JSON Inspector**: View and copy formatted JSON responses directly for downstream developer inspection or backend integration.
