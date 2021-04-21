from machine import*
from time import*
import wifi_connect
import socket

#led1 = Pin(4, Pin.OUT)
led2 = PWM(Pin(5),Pin.OUT)
led2.freq(500)


#def nyala1():
#    a = 0
#    while True:
#        a += 1
#        led.on()
#        sleep(3)
#        led.off()
#        sleep(3)
#        if a == 3:
#            led.off()
#
#def nyala2():
#    a = 0
#    while True:
#        led.on()
#        sleep(0.3)
#        led.off()
#        sleep(0.3)
#        if a == 10:
#            led.off()

# HTML WEB PAGE
def web_page():
    html = '''<!DOCTYPE html>
    <html>
    <head>
    	<title>Remote Control</title>
    	<style>
    		.tombol1{
    			color: Red;
    			margin-bottom: 10px;
    		}

            .tombol2{
                color: Blue;
            }
    	</style>
    </head> 

    <body>
    	<form>
    		<center>
    			<button class="tombol1" name="TOMBOL" value="EXECUTE1" type="submit">
    				PUSH 1
    			</button>
    		</center>

            <center>
    			<button class="tombol2" name="TOMBOL" value="EXECUTE2" type="submit">
    				PUSH 2
    			</button>
    		</center>
    	</form>

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

    nyala_1 = request.find('/?TOMBOL=EXECUTE1')
    nyala_2 = request.find('/?TOMBOL=EXECUTE2')

    if nyala_1 == 6:
        led2.duty(500)

    elif nyala_2 == 6:
        led2.duty(100)

    response = web_page()
    conn.send('HTTP/1.1 200 OK/n')
    conn.send('Content-Type : text/html\n')
    conn.send('Connection : close\n\n')
    conn.sendall(response)
    conn.close()