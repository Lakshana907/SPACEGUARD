# IBM LinuxONE deployment guide

First run SPACEGUARD locally. Deployment depends on the exact Linux image, CPU architecture, firewall and account privileges.

## SSH access
If the private SSH key is missing, use the Community Cloud's documented recovery/support process. A private key generally cannot be downloaded again. Do not delete a working server just to try another key. Ask support or use a documented console/recovery option to install a new public key. Never share the private key or commit it to source control.

## Verify the server after login
```bash
uname -m
cat /etc/os-release
python3 --version
```
Confirm package compatibility for the actual LinuxONE image and architecture (often `s390x`).

## Transfer backend from Windows PowerShell
After valid SSH access, run this from the project root; replace placeholders:
```powershell
scp -i "$HOME\Downloads\your-key.pem" -r .\backend linux1@YOUR_SERVER_IP:~/spaceguard-backend
```

## Install and start API
```bash
cd ~/spaceguard-backend
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000
```
Test in a second shell:
```bash
curl http://127.0.0.1:8000/health
```

## Production checklist
- Use a TLS-enabled reverse proxy such as Nginx; do not expose the development server directly to the public internet.
- Restrict firewall ports and configure CORS to the exact frontend origin.
- Keep secrets outside source code.
- Verify all dependencies support the selected LinuxONE architecture.
- Use systemd or an approved process supervisor after validating paths and permissions.
- The current data is synthetic and the scoring is heuristic. Do not represent it as operational collision prediction.
