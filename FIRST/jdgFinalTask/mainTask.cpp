
#define CRIO
#include <stdio.h>
#include <string.h>
//#include <sys/file.h>
//#include <sys/time.h>
#include <sys/resource.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
//#include <sys/ipc.h>
//#include <sys/shm.h>
#include <sys/wait.h>
#include <errno.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/un.h>
#include <net/if.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <dirent.h>
#if defined CRIO
#include <ioLib.h>
#include <selectLib.h>
#endif
#include "libSocket.h"
#include "BaeUtilities.h"
#include "AxisCamera.h" 
#include "TrackAPI.h" 
#include "FrcError.h"
#include "Utility.h"
#include "WPILib.h"
#include <taskLib.h>
#include "telnetServer.h"

#define _define_storage_
#include "mainGlobal.h"


#if defined CRIO

/**
*  Routine Name:	: RunProgram
*  Description 		: Start point of the program
*  Returns			: n/a
*  Parameters		: n/a
* 
*/
void RunProgram(void)
{
	int taskID;
	int portNumber;
	
	memset ((void *)&globalData, 0, sizeof(globalData));
	
	//telnetServer("50000");
	portNumber = 50000;
	taskID = taskSpawn("telnetServer",
					100,							// priority
					VX_FP_TASK,						// floating point C++ context save
					64000,							// stack size
					(FUNCPTR) telnetServer,			// function to be called
                    portNumber,						// port number
                    0,0,0,0,0,0,0,0,0);				// parameters (unused)
	
	portNumber = 50001;
	taskID = taskSpawn("telnetServer",
					100,							// priority
					VX_FP_TASK,						// floating point C++ context save
					64000,							// stack size
					(FUNCPTR) telnetServer,			// function to be called
                    portNumber,						// port number
                    0,0,0,0,0,0,0,0,0);				// parameters (unused)

}

/**
 * This is the main program that is run by the debugger or the robot on boot.
 **/
int jdgFinalTask_StartupLibraryInit(void)
	{
		RunProgram();
		return 0;
	}

#endif
