#SCRIPTS CREATE BY AK SAED 
#chor Kishoreganj black hat👨‍💻HACKER
#---------------------● IMPORT ●---------------------#
import cython,os,time,marshal
#---------------------● COLOUR ●---------------------#
G="\x1b[38;5;46m";W="\x1b[38;5;15m";B="\x1b[38;5;265m";Y="\x1b[38;5;226m";A="\x1b[38;5;123m";R="\x1b[38;5;160m";O="\x1b[38;5;81m"
#---------------------● STYLE ●---------------------#
xd=f"{G}>{Y}>{W}";xd1=f"{G}0{Y}1{W}";xd2=f"{G}0{Y}2{W}"
#---------------------● CLEAR ●---------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{Y}──────────────────────────────────────────────────')
#---------------------● LOGO ●---------------------#
logo=(f"""
      {Y}███████╗   █████╗   ███████╗██████╗  
   {W}  ██╔════╝██╔══██╗██╔════╝██      ═██╗  {W} OWNER  {Y}:{W} AK-SAED
      {Y}███████╗███████║█████╗      ██║      ██║  {W} TOOLS  {Y}:{W} MARSHAL {Y}|{W} CYTHON ENC
    {W} ╚════██║██╔══██║██╔══╝      ██║      ██║  {W} STATUS {Y}:{W} F{Y}R{W}EE
      {Y}███████║██║      ██║███████   ██████╔╝
     {W}╚══════╝╚═╝      ╚═╝╚══════╝╚═════╝
{Y}──────────────────────────────────────────────────""")
#---------------------● MAIN MENU ●---------------------#
def ___swag___():
	clear();print(f"{xd1} START CYTHON ENCODE ");print(f"{xd2} START MARSHAL ENCODE ");linex();option = input(f"{xd} SELECT : ")
	if option in ["1"]:___cythonx___()
	if option in ["2"]:___marshalx___()
	else:linex();print(f"{xd} OPTION NOT FOUND ");linex();time.sleep(1);print(f"{xd} TRY AGAIN BROTHER");time.sleep(1);___saed___()
#---------------------● CYTHON ●---------------------#
def ___cythonx___():
	clear();print(f"{xd} EXAMPLE : AK.py {Y}|{W} SAED.py {Y}|{W} HASAN.py ");linex()
	encfilex=input(f"{xd} ENTER YOUR FILE NAME : ")
	clear();print(f"{xd} WAITING FOR CYTHON ENCODE");linex();os.system(f"cythonize -b {encfilex}");linex();print(f"{xd} SUCCESSFUL CYTHON ENCODE");exit()
#---------------------● CYTHON USE CODE ●---------------------#
def ___marshalx___():
	clear();print(f"{xd} EXAMPLE : /sdcard/AK.py {Y}|{W} /sdcard/SAED.py ");linex()
	x=input(f"{xd} ENTER YOUR FILE NAME : ") 
	try:
		q = x.split('.')
		u = q[0] + "_enc.py"
	except:
		u = input(f"{xd} ENTER YOUR FILE SAVE NAME : ")
	f = int(input(f"{xd} ENCODE COUNT LIMIT : "))
	linex()
	a = open(x).read()
	try:
		j = 0
		for i in range(f):
			j += 1
			m = compile(a, ' ', 'exec')
			k = marshal.dumps(m)
			t = '#ENCODED By : AK SAED \n#ENCRYPTION : PY3 MARSHAL\n\nimport marshal\nexec(marshal.loads('+repr(k)+'))'
			time.sleep(0.004)
			print(f"{xd} ENCODE COUNT :{G} " + str(j))
	except ValueError:
		exit(f"{xd} WRONG INPUT VALUE")
	except FileNotFoundError:
		exit(f"{xd} FILE " + x + "NOT FOUND")
	linex()
	l = open(u, 'w')
	l.write(t)
	l.close()
	print(f"{xd} YOUR ENCODE FILE SAVE AS :{G} " + u )
___swag___()
