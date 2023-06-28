import subprocess
import platform

if __name__ == '__main__':
    operating_system = platform.system()
    subprocess.run(["bash", "-c", f"echo -e 'bob\nbob\nbob@admin.de' | ./brat/install.sh"])
    subprocess.Popen(["./brat/standalone.py"])
    if operating_system.lower() == "windows":
        subprocess.Popen(['start', 'cmd', '/c', 'flask --app app.py run'], shell=True)
    elif operating_system.lower() == "linux":
        subprocess.Popen(["flask", "--app", "app.py", "run"])
