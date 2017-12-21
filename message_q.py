import sysv_ipc


mq = sysv_ipc.MessageQueue(1234566, sysv_ipc.IPC_CREX) 

message = mq.receive()
print message
