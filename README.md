Takes a target URL with a parameter.

Appends each payload to the URL.

Sends a GET request and scans the response for known SQL error indicators:

"sql syntax"

"mysql"

"warning"

"unterminated"

"query failed"

If any are found, it reports the URL as potentially vulnerable.
