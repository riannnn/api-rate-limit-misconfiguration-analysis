# api-rate-limit-misconfiguration-analysis
Security analysis of API rate limiting misconfiguration validated via Burp Suite, cURL automation, and Python scripting.

This project aims to analyze the rate limiting implementation of an API endpoint and identify potential configuration errors that could lead to API misuse.

Tests are performed both manually and automatically to ensure that the system actually executes requests on the backend.

📌Overview

This project aims to analyze the rate of implementation on an API endpoint and identify potential misconfigurations that could impact the API.

Tests were performed both manually and automatically to ensure the system was actually executing requests on the backend.

🎯 Project Objectives

Understand how rate limiting works on APIs

Test the effectiveness of trade requests

Identify potential API throttling

Provide security improvement recommendations

🛠 Testing Methodology

1️⃣ Manual Testing (cURL)

Send requests repeatedly within a short period of time

Observe server responses

Check for HTTP 429 (Too Many Requests) errors

Result:
The server continued to respond with 200 OK without any response.

2️⃣ Automated Testing (Python Script)

Creating a script using the requests library

Sending approximately 50 requests quickly

Logging the status code of each response

Result:
No HTTP 429 or backend network mechanism found.

📊 Findings

The system displays rate limit information

No backend enforcement

All requests are processed without a transaction

No HTTP 429 (Too Many Requests) error appears.

▶ How to Run the Script (If Included)

Install dependency:

pip install requests

Run:

python test_rate_limit.py

📌 Conclusion

The rate limit is only displayed as information, but is not effectively enforced in the backend. This opens up the possibility of API abuse if exploited by irresponsible parties.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Security](https://img.shields.io/badge/Security-Research-red) ![OWASP](https://img.shields.io/badge/OWASP-Aware-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Focus](https://img.shields.io/badge/Focus-API%20Security-critical)
