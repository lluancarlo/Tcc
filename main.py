
import bluetooth
import RPi.GPIO
import thread as th
import time
import os

class driver:
	def __init__(self, nome, dtanasc, cnh, cnhtip, dtavenc, totalkm, mediakm, mediatemp):
		self.nome = nome
		self.dtanasc = dtanasc
		self.cnh = cnh
		self.cnhtip = cnhtip
		self.dtavenc = dtavenc
		self.totalkm = totalkm
		self.mediakm = mediakm
		self.mediatemp = mediatemp
class bt:
	def __init__(self, port):
		self.server = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
		self.server.bind(("",port))
		self.server.listen(port)
	def connect(self):
		self.client, self.clientAddress = self.server.accept()
	def recvMsg(self):
		return self.client.recv(1024)
	def sendMsg(self,msg):
		self.client.send(msg)
	def close(self):
		self.client.close()
		self.server.close()

class led:
	status = 0
	def __init__(self, pine):
		self.pine = pine
		RPi.GPIO.setup(self.pine, RPi.GPIO.OUT)
	def On(self):
		RPi.GPIO.output(self.pine, RPi.GPIO.HIGH)
		self.status = 1
	def Off(self):
		RPi.GPIO.output(self.pine, RPi.GPIO.LOW)
		self.status = 0

class motor:
        status = 0
        def __init__(self, pine):
                self.pine = pine
                RPi.GPIO.setup(self.pine, RPi.GPIO.OUT)
        def On(self):
                RPi.GPIO.output(self.pine, RPi.GPIO.HIGH)
                self.status = 1
        def Off(self):
                RPi.GPIO.output(self.pine, RPi.GPIO.LOW)
                self.status = 0

class buzzer:
	status = 0
	def __init__(self, pine):
		self.pine = pine
		RPi.GPIO.setup(self.pine, RPi.GPIO.OUT)
	def play1(self):
		self.buzz = RPi.GPIO.PWM(self.pine, 1)
		self.buzz.start(1)
		for dc in range(150,1800,10):
			self.buzz.ChangeFrequency(dc)
			time.sleep(0.01)
		for dc in range(1800, 150, -10):
			self.buzz.ChangeFrequency(dc)
			time.sleep(0.01)
		self.buzz.stop()
	def playStarWars(self):
		self.buzz = RPi.GPIO.PWM(self.pine, 1)
		self.buzz.start(1)

		timeNt = [500,500,500,350,150,500,350,150,1000,500,500,500,350,150,500,350,150,1000,500,350,150,500,250,250,125,125,
			  350,  1,250,500,250,250,125,125,250,  1,125,500,375,125,500,375,125,1000,500,250,150,500,250,250,125,125,
			  250,  1,250,500,250,250,125,125,250,  1,250,500,375,125,500,375,125,1000]
		melody = [440,440,440,349,523,440,349,523, 440,659,659,659,698,523,415,349,523, 440,880,440,440,880,830,784,740,698,
			  740,250,455,622,587,554,523,466,523,250,349,415,349,440,523,440,523, 659,880,440,440,880,830,784,740,698,
			  740,250,455,622,587,554,523,466,523,250,349,415,349,523,440,349,261,440]

		for x in range(0,len(melody),1):
			self.buzz.ChangeFrequency(melody[x])
			time.sleep(float(timeNt[x]/1000.000))
		self.buzz.stop()

	def playMario(self):
		self.buzz = RPi.GPIO.PWM(self.pine, 1)
		self.buzz.start(1)

		timeNt = [120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120,
                          120, 120, 120, 120,  90,  90,  90, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120,
                          120, 120, 120, 120, 120, 120, 120,  90,  90,  90, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120]
		melody = [2637, 2637, 250, 2637, 250, 2093, 2637, 250, 3136, 250,  250, 250, 1568, 250, 250, 250, 2093, 250, 250, 1568, 250, 250, 1319, 250, 250,
			  1760, 250, 1976, 250, 1865, 1760, 250, 1568, 2637, 3136, 3520, 250, 2794, 3136, 250, 2637, 250, 2093, 2349, 1976, 250, 250, 2093, 250,
			  250, 1568, 250, 250, 1319, 250, 250, 1760, 250, 1976, 250, 1865,  1760, 250, 1568, 2637, 3136, 3520, 250, 2794, 3136, 250, 2637, 250,
			  2093, 2349, 1976, 250, 250]

		for x in range(0,len(melody),1):
			self.buzz.ChangeFrequency(melody[x])
			time.sleep(float(timeNt[x]/1000.000))
		self.buzz.stop()

	def playPirates(self):
		self.buzz = RPi.GPIO.PWM(self.pine, 1)
		self.buzz.start(1)

		timeNt = [125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 375, 125, 125, 125,
			  250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 375, 125, 125, 125, 250, 125,
			  125, 125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 125, 250, 125, 125, 125, 250, 125, 125,
			  250, 125, 250, 125, 125, 125, 250, 125, 125, 125, 125, 375, 375, 250, 125, 125, 125, 250, 125, 125, 125,
			  125, 250, 125, 125, 125, 125, 375, 125, 125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 250,
			  125, 125, 125, 125, 375, 125, 125, 125, 250, 125, 125, 125, 125, 250, 125, 125, 125, 125, 250, 125, 125,
			  125, 125, 125, 250, 125, 125, 125, 250, 125, 125, 250, 125, 250, 125, 125, 125, 250, 125, 125, 125, 125,
			  375, 375, 250, 125, 375, 250, 125, 375, 125, 125, 125, 125, 125, 125, 125, 125, 375, 250, 125, 375, 250,
			  125, 375, 125, 125, 125, 125, 125, 500, 250, 125, 375, 250, 125, 375, 125, 125, 125, 125, 125, 125, 125,
			  125, 375, 250, 125, 375, 250, 125, 375, 125, 125, 125, 125, 125, 500]
		melody = [330, 392, 440, 440,250, 440, 494, 523, 523,250, 523, 587, 494, 494,250, 440, 392, 440,250, 330, 392, 440, 440,
                           250, 440, 494, 523, 523,250, 523, 587, 494, 494,250, 440, 392, 440,250, 330, 392, 440, 440,250, 440, 523, 587,
                          587,250, 587, 659, 698, 698,250, 659, 587, 659, 440,250, 440, 494, 523, 523,250, 587, 659, 440,250, 440, 523,
                          494, 494,250, 523, 440, 494,250, 440, 440, 440, 494, 523, 523,250, 523, 587, 494, 494,250, 440, 392, 440,250,
                          330, 392, 440, 440,250, 440, 494, 523, 523,250, 523, 587, 494, 494,250, 440, 392, 440,250, 330, 392, 440, 440,
                           250, 440, 523, 587, 587,250, 587, 659, 698, 698,250, 659, 587, 659, 440,250, 440, 494, 523, 523,250, 587, 659,
                          440,250, 440, 523, 494, 494,250, 523, 440, 494,250, 659,250,250, 698,250,250, 659, 659,250, 784,250, 659, 587,250,250,
                          587,250,250, 523,250,250, 494, 523,250, 494,250, 440, 659,250,250, 698,250,250, 659, 659,250, 784,250, 659, 587,250,250,
                          587,250,250, 523,250,250, 494, 523,250, 494,250, 440]

		for x in range(0,len(melody),1):
			self.buzz.ChangeFrequency(melody[x])
			time.sleep(float(timeNt[x]/1000.000))
		self.buzz.stop()

if __name__ == "__main__":
	#Set Global Board Mode
	RPi.GPIO.setmode(RPi.GPIO.BOARD)
	l = led(11)
	l.On()

	"""
	def Test():
		RPi.GPIO.setmode(RPi.GPIO.BOARD)
		trig = 20
		echo = 21
		RPi.GPIO.setup(trig, GPIO.OUT)
		RPi.GPIO.setup(echo, GPIO.IN)

		RPi.GPIO.output(trig, false)
		print("Pegando Distancia..")
		time.sleep(2)

		RPi.GPIO.output(trig, true)
		time.sleep(1)
		RPi.GPIO.output(trig, false)

		while RPi.GPIO.input(echo) == 0:
			pulse_start = time.time()

		while RPi.GPIO.input(echo) == 1:
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17150

		distance = round(distance, 2)

		print("A distancia e ",distance," cm")
	"""

	def turnOnBt():
		os.system('hciconfig hci0 piscan')
		op = ''
		bth = bt(1)
		bth.connect()
		bth.sendMsg('\n[COMANDO] -> ')

		#Def Driver
		motoristaA = driver('Luan Carlo', '23/09/1997', '12345678910', 'A', '16/10/2020', '13.876,27','9,6 Km/L', '39M')
		motoristaB = driver('Thiago Almeida', '05/07/19??', '12345678910', 'A, B', '02/03/2021', '6.285,03','8,2 Km/L', '1H 13M')
		motoristaC = driver('Jose Camacho', '01/02/19??', '12345678910', 'A, D', '19/06/2023', '8.189,62','10,2 Km/L', '1H 35M')

		#imports
		farol = led(40)
		bozina = buzzer(36)
		mot = motor(32)

		#Process
		while op != 'z':
			op = bth.recvMsg()
			if (op=='1'):
				if (farol.status == 0):
					farol.On()
					bth.sendMsg('\n\n[SISTEMA] -> Farol Ligado!')
				else:
					farol.Off()
					bth.sendMsg('\n\n[SISTEMA] -> Farol Desligado!')
				bth.sendMsg('\n\n[COMANDO] ->  ')
			elif (op=='2'):
                                if (mot.status ==0):
                                        mot.On()
                                else:
                                        mot.Off()
			elif (op=='3'):
				if (bozina.status ==0):
					bozina.playStarWars()
				else:
					bozina.Off()
			elif (op=='4'):
				if (bozina.status ==0):
					bozina.playPirates()
				else:
					bozina.off()
			elif(op=='5'):
				if (bozina.status ==0):
					bozina.playMario()
				else:
					bozina.off()
			elif(op=='a'):
				bth.sendMsg('\n\n[MOTORISTA A] \n[NOME] -> {}\n[NASC] -> {}\n[CNH] -> {}\n[TIPO] -> {}\n[VENC] ->{}\n[TOTAL KM] -> {}\n[MEDIA KM] -> {}\n[MEDIA TEMPO] -> {}'.format(motoristaA.nome, motoristaA.dtanasc, motoristaA.cnh, motoristaA.cnhtip, motoristaA.dtavenc, motoristaA.totalkm, motoristaA.mediakm, motoristaA.mediatemp))
				bth.sendMsg('\n\n[COMANDO] ->  ')
			elif(op=='b'):
                                bth.sendMsg('\n\n[MOTORISTA B] \n[NOME] -> {}\n[NASC] -> {}\n[CNH] -> {}\n[TIPO] -> {}\n[VENC] ->{}\n[TOTAL KM] -> {}\n[MEDIA KM] -> {}\n[MEDIA TEMPO] -> {}'.format(motoristaB.nome, motoristaB.dtanasc, motoristaB.cnh, motoristaB.cnhtip, motoristaB.dtavenc, motoristaB.totalkm, motoristaB.mediakm, motoristaB.mediatemp))
                                bth.sendMsg('\n\n[COMANDO] ->  ')
			elif(op=='c'):
                                bth.sendMsg('\n\n[MOTORISTA C] \n[NOME] -> {}\n[NASC] -> {}\n[CNH] -> {}\n[TIPO] -> {}\n[VENC] ->{}\n[TOTAL KM] -> {}\n[MEDIA KM] -> {}\n[MEDIA TEMPO] -> {}'.format(motoristaC.nome, motoristaC.dtanasc, motoristaC.cnh, motoristaC.cnhtip, motoristaC.dtavenc, motoristaC.totalkm, motoristaC.mediakm, motoristaC.mediatemp))
                                bth.sendMsg('\n\n[COMANDO] ->  ')

		else:
			l.Off()
			bth.sendMsg('\n\n[DESLIGANDO SISTEMA...]')
			bth.close()
			os.system('shutdown')
	turnOnBt()
