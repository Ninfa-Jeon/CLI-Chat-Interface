# CLI-Chat-Interface

A single-server multi-client CLI chat interface that can be used for exchanging text messages as well as run system commands.

### Working

 * Run the __RunMeFirst.py__ file before anything to generate the private and public keys
 * The client text messages and system commands(linux) are randomly selected from the __message.txt__ file
 * The server responses to text messages have to be __manually__ made by a worker while the system commands are run
   __automatically__ by the server and need no assistance of any sort.
 * After a maximum of 4 client messages, the client disconnects __automatically__ to let the other clients in queue connect
   to the server.
 * There is message logging for server and clients separately which also records the date and time of interaction.
 * If system commands are sent by the clients, the server makes sure to relay __ACK__ and __NOACK__ messages back to 
   the client.
 * All messages and commands relayed are __RSA__ encrypted.
