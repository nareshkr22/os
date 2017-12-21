#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>

int main(int argc, const char **argv)
{
   int shmid; 
   key_t key = 123456;
   char *shared_memory; 
   if ((shmid = shmget(key, 60, IPC_CREAT | 0666)) < 0)
   {
 
      printf("Error getting shared memory id");
      exit(1);
   }
   // Attached shared memory
   if ((shared_memory = shmat(shmid, NULL, 0)) == (char *) -1)
   {
 
      printf("Error attaching shared memory id");
      exit(1);
   } 
	    
   memcpy(shared_memory, "Content From shared mem:", sizeof("Content From shared mem"));
   // sleep so there is enough time to run he reader!
   sleep(10);
   // Detach and remove shared memory
   shmdt(&shmid);
   shmctl(shmid, IPC_RMID, NULL);
}
