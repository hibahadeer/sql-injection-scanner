# SQL Injection Scanner

A simple Python script to test URLs for basic SQL injection vulnerabilities using common payloads.  
Ideal for educational or authorized penetration testing purposes.

---

## 📚 How It Works

1. Takes a target URL with a parameter.
2. Appends each SQL injection payload to the URL.
3. Sends a GET request to the modified URL.
4. Scans the response for known SQL error indicators:
   - `"sql syntax"`
   - `"mysql"`
   - `"warning"`
   - `"unterminated"`
   - `"query failed"`
5. If any of these indicators are found in the response, it reports the URL as **potentially vulnerable**.
