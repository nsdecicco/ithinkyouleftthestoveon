class StateMachine:
	STOVE_IS_ON=0
	STOVE_IS_OFF=1
	
	HAVE_CONNECTION=2
	LOST_CONNETION=4
	state=0
	stovePin=None

	def __init__(self):
		stovePin = mraa.Gpio(pin number)
		stovePin. # make this guy an input
		updateState(self)

	def updateState(self):
		# poll pins
		if stovePin.read():
			self.state |= self.STOVE_IS_ON
		else
			self.state &= ~self.STOVE_IS_ON
		# maybe determine if the user is still around here as well
		if self.state & self.STOVE_IS_ON:
			if self.state & self.LOST_CONNECTION:
				# send e-mail


stateMachine = StateMachine()


while True:
	stateMachine.updateState()
