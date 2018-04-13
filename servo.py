def main():   
    #Import functions
    import measure, move
    import time
    import RPi.GPIO as GPIO
    #Declare Variables
    Servo_pin = 35
    angle = 45
    freq = 50
    #Setup board
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Servo_pin, GPIO.OUT)
    servo = GPIO.PWM(Servo_pin,freq)
    #Determine Duty Cycle
    dc = 1/18 * (angle) + 2
    print("Starting Duty Cycle: ",dc)
    #Start servo
    servo.start(dc)

    i = 1
    #Determine angle based on previous angle
    while True:
        if (i == 0):
            angle = 45
        elif (i == 1):
            angle = 90
        elif (i == 2):
            angle = 180
        elif (i > 2):
            angle = 45
            i = 0
        i = i+1
        #Change servo's position
        #Convert angle to Duty Cycle
        dc = 1/18 * (angle) + 2
        print("Setting Duty Cycle: ",dc)
        #Change position
        servo.ChangeDutyCycle(dc)
        #Give servo time to finish moving
        time.sleep(0.3)    
main()
