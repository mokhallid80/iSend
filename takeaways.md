# Takeaways

### Response Types (in case of TCP)

1. SA (TCP Flag) => Successful Ack.
2. RA (TCP Flag) => Unsuccessful Ack. Happens when we try to send a packet to a port that nothing listens to it.
3. No Response => When we exceed the timeout in the rs1 function.