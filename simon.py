import lcddriver
import time
import RPi.GPIO as GPIO
import random
import sys

time.sleep(0.8)
lcd=lcddriver.lcd()

rojo=19
verde=26
amarillo=16
blanco=20

botonR=9
botonV=11
botonA=25
botonB=8

correcto=6
incorrecto=5

reset=24

buzzer=12

rojoU=17
verdeU=27
amarilloU=15
blancoU=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(rojo, GPIO.OUT)
GPIO.setup(verde, GPIO.OUT)
GPIO.setup(amarillo, GPIO.OUT)
GPIO.setup(blanco, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(botonR, GPIO.IN)
GPIO.setup(botonV, GPIO.IN)
GPIO.setup(botonA, GPIO.IN)
GPIO.setup(botonB, GPIO.IN)
GPIO.setup(rojoU, GPIO.OUT)
GPIO.setup(verdeU, GPIO.OUT)
GPIO.setup(amarilloU, GPIO.OUT)
GPIO.setup(blancoU, GPIO.OUT)
GPIO.setup(correcto, GPIO.OUT)
GPIO.setup(incorrecto, GPIO.OUT)
GPIO.setup(reset, GPIO.IN)

GPIO.output(correcto, False)

first=True
num=0
color=0
num_colores=-1

num_restart=0

num_rest=0

global colores

try:
	time.sleep(0.8)

	while True:

#		GPIO.output(rojo, False)

		def num_random():
			a=True
			while a:
				a=False
				numero=[-1,-2,-3]
				color0=random.randrange(4)
				numero.append(color)
				for i in numero:
					num=i
				if numero[num]==numero[num-1]:
					if numero[num]==numero[num-2]:
						if numero[num]==numero[num-3]:
							a=True
				return color0

#		while(True):
#			time.sleep(1)
#			print(GPIO.input(b))
		colores=[]
		def start():
			color=num_random()
			colores.append(color)
			i=0
			l=len(colores)
			print(l)
			while(i<l):
				lcd.lcd_display_string("Memorice:",1,1)
				if colores[i]==0:
					print("ROJO-0")
					GPIO.output(rojo, True)
					lcd.lcd_display_string("Rojo",2,1)
					GPIO.output(buzzer, True)
					time.sleep(0.5)
					GPIO.output(buzzer, False)
					GPIO.output(rojo, False)
					time.sleep(0.5)
					lcd.lcd_clear()
				if colores[i]==1:
					print("VERDE-1")
					GPIO.output(verde, True)
					lcd.lcd_display_string("Verde",2,1)
					GPIO.output(buzzer, True)
					time.sleep(0.5)
					GPIO.output(buzzer, False)
					GPIO.output(verde, False)
					time.sleep(0.5)
					lcd.lcd_clear()
				if colores[i]==2:
					print("AMARILLO-2")
					GPIO.output(amarillo, True)
					lcd.lcd_display_string("Amarillo",2,1)
					GPIO.output(buzzer, True)
					time.sleep(0.5)
					GPIO.output(buzzer, False)
					GPIO.output(amarillo, False)
					time.sleep(0.5)
					lcd.lcd_clear()
				if colores[i]==3:
					print("BLANCO-3")
					GPIO.output(blanco, True)
					lcd.lcd_display_string("Blanco",2,1)
					GPIO.output(buzzer, True)
					time.sleep(0.5)
					GPIO.output(buzzer, False)
					GPIO.output(blanco, False)
					time.sleep(0.5)
					lcd.lcd_clear()

				rest=GPIO.input(reset)
				if(rest==1):
					time.sleep(1.5)
					rest=GPIO.input(reset)
					if(rest==1):
						lcd.lcd_display_string("RECONFIGURANDO",1)
						time.sleep(1.5)
						restart()
						sys.exit()
				i=i+1

			lcd.lcd_clear()
			return num_colores + 1

		def pr(c):
			print("Num_bot: ",num_bot)
			print("len: ", len(colores))
			print("Boton: ", c)
			l=len(colores)
			x=0
			while(x<l):
				print("x: ", x)
				print(colores[x])
				x=x+1

		def delete():
		#	y=1
		#	le=len(colores)
		#	while(y<le):
		#		colores.remove(y)
		#		y=y+1

			for y in colores:
				colores.remove(y)

		def mal():

			print("INCORRECTO")
			lcd.lcd_display_string("INCORRECTO",2,1)
			GPIO.output(incorrecto, True)
			GPIO.output(buzzer, True)
			time.sleep(0.3)
			GPIO.output(buzzer, False)
			time.sleep(0.2)
			GPIO.output(buzzer, True)
			time.sleep(0.3)
			GPIO.output(buzzer, False)
			GPIO.output(incorrecto, False)
			delete()
		#	num_bot=0
		#	num_colores=0
			colores=[]
			time.sleep(1.5)
			lcd.lcd_clear()
		#	introducir=False
		#	ok=False

		def bien():

			print("CORRECTO")
			lcd.lcd_display_string("CORRECTO",2,1)
			GPIO.output(correcto, True)
			num_bot=0
			time.sleep(1.5)
			GPIO.output(correcto, False)
			lcd.lcd_clear()

		def restart():

			lcd.lcd_display_string("Limpiando pines",1)

			GPIO.cleanup()
			slep=0.5

			time.sleep(1)

			lcd.lcd_display_string("Config. leds", 1)

			time.sleep(1)

			rojoU=17

			lcd.lcd_display_string("11",2)

			time.sleep(slep)

			verdeU=27

			lcd.lcd_display_string("1113",2)

			time.sleep(slep)

			amarilloU=15

			lcd.lcd_display_string("111310",2)

			time.sleep(slep)

			blancoU=18

			lcd.lcd_display_string("11131012", 2)

			time.sleep(slep)

			rojo=19

			lcd.lcd_display_string("1113101235",2)

			time.sleep(slep)

			verde=26

			lcd.lcd_display_string("111310123537",2)

			time.sleep(slep)

			amarilllo=16

			lcd.lcd_display_string("11131012353736",2)

			time.sleep(slep)

			blanco=20

			lcd.lcd_display_string("1113101235373638",2)

			time.sleep(1)

			lcd.lcd_clear()

			lcd.lcd_display_string("GPIO.BCM",1,1)

			GPIO.setmode(GPIO.BCM)

			time.sleep(1)

			lcd.lcd_display_string("Led:",1,1)

			GPIO.setup(rojoU, GPIO.OUT)
			lcd.lcd_display_string("Rojo, 11, 17",2)
			time.sleep(0.5)
			GPIO.output(rojoU, True)
			time.sleep(0.5)
			GPIO.output(rojoU, False)

			GPIO.setup(verdeU, GPIO.OUT)
			lcd.lcd_display_string("Verde, 13, 27",2)
			time.sleep(0.5)
			GPIO.output(verdeU, True)
			time.sleep(0.5)
			GPIO.output(verdeU, False)

			GPIO.setup(amarilloU, GPIO.OUT)
			lcd.lcd_display_string("Amarillo, 10, 15",2)
			time.sleep(0.5)
			GPIO.output(amarilloU, True)
			time.sleep(0.5)
			GPIO.output(amarilloU, False)

			GPIO.setup(blancoU, GPIO.OUT)
			lcd.lcd_display_string("Blanco, 12, 18",2)
			time.sleep(0.5)
			GPIO.output(blancoU, True)
			time.sleep(0.5)
			GPIO.output(blancoU, False)

			buzzer=12

			lcd.lcd_display_string("Buzzer:",1,1)

			GPIO.setup(buzzer, GPIO.OUT)
			lcd.lcd_display_string("Buzzer, 32, 12",2)
			time.sleep(0.5)
			GPIO.output(buzzer, True)
			time.sleep(0.5)
			GPIO.output(buzzer, False)

			GPIO.setup(rojo, GPIO.OUT)
			lcd.lcd_display_string("Led:",1,1)
			lcd.lcd_display_string("Rojo, 35, 19",2)
			time.sleep(0.5)
			GPIO.output(rojo, True)
			time.sleep(0.5)
			GPIO.output(rojo, False)

			GPIO.setup(verde, GPIO.OUT)
			lcd.lcd_display_string("Verde, 37, 26",2)
			time.sleep(0.5)
			GPIO.output(verde, True)
			time.sleep(0.5)
			GPIO.output(verde, False)

			GPIO.setup(amarillo, GPIO.OUT)
			lcd.lcd_display_string("Amarillo, 36, 16",2)
			time.sleep(0.5)
			GPIO.output(amarillo, True)
			time.sleep(0.5)
			GPIO.output(amarillo, False)

			GPIO.setup(blanco, GPIO.OUT)
			lcd.lcd_display_string("Blanco, 38, 20",2)
			time.sleep(0.5)
			GPIO.output(blanco, True)
			time.sleep(0.5)
			GPIO.output(blanco, False)

			lcd.lcd_clear()

			lcd.lcd_display_string("LISTO",2,1)

			time.sleep(1)

			lcd.lcd_clear()

			lcd.lcd_display_string("Confg. botones",1)
			time.sleep(1)

			botonR=9

			lcd.lcd_display_string("21",2)

			time.sleep(slep)

			botonV=11

			lcd.lcd_display_string("2123",2)

			time.sleep(slep)

			botonA=25

			lcd.lcd_display_string("212322",2)

			time.sleep(slep)

			botonB=8

			lcd.lcd_display_string("21232224",2)

			time.sleep(slep)

			lcd.lcd_display_string("2123222418",2)

			reset=24

			time.sleep(1)

			Cr=False
			Cv=False
			Ca=False
			Cb=False

			comprovar=True

			correcto=6
			incorrecto=5

			lcd.lcd_clear()
			lcd.lcd_display_string("Boton:",1,1)

			GPIO.setup(botonR, GPIO.IN)
			GPIO.setup(botonV, GPIO.IN)
			GPIO.setup(botonA, GPIO.IN)
			GPIO.setup(botonB, GPIO.IN)
			GPIO.setup(reset, GPIO.IN)

			GPIO.setup(correcto, GPIO.OUT)
			GPIO.setup(incorrecto, GPIO.OUT)

			while(comprovar):

				GPIO.setup(botonR, GPIO.IN)
				GPIO.setup(botonV, GPIO.IN)
				GPIO.setup(botonA, GPIO.IN)
				GPIO.setup(botonB, GPIO.IN)
			#	time.sleep(0.3)
				rB=GPIO.input(botonR)
			#	time.sleep(3)
				vB=GPIO.input(botonV)
			#	time.sleep(3)
				aB=GPIO.input(botonA)
			#	time.sleep(3)
				bB=GPIO.input(botonB)

				if(rB==1):
					print("ROJO")
					lcd.lcd_display_string("Rojo, 21, 9",2)
					Cr=True

				if(vB==1):
					print("VERDE")
					lcd.lcd_display_string("Verde, 23, 11",2)
					Cv=True

				if(aB==1):
					print("AMARILLO")
					lcd.lcd_display_string("Amarillo, 22, 25",2)
					Ca=True

				if(bB==1):
					print("BLANCO")
					lcd.lcd_display_string("Blanco, 24, 8",2)
					Cb=True

				if(Cr==True):
					if(Cv==True):
						if(Ca==True):
							if(Cb==True):
								time.sleep(1)
								lcd.lcd_clear()
								lcd.lcd_display_string("Boton reset:",1,1)
								terminado=True
								while(terminado):
									r=GPIO.input(reset)
									if(r==1):
										terminado=False
										lcd.lcd_display_string("BotonR, 18, 24",2)
										time.sleep(1)
									#	lcd.lcd_clear()
										lcd.lcd_display_string("Terminando",1,1)


										GPIO.output(incorrecto, True)
										lcd.lcd_display_string("LED1, 29,5 ",2)
										time.sleep(1)
										GPIO.output(incorrecto, False)

										GPIO.output(correcto, True)
										lcd.lcd_display_string("LED1, 29, LED2,31 ,6 ",2)
										time.sleep(1)
										GPIO.output(correcto, False)
										break
								comprovar=False
								print("ECHO")
								time.sleep(0.5)
								lcd.lcd_clear()
								time.sleep(0.3)
								lcd.lcd_display_string("ECHO",1,1)
								GPIO.output(buzzer, True)
								time.sleep(0.5)
								GPIO.output(buzzer, False)
								time.sleep(0.3)
								GPIO.output(buzzer, True)
								time.sleep(0.8)
								GPIO.output(buzzer, False)
								time.sleep(1)
	#							num_restart=1
	#							print(num_restart)
	#	print(num_restart)
	#	if(num_restart==1):
	#		print("CORRECTO")
	#		sys.exit()
	#		break

		while(True):

			time.sleep(0.3)

			lcd.lcd_display_string("Memorice",1,1)

			num_colores=start()

			introducir=True

			num_bot=0

			lcd.lcd_clear()

			lcd.lcd_display_string("Su turno",1,1)

			time.sleep(0.3)

			while(introducir):

				ok=True

				r=GPIO.input(botonR)
				v=GPIO.input(botonV)
				a=GPIO.input(botonA)
				b=GPIO.input(botonB)

				if r:
#					lcd.lcd_clear()
			#		pr("rojo")
					GPIO.output(rojoU, True)
					lcd.lcd_display_string("Rojo",1,1)
					GPIO.output(buzzer, True)
					time.sleep(0.5)
					GPIO.output(buzzer, False)
					GPIO.output(rojoU, False)

					if(colores[num_bot]!=0):
						print("DENTRO")
						mal() #delete()
						colores=[]
						num_bot=0
						num_colores=-1
						introducir=False
						ok=False

					if(num_bot!=num_colores):
						num_bot+=1
					else:
						if(ok):
							bien()
							introducir=False
				if v:
#					lcd.lcd_clear()
			#	pr("verde")
					GPIO.output(verdeU, True)
					lcd.lcd_display_string("Verde",1,1)
					GPIO.output(buzzer, True)
					time.sleep(0.5)
					GPIO.output(buzzer, False)
					GPIO.output(verdeU, False)

					if(colores[num_bot]!=1):
						mal() #delete()
						colores=[]
						num_bot=0
						num_colores=-1
						introducir=False
						ok=False

					if(num_bot!=num_colores):
						num_bot+=1
					else:
						if(ok):
							bien()
							introducir=False
				if a:
#					lcd.lcd_clear()
				#	pr("amarillo")
					GPIO.output(amarilloU, True)
					lcd.lcd_display_string("Amarillo",1,1)
					GPIO.output(buzzer, True)
					time.sleep(0.5)
					GPIO.output(buzzer, False)
					GPIO.output(amarilloU, False)

					if(colores[num_bot]!=2):
						mal() #delete()
						colores=[]
						num_bot=0
						num_colores=-1
						introducir=False
						ok=False

					if(num_bot!=num_colores):
						num_bot+=1
					else:
						if(ok):
							bien()
							introducir=False
				if b:
#					lcd.lcd_clear()
				#	pr("blanco")
					GPIO.output(blancoU, True)
					lcd.lcd_display_string("Blanco",1,1)
					GPIO.output(buzzer, True)
					time.sleep(0.5)
					GPIO.output(buzzer, False)
					GPIO.output(blancoU, False)

					if(colores[num_bot]!=3):
						mal() #delete()
						colores=[]
						num_bot=0
						num_colores=-1
						introducir=False
						ok=False

					if(num_bot!=num_colores):
						num_bot+=1
					else:
						if(ok):
							bien()
							introducir=False

				rest=GPIO.input(reset)
				if(rest==1):
					time.sleep(5)
					rest=GPIO.input(reset)
					if(rest==1):
						lcd.lcd_display_string("RECONFIGURANDO",1)
						time.sleep(1.5)
						restart()
						sys.exit()

	#	num_restart=1
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
	lcd.lcd_clear()
