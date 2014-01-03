
/***************************************************************************/
/***************************************************************************/

#include	<stdio.h>
#include	<stdlib.h>
#include	<ctype.h>
#include	<errno.h>
#include	<string.h>
#include	<stdarg.h>
void print_err ();

#ifndef  CLIENT

#ifndef SERVER
#define CLIENT 1		/* default to client */
#endif

#endif

#ifndef NULL
#define NULL ((void *)0)
#endif

char           *pname = NULL;

/***************************************************************************/

#ifdef CLIENT
/***************************************************************************/
//print_err ();

/***************************************************************************/
/***************************************************************************/
void
err_quit (char *fmt, ...)
{
    va_list         args;

    va_start (args, fmt);
    if (pname != NULL)
	fprintf (stderr, "%s ", pname);
    vfprintf (stderr, fmt, args);
    fputc ('\n', stderr);
    va_end (args);

    exit (1);
}

/***************************************************************************/
/***************************************************************************/
void
err_sys (char *fmt, ...)
{
    va_list         args;

    va_start (args, fmt);
    if (pname != NULL)
	fprintf (stderr, "%s ", pname);
    vfprintf (stderr, fmt, args);
    va_end (args);

    print_err ();

    exit (1);
}

/***************************************************************************/
/***************************************************************************/
void
err_ret (char *fmt, ...)
{
    va_list         args;

    va_start (args, fmt);
    if (pname != NULL)
	fprintf (stderr, "%s ", pname);
    vfprintf (stderr, fmt, args);
    va_end (args);

    print_err ();

    fflush (stdout);
    fflush (stderr);

    return;
}

/***************************************************************************/
/***************************************************************************/
void
err_dump (char *fmt, ...)
{
    va_list         args;

    va_start (args, fmt);
    if (pname != NULL)
	fprintf (stderr, "%s ", pname);
    fmt = va_arg (args, char *);
    vfprintf (stderr, fmt, args);
    va_end (args);

    print_err ();

    fflush (stdout);
    fflush (stderr);

    abort ();
    exit (1);
}


/***************************************************************************/
/***************************************************************************/
void
print_err ()
{

  fprintf (stderr, " >>> %s\n", strerror(errno));

}

#endif				/* CLIENT */


/***************************************************************************/

#ifdef SERVER
/***************************************************************************/
#define LOGERRORS
#ifdef LOGERRORS
/* Messages will be logged by the LOG DAEMON
 * The error message is put in /var/adm/messages
 */
#include	<syslog.h>
#else
#define syslog(a,b)	fprintf (stderr, "%s\n", (b))
#define	openlog(a,b,c)	fprintf (stderr, "%s\n", (a))
#endif
char            emesgstr[255] = {0};


/***************************************************************************/
/***************************************************************************/
err_init (ident)
char           *ident;
{
    openlog (ident, (LOG_PID | LOG_CONS), LOG_DAEMON);
}

/***************************************************************************/
/***************************************************************************/
err_quit (char *fmt, ...)
{
    va_list         args;

    va_start (args, fmt);
    vsprintf (emesgstr, fmt, args);
    va_end (args);

    syslog (LOG_ERR, emesgstr);

    exit (1);
}

/***************************************************************************/
/***************************************************************************/
err_sys (char *fmt, ...)
{
    va_list         args;

    va_start (args, fmt);
    vsprintf (emesgstr, fmt, args);
    va_end (args);

    print_err ();
    syslog (LOG_ERR, emesgstr);

    exit (1);
}

/***************************************************************************/
/***************************************************************************/
err_ret (char *fmt, ...)
{
    va_list         args;

    va_start (args, fmt);
    fmt = va_arg (args, char *);
    vsprintf (emesgstr, fmt, args);
    va_end (args);

    print_err ();
    syslog (LOG_ERR, emesgstr);

    return;
}

/***************************************************************************/
/***************************************************************************/
err_dump (char *fmt, ...)
{
    va_list         args;

    va_start (args, fmt);
    fmt = va_arg (args, char *);
    vsprintf (emesgstr, fmt, args);
    va_end (args);

    print_err ();
    syslog (LOG_ERR, emesgstr);

    abort ();
    exit (1);
}

/***************************************************************************/
/***************************************************************************/
print_err ()
{
    register int    len;

    len = strlen (emesgstr);
    sprintf (emesgstr + len, " >>> %s\n", strerror(errno));
}

#endif				/* SERVER */
