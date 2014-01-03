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
#include "lib_socket.h"
#include "BaeUtilities.h"
#include "AxisCamera.h" 
#include "TrackAPI.h" 
#include "FrcError.h"
#include "Utility.h"
#include "WPILib.h"
#include <taskLib.h>

#define _define_storage_
#include "jdgGlobal.h"


int processSocket (int fd);

/******************************************************************************
**  Routine Name : main
**
**  Purpose      :
**
**  Returns      :
******************************************************************************/
int
main ()
{
  int           sockfd,
                newsockfd;

  sockfd = LIB_SOCKET_server_setup (NULL, "50000", "inet");

  printf ("SOCKET:%d\n",sockfd);
  if (sockfd == -1) exit (0);

  for (;;)
  {
    newsockfd = LIB_SOCKET_server_accept (sockfd);

    processSocket (newsockfd);

    close (newsockfd);
  }

}


/******************************************************************************
**  Routine Name : processSocket
**
**  Purpose      :
**
**  Returns      :
******************************************************************************/
int
processSocket (int fd)
{
  static int    count = 0;
  char input[256];
  char  output[256];
  char command[256];
  int outputFlag = 0;
  char parameterStr[256];
  fd_set select_list,select_buffer;
  int select_value;
  int imageSize;
  Image* cameraImage;
  double currentTimestamp;
  double lastTimestamp=0.0;
  char* imageName = "crio.png";   // this directory must exist on the cRIO


  printf ("SERVER: processImageSocket (%d)\n", fd);
  
  /* allow writing to vxWorks target */
  Priv_SetWriteFileAllowed(1);   		
 
  if (StartCameraTask(10, 0, k640x480, ROT_0) == -1) {
		printf( "Failed to spawn camera task; exiting. Error code %s", 
				GetVisionErrorText(GetLastVisionError()) );
	}
 
  FD_ZERO (&select_list);
  FD_SET (fd, &select_list);
  for (;;)
  {
    bcopy ((const char *)&select_list, (char *)&select_buffer, sizeof(select_list));
#if defined CRIO
    if ((select_value = select (FD_SETSIZE, &select_buffer, NULL, NULL, NULL)) < 0)
#else
    if ((select_value = select (getdtablesize(), &select_buffer, NULL, NULL, NULL)) < 0)
#endif
    {
      if (errno == EINTR)
        continue;
      else
        return (0);
    }
    if (select_value == 0) continue;

    if (FD_ISSET (fd, &select_buffer))
    {
      memset (input, 0, sizeof(input));
      if ((count = LIB_SOCK_UTIL_readline (fd, input, sizeof(input)-1)) <= 0) return (0);
      
      
      if (input[0] == 'q' || input[0] == 'Q') {
              return(-1);
      } else if (input[0] == 'h' || input[0] == 'H') {
          strcpy (output, "HELP MENU\n*****************\n\r");
          strcat (output," [h|H] prints Help menu\n\r");
          strcat (output," [s|S] displays system status\n\r");
          strcat (output," [t|T] toggles output flag\n\r");
          strcat (output," [p|P] sets a useless parameter\n\r");
          strcat (output," [i|I] generates an imageFile (FTP)\n\r");
          strcat (output," [q|Q] Quits\n\r");
          LIB_SOCKET_write (fd, output, strlen (output));
      } else if (input[0] == 's' || input[0] == 'S') {
          strcpy (output, "Status to follow:\n\r*****************\n\r");
          LIB_SOCKET_write (fd, output, strlen (output));
          sprintf (output, "Parameter:%d\n\r", parameter);
          LIB_SOCKET_write (fd, output, strlen (output));
          sprintf (output, "frameCount:%d\n\r", frameCount);
          LIB_SOCKET_write (fd, output, strlen (output));
      } else if (input[0] == 't' || input[0] == 'T') {
          if (outputFlag)
        	  outputFlag = 0;
          else
        	  outputFlag = 1;
      } else if (input[0] == 'p' || input[0] == 'P') {
          memset (command, 0, sizeof (command));
          memset (parameterStr, 0, sizeof (parameterStr));
          count = sscanf (input, "%s %s", command, parameterStr);
          if (count == 2)
          {
            parameter = atoi (parameterStr);
          }
      } else if (input[0] == 'i' || input[0] == 'I') {
    	while (1) {
    	/* Generate an image */
		  cameraImage = frcCreateImage(IMAQ_IMAGE_HSL);

  		  if ( !GetImageBlocking (cameraImage,&currentTimestamp,lastTimestamp) ) {
  			printf ("Camera Acquisition FAILED %i\n", GetLastVisionError());
  			frcDispose(cameraImage);
            sprintf (output, "%s\n", "FAILED");
            if (!LIB_SOCKET_write (fd, output, strlen (output))) return (0);
  			WaitSec(1.0);
  			break;
  		  } else { 
  			printf ("Camera Acquisition TOOK IMAGE TS:%lf\n",currentTimestamp);
  			lastTimestamp = currentTimestamp;
  			
			if (!frcWriteImage(cameraImage, imageName) ) { 
					printf ("frcWriteImage failed\n");
			} else { 
				  	//printf ("Saved image to %s\n", imageName);	
					frcDispose(cameraImage);
			}

            sprintf (output, "%s\n", "crio.png");
            if (!LIB_SOCKET_write (fd, output, strlen (output))) return (0);
            frameCount++;
            break;
  		  }
    	}
      } 
      if (outputFlag) {
        strcpy (output, "\n>>");
        LIB_SOCKET_write (fd, output, strlen (output));
      }
    }

  }

}


#if 0
int
processImageSocketFirstPull (int fd)
{
  char  output[256];
  char* imageName = "/pics/crio.png";   // this directory must exist on the cRIO
  int imageSize;
  Image* cameraImage;
  double currentTimestamp;
  double lastTimestamp=0.0;

  printf ("SERVER: processImageSocket (%d)\n", fd);
  
  /* start the CameraTask	 */
	
  if (StartCameraTask(10, 0, k640x480, ROT_180) == -1) {
		printf( "Failed to spawn camera task; exiting. Error code %s", 
				GetVisionErrorText(GetLastVisionError()) );
	}


  for (;;)
  {
        cameraImage = frcCreateImage(IMAQ_IMAGE_HSL);
        //GetImageDataBlocking(char** imageData, int* numBytes, double* timestamp, double lastImageTimestamp);
		if ( !GetImageDataBlocking ((char **)&cameraImage,&imageSize,&currentTimestamp, lastTimestamp) ) {
			printf ("Camera Acquisition FAILED %i\n", GetLastVisionError());
		} else { 
			printf ("Camera Acquisition TOOK IMAGE TS:%lf SIZE:%d\n",currentTimestamp, imageSize);
			lastTimestamp = currentTimestamp;
			/*
			sprintf (output, "%d", imageSize);
			printf ("LEN:%s\n\r",output);
			if (!LIB_SOCKET_write(fd, output, strlen(output)))
			{
				printf ("SERVER: DISCONNECTED\n");
				return (-1);
			}
			
			WaitSec( 1.0 );
			*/
			  if (!frcWriteImage(cameraImage, imageName) ) { 
					printf ("frcWriteImage failed\n");
			  } else { 
				  	printf ("\nSaved image to %s", imageName);	
			  }
/*
			if (!LIB_SOCKET_write (fd, (char *)cameraImage, imageSize))
			{
		    	printf ("SERVER: processImageSocket (%d) EXITING\n", fd);
		   	    return (-1);	
			}
*/		
			
		}

	  frcDispose(cameraImage);
	  
      WaitSec( 1.0 );
  }

}
#endif


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
	main();
}

/**
 * This is the main program that is run by the debugger or the robot on boot.
 **/
int jdgTask_StartupLibraryInit(void)
	{
		RunProgram();
		return 0;
	}

#endif
