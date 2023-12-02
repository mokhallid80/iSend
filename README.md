# iSend
Very simple script in my journey for learning important security tools in Python. The purpose of iSend is to create, send and inspect packets.

## Techs
1. Spacy (To create, send and inspect packets).
2. venv (To create a Python virtual env).
3. yaml (To read a .yaml config file).

## Takeaways
### Response Types (in case of TCP)

1. SA (TCP Flag) => Successful Ack.
2. RA (TCP Flag) => Unsuccessful Ack. Happens when we try to send a packet to a port that nothing listens to it.
3. No Response => When we exceed the timeout in the rs1 function.


## Output Demo
![Output Demo](https://github.com/mokhallid80/iSend/blob/master/demo_images/demo_output.png)
