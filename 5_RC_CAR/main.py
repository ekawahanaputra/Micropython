from machine import*
from time import*
import wifi_connect
import socket

speed_RH = PWM(Pin(5), Pin.OUT)
speed_RH.freq(500)
direct_RH = Pin(0, Pin.OUT)

speed_LH = PWM(Pin(4), Pin.OUT)
speed_LH.freq(500)
direct_LH = Pin(2, Pin.OUT)


def Maju():
    speed_RH.duty(1100)
    speed_LH.duty(1100)
    direct_RH.value(0)
    direct_LH.value(1)

def Mundur():
    speed_RH.duty(1000)
    speed_LH.duty(1000)
    direct_RH.value(1)
    direct_LH.value(0)

def Stop():
    speed_RH.duty(0)
    speed_LH.duty(0)

def Belok_Kanan():
	speed_RH.duty(1100)
	speed_LH.duty(1100)
	direct_RH.value(1)
	direct_LH.value(1)

def Belok_Kiri():
    speed_RH.duty(1100)
    speed_LH.duty(1100)
    direct_RH.value(0)
    direct_LH.value(0)



  
def Web_Page():

	html = '''<!DOCTYPE html>
	<html>
	<head>
		<title>REMOTE CONTROL</title>
		<style type="text/css">

			h1{
				font-weight: bold;
			}

			.bfwd{
				background-color: LightGreen;
				font-weight: bold;
				margin-bottom: 20px;
				font-size: 40px;
				width: 230px;
				height: 100px;
				position: relative;
				left: 470px;
			}

			.bstop{
				background-color: rgb(177, 55, 55);
				font-weight: bold;
				margin-top: 20px;
				margin-bottom: 20px;
				position: relative;
				font-size: 40px;
				width: 230px;
				height: 100px;
				position: relative;
				top: 100px;
			}

			.brev{
				background-color: LightGreen;
				font-weight: bold;
				margin-top: 20px;
				font-size: 40px;
				width: 230px;
				height: 100px;
				position: relative;
				right: 470px;
				top: 200px;
			}

			.bright{
				background-color: Yellow;
				font-weight: bold;
				position: relative;
				font-size: 40px;
				width: 230px;
				top: 100px;
				left: 20px;
				height: 262px;
				}

			.bleft{
				background-color: Yellow;
				font-weight: bold;
				position: relative;
				font-size: 40px;
				width: 230px;
				top: 100px;
				right: 20px;
				height: 262px;
			}

			div{
				position: relative;
				top: 150px;
				bottom: 50px;
			}


		</style>

	</head>
	<body>
		<center>
		<form>
			<h1>REMOTE CONTROL</h1>


			<center>
			<button class="bfwd" name="BUTTON" value="FORWARD" type="submit">
			MAJU </button>

			<button class="bleft" name="BUTTON" value="LEFT" type="submit">
			LEFT</button>

			<button class="bstop", name="BUTTON", value="STOP", type="submit">
			STOP</button>

			<button class="bright" name="BUTTON" value="RIGHT" type="submit">
			RIGHT</button>

			<button class="brev" name="BUTTON" value="REVERSE" type="submit">
			MUNDUR</button>

			</center>


		</form>
		</center>

	</body>
	</html>
	'''
	return html



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
    
# EXECUTE PROGRAM
while True:
    # socket accept
    conn, addr = s.accept()
    request = conn.recv(1024)
    request = str(request)

    MAJU = request.find('/?BUTTON=FORWARD')
    MUNDUR = request.find('/?BUTTON=REVERSE')
    DIAM = request.find('/?BUTTON=STOP')
    BELOK_RH = request.find('/?BUTTON=RIGHT')
    BELOK_LH = request.find('/?BUTTON=LEFT')

    if MAJU == 6:
        Maju()

    elif DIAM == 6:
        Stop()

    elif MUNDUR == 6:
        Mundur()

    elif BELOK_RH == 6:
        Belok_Kanan()

    elif BELOK_LH == 6:
        Belok_Kiri()


    response = Web_Page()
    conn.send('HTTP/1.1 200 OK/n')
    conn.send('Content-Type : text/html\n')
    conn.send('Connection : close\n\n')
    conn.sendall(response)
    conn.close()