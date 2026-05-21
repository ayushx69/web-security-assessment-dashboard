from flask import Flask, render_template, request, Response, send_file
import scanner
import os
from datetime import datetime

app = Flask(__name__)

REPORT_DIR = "reports"
LATEST_REPORT = os.path.join(REPORT_DIR, "latest_scan_report.txt")

os.makedirs(REPORT_DIR, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scan', methods=['POST'])
def scan():
    target_ip = request.form['target_ip']
    target_url = request.form.get('target_url', '')
    selected_tools = request.form.getlist('tools')

    def generate():
        report_lines = []

        def send(line):
            report_lines.append(line)
            return line

        header = f"""
==============================
Website Security Scan Report
==============================
Target: {target_ip}
URL: {target_url if target_url else "Not Provided"}
Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Tools Selected: {", ".join(selected_tools)}
==============================

"""
        yield send(header)

        yield send("Starting Security Scan...\n\n")

        if "nmap" in selected_tools:
            yield send("=== Port Scan Started ===\n")
            yield send(scanner.scan_ports_output(target_ip))
            yield send("\n=== Port Scan Completed ===\n\n")
        else:
            yield send("[!] Nmap skipped\n\n")

        if "nikto" in selected_tools:
            yield send("=== Nikto Scan Started ===\n")
            yield send(scanner.run_nikto_output(target_ip))
            yield send("\n=== Nikto Scan Completed ===\n\n")
        else:
            yield send("[!] Nikto skipped\n\n")

        if "nuclei" in selected_tools:
            yield send("=== Nuclei Scan Started ===\n")
            yield send(scanner.run_nuclei_output(target_ip))
            yield send("\n=== Nuclei Scan Completed ===\n\n")
        else:
            yield send("[!] Nuclei skipped\n\n")

        if "wpscan" in selected_tools:
            yield send("=== WPScan Started ===\n")
            yield send(scanner.run_wpscan_output(f"http://{target_ip}"))
            yield send("\n=== WPScan Completed ===\n\n")
        else:
            yield send("[!] WPScan skipped\n\n")

        if "sqlmap" in selected_tools and target_url:
            yield send("=== SQLMap Scan Started ===\n")
            yield send(scanner.run_sqlmap_output(target_url))
            yield send("\n=== SQLMap Scan Completed ===\n\n")

            yield send("=== XSS Simulation Started ===\n")
            yield send(scanner.simulate_xss_output(target_url))
            yield send("\n=== XSS Simulation Completed ===\n\n")
        else:
            yield send("[!] SQLMap/XSS skipped\n\n")

        yield send("=== Protection Suggestions ===\n")
        yield send(scanner.suggest_protections())

        yield send("\n\nScan Completed.")

        with open(LATEST_REPORT, "w", encoding="utf-8") as f:
            f.write("".join(report_lines))

    return Response(generate(), mimetype='text/plain')


@app.route('/download-report')
def download_report():
    if os.path.exists(LATEST_REPORT):
        return send_file(
            LATEST_REPORT,
            as_attachment=True,
            download_name="security_scan_report.txt"
        )
    return "No report found. Please run a scan first."


if __name__ == '__main__':
    app.run(debug=True)
