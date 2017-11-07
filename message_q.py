import sysv_ipc


mq = sysv_ipc.MessageQueue(12345, sysv_ipc.IPC_CREX)
 
print "ERROR: message queue creation failed"


 
message = mq.receive()
print message
