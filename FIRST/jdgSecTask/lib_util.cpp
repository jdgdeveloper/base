/******************************************************************************
**
**  Name : lib_util.c
**
**  Description : LIB_UTIL component utility file
**
**  Routines:
**           LIB_UTIL_error_return (va_alist) - report system error and return
**           LIB_UTIL_error_exit   (va_alist) - report system error and exit
**           LIB_UTIL_print_error  ()         - output the system error
**
**
******************************************************************************/
/*****************************************************************************/
#include	<stdio.h>
#include	<stdlib.h>
#include	<errno.h>
#include	<stdarg.h>
#include	<math.h>
//#include	<sys/file.h>
#include	<sys/types.h>
#include	<sys/stat.h>
#include	<sys/ioctl.h>
//#include	<sys/time.h>
#include <string.h>
#include "lib_util.h"


/******************************************************************************
**  Routine Name : LIB_UTIL_error_return
**
**  Purpose      : Print the input string, the system error message and
**                 return to the calling routine
**
**  Returns      : None
******************************************************************************/
void LIB_UTIL_error_return (char *fmt, ...)
{
  va_list       args;		/* Variable list */

 /*
    Retrieve the format string from the variable arguments and print the
    contents to the standard error device
 */
  va_start (args, fmt);
  vfprintf (stderr, fmt, args);
  va_end (args);

 /*
    Print the system errno and the associated error string to the stderr device
 */
  LIB_UTIL_print_error ();

 /*
    Flush the standard output device and standard error device
 */
  fflush (stdout);
  fflush (stderr);

 /*
    Return to the calling routine
 */
  return;

}


/******************************************************************************
**  Routine Name : LIB_UTIL_error_exit
**
**  Purpose      : Print the input string, the system error message and
**                 perform a process exit
**
**  Returns      : None
******************************************************************************/
void LIB_UTIL_error_exit (char *fmt, ...)
{
  va_list       args;		/* Variable list */

 /*
    Retrieve the format string from the variable arguments and print the
    contents to the standard error device
 */
  va_start (args, fmt);
  vfprintf (stderr, fmt, args);
  va_end (args);

 /*
    Print the system errno and the associated error string to the stderr device
 */
  LIB_UTIL_print_error ();

 /*
    Exit the process
 */
  exit (1);

}


/******************************************************************************
**  Routine Name : LIB_UTIL_print_error
**
**  Purpose      : Print the system errno and errno string
**                 to the standard error device
**
**  Returns      : None
******************************************************************************/
void LIB_UTIL_print_error ()
{

  fprintf (stderr, " >>> %s\n", strerror(errno));

  fflush (stderr);
}
