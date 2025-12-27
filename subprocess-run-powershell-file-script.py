import subprocess

resultado = subprocess.run(
    ["powershell", "-File", "subprocess-run-powershell-file-script.ps1"],
    capture_output=True,
    text=True
)

print(resultado.stdout)