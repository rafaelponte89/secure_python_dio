import subprocess
from colors import Colors
color = Colors()
sub_one = subprocess.run(["ls", "-l"])
sub_two=''
try:
    sub_two = subprocess.run('exit 2', shell=True, check=True)
except subprocess.CalledProcessError as e:
    output = sub_two.stderr.decode('utf8')
    print(output)
sub_three = subprocess.run(['ls','-l'], capture_output=True)

print(sub_one)
#print(sub_two)
print(sub_three)
string = sub_three.stdout.decode('utf-8')
if sub_three.returncode == 0:
    print(color.colorIO(string,'blue'))
