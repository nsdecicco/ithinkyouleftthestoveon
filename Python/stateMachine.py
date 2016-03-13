class StateMachine:
#stove, door, window, door2, door3, fridge - S1,2,3,4,5,6
	SW_ENGAGED=0
	SW_DISENGAGED=1
	
	stovemsgE = "The Stove is on!!"
	stovemsgD = "The Stove is off."
	
	doormsgE = "The Front Door is unlocked!!"
	doormsgD = "The Front Door is locked."
	
	windowmsgE = "The Window is ajar!!"
	windowmsgD = "The Window is closed."
	
	door2msgE = "The Door 2 is unlocked!!"
	door2msgD = "The Door 2 is locked."
	
	door3msgE = "The Door 3 is unlocked!!"
	door3msgD = "The Door 3 is locked."
	
	fridgemsgE = "The Refrigerator is currently running!! You better go catch it!"
	fridgemsgD = "The Refridgerator is currently chilling."
	
	HAVE_CONNECTION=2
	LOST_CONNETION=4
	state=0
	stovePin=None
	doorPin=None
	windowPin=None
	door2Pin=None
	door3Pin=None
	fridgePin=None
	
	

	def __init__(self):
		stovePin = mraa.Gpio(2)
		stovePin.dir(mraa.DIR_IN) # stove input
		doorPin = mraa.Gpio(4)
		doorPin.dir(mraa.DIR_IN) # door input
		windowPin = mraa.Gpio(7)
		windowPin.dir(mraa.DIR_IN) # window input
		
		door2Pin = mraa.Gpio(8)
		door2Pin.dir(mraa.DIR_IN) # stove input
		door3Pin = mraa.Gpio(12)
		door3Pin.dir(mraa.DIR_IN) # door input
		fridgePin = mraa.Gpio(13)
		fridgePin.dir(mraa.DIR_IN) # window input
		
		updateState(self)

	def updateState(self):
		# poll pins
		# # if stovePin.read():
			# # self.state |= self.STOVE_IS_ON
		# # else
			# # self.state &= ~self.STOVE_IS_ON
		
		# # if doorPin.read():
			# # self.state |= self.STOVE_IS_ON
		# # else
			# # self.state &= ~self.STOVE_IS_ON		
			
			
		# maybe determine if the user is still around here as well
		if self.state & self.LOST_CONNECTION:
		#build the message to be e-mailed
			self.message = ""
			if self.stovePin.read() & self.SW_ENGAGED:
				self.message += self.stovemsgE
			else
				self.message += self.stovemsgD
				
			if self.doorPin.read() & self.SW_ENGAGED:
				self.message += self.doormsgE
			else
				self.message += self.doormsgD
				
			if self.windowPin.read() & self.SW_ENGAGED:
				self.message += self.windowmsgE
			else
				self.message += self.windowmsgD
				
			if self.door2Pin.read() & self.SW_ENGAGED:
				self.message += self.door2msgE
			else
				self.message += self.door2msgD
				
			if self.door3Pin.read() & self.SW_ENGAGED:
				self.message += self.door3msgE
			else
				self.message += self.door3msgD
				
			if self.fridgePin.read() & self.SW_ENGAGED:
				self.message += self.fridgemsgE
			else
				self.message += self.fridgemsgD
				# send e-mail
			
		


		
		
		
stateMachine = StateMachine()


while True:
	stateMachine.updateState()
