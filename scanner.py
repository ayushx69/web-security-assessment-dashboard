import nmap
import subprocess
import os

def scan_ports_output(target):
    nm = nmap.PortScanner()
    output = ""
    try:
        nm.scan(target, '21,22,23,25,53,80,110,139,143,443,445,3306,8080')
        for host in nm.all_hosts():
            output += f"Host: {host} ({nm[host].hostname()})\n"
            output += f"State: {nm[host].state()}\n"
            for proto in nm[host].all_protocols():
                output += f"Protocol: {proto}\n"
                for port in sorted(nm[host][proto].keys()):
                    state = nm[host][proto][port]['state']
                    output += f"Port {port}\tState: {state}\n"
    except Exception as e:
        output = f"Port scan error: {e}\n"
    return output

def run_nikto_output(target):
    try:
        command = f"nikto -h http://{target} -Tuning 1 -nossl -nointeractive -o nikto_report.txt -Format txt"
        result = subprocess.getoutput(command)
        return f"Nikto scan completed. Report saved as nikto_report.txt.\n{result}"
    except Exception as e:
        return f"Error running Nikto scan: {e}"

def run_nuclei_output(target):
    try:
        command = f"nuclei -u http://{target} -o nuclei_report.txt"
        result = subprocess.getoutput(command)
        return f"Nuclei scan completed. Report saved as nuclei_report.txt.\n{result}"
    except Exception as e:
        return f"Error running Nuclei scan: {e}"

def run_zap_output(target):
    try:
        result = subprocess.getoutput(f"zap-baseline.py -t {target} -m 5 -r zap_report.html")
        return f"ZAP scan completed. Report saved as zap_report.html.\n{result}"
    except Exception as e:
        return f"Error running ZAP scan: {e}"

def run_sqlmap_output(url):
    try:
        return subprocess.getoutput(f"sqlmap -u {url} --batch")
    except Exception as e:
        return f"Error running SQLMap scan: {e}"

def simulate_xss_output(url):
    payload = "<script>alert('XSS')</script>"
    return f"SIMULATED XSS PAYLOAD for {url}: {payload}"

def run_wpscan_output(target):
    try:
        cache_dir = os.path.join(os.getcwd(), "wpscan_cache")
        os.makedirs(cache_dir, exist_ok=True)

        command = f"wpscan --url {target} --enumerate u,vp,vt --api-token bLsxbU1fyY9jYCimalyfmPJhn7rG7kxKb1fzuFTdiFQ --cache-dir {cache_dir}"
        result = subprocess.getoutput(command)
        return result
    except Exception as e:
        return f"Error running WPScan: {e}"

def suggest_protections():
    return """
BASIC PROTECTION SUGGESTIONS:
 - Use a Web Application Firewall (e.g., CloudFlare)
 - Sanitize and validate user inputs
 - Keep software and dependencies updated
 - Use HTTPS everywhere
 - Implement security headers (CSP, X-Frame-Options, etc.)
 - Configure proper CORS settings
"""

# === CLI Execution ===
if __name__ == "__main__":
    target = input("Enter Target IP or Hostname (e.g. example.com): ").strip()
    print("\n=== Port Scan ===")
    print(scan_ports_output(target))

    print("\n=== Nikto Scan ===")
    print(run_nikto_output(target))

    print("\n=== Nuclei Scan ===")
    print(run_nuclei_output(target))

    print("\n=== ZAP Scan ===")
    print(run_zap_output(target))

    url = input("\nEnter URL for SQLMap/XSS (optional, include http://): ").strip()
    if url:
        print("\n=== SQLMap Scan ===")
        print(run_sqlmap_output(url))

        print("\n=== XSS Simulation ===")
        print(simulate_xss_output(url))

    # WPScan – Only run if it looks like a WordPress site
    if "wptest.io" in target or "wordpress" in target.lower():
        print("\n=== WPScan ===")
        print(run_wpscan_output(target))
    else:
        print("\n[!] WPScan skipped: Target is not a WordPress site.")

    print("\n=== Protection Suggestions ===")
    print(suggest_protections())

