import subprocess

resultado = subprocess.run(
    ["powershell", "-Command", "Get-Process"],
    capture_output=True,
    text=True
)

print(resultado.stdout)