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