import subprocess

cmd = 'Get-Service | Where-Object {$_.Status -eq "Running"}'

resultado = subprocess.run(
    ["powershell", "-Command", cmd],
    capture_output=True,
    text=True
)

print(resultado.stdout)
