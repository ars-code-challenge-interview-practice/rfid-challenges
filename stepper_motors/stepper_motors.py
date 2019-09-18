"""
You're implementing a test framework that needs to control several different brands of stepper motors. All the motors have this in common

o    You connect to it via ssh over a socket

o    You control it by sending text commands over that socket

These are the methods that you'll need to implement

o    connect --> takes an IP address, pwd and uname. This is the same implementation for all motors

o    disconnect --> no params, same for all motors too.

o    accelerate_to_speed --> takes one integer and uses the motor protocol

o    stop-> no parameters, also uses the motor protocol

The tricky part here is that each motor has a different protocol. The commands you send over the socket to accelerate, and stop on motor 'a' is different than on motor 'b' and so on.

The goal here isn't to implement a working solution, you can 'stub' out the calls into stepper motor protocols with commented out pseudo code. What we're looking for is enough code and inline comments to show the design that you'd use for this situation.

One last thing. Implement a check that raises an exception anytime a command is called before connect has been called.
"""

# Full disclosure - I'm having trouble visualizing about how to even start this challenge. I'm very unfamiliar with SSH and sockets. As I understand it, SSH mainly happens in the terminal. Since I'm entirely unfamiliar with what goes into the motor protocols, I'm not sure what to have the code look for and handle. I have my understanding of what each method should do is below.

def connect(ip, pwd, uname):
    # it should verify that the username and password match, and are authorized to be on the ip address. After it finishes with that, it needs to communicate with the socket.  After that, I'm not sure what it needs to do, or the steps it will need to take to finish connecting.
    pass

def disconnect():
    # checks for connection. Will have to tell the socket to disconnect. It probably involves telling the motors to stop communicating with the socket. Unsure how this will be accomplished.
    pass

def accelerate_to_speed(int):
    # checks for connection. Takes in the integer over over text command. Assuming the motors have some way to handle speed, it should replace the speed for those motors with the integer.
    pass

def stop():
    # checks for connection.  Sets accelerate_to_speed to 0. Takes in motor protocols as variables.
    pass