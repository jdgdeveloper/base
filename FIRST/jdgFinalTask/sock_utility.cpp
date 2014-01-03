#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <string.h>
#include <ioLib.h>
#include <ctype.h>
#include <sockLib.h>

#define MAXLINE 512


/***************************************************************************/
/***************************************************************************/
int
readn (int fd, char *ptr, int nbytes)
{
  int           nleft,
                nread;

  nleft = nbytes;
  while (nleft > 0)
  {
    nread = read (fd, ptr, nleft);
    if (nread < 0)
      return (nread);
    else if (nread == 0)
      break;

    nleft -= nread;
    ptr += nread;
  }
  return (nbytes - nleft);
}

/***************************************************************************/
/***************************************************************************/
int
writen (int fd, char *ptr, int nbytes)
{
  int           nleft,
                nwritten;

  nleft = nbytes;
  while (nleft > 0)
  {
    nwritten = write (fd, ptr, nleft);
    if (nwritten <= 0)
      return (nwritten);

    nleft -= nwritten;
    ptr += nwritten;
  }
  return (nbytes - nleft);
}

/***************************************************************************/
/***************************************************************************/
int
readline (int fd, char *ptr, int maxlen)
{
  int           n,
                rc;
  char          c;

  for (n = 1; n < maxlen; n++)
  {
    if ((rc = read (fd, &c, 1)) == 1)
    {
      *ptr++ = c;
      if (c == '\n')
	break;
    }
    else if (rc == 0)
    {
      if (n == 1)
	return (0);
      else
	break;
    }
    else
    {
      return (-1);
    }
  }

  *ptr = 0;
  return (n);

}


/***************************************************************************/
/***************************************************************************/
int
str_echo (int sockfd)

{
  int           n,
                i;
  char          line[MAXLINE];

  for (;;)
  {
    n = readline (sockfd, line, MAXLINE);
    if (n == 0)
      return (0);
    else if (n < 0)
    {
      printf ("str_echo: readline error");
      return(-1);
    }

    printf ("received:%s",line);
    for (i = 0; i < n; i++)
    {
      if (isupper (line[i]))
	line[i] = tolower (line[i]);
      else
	line[i] = toupper (line[i]);
    }

    if (writen (sockfd, line, n) != n)
    {
      printf ("str_echo: writen error");
      return(-1);
    }

  }
}

/***************************************************************************/
/***************************************************************************/
int
str_cli (FILE *fp, int sockfd)
{
  int           n;
  char          sendline[MAXLINE],
                recvline[MAXLINE + 1];

  printf ("START ENTERING STRINGS\n");
  while (fgets (sendline, MAXLINE, fp) != NULL)
  {
    n = strlen (sendline);
    if (writen (sockfd, sendline, n) != n)
    {
      printf ("str_cli: writen error on socket");
      return (-1);
    }

    n = readline (sockfd, recvline, MAXLINE);
    if (n < 0)
    {
      printf ("str_cli: readline error");
      return (-1);
    }
    recvline[n] = 0;
    fputs (recvline, stdout);
  }
  if (ferror (fp))
  {
    printf ("str_cli: error reading file");
    return (-1);
  }
  return (0);
}

/***************************************************************************/
/***************************************************************************/
int
dg_echo (int sockfd, struct sockaddr *pcli_addr, int maxclilen)
{
  int           n;
  int              clilen;
  char          mesg[MAXLINE];

  for (;;)
  {
    clilen = maxclilen;
    n = recvfrom (sockfd, mesg, MAXLINE, 0, pcli_addr, &clilen);
    if (n < 0)
    {
      printf ("dg_echo: recvfrom error");
      return (-1);
    }
    mesg[n] = 0;
    printf ("RECVFROM: %s\n", mesg);

    if (sendto (sockfd, mesg, n, 0, pcli_addr, clilen) != n)
    {
      printf ("dg_echo: sendto error");
      return(-1);
    }
  }
}

/***************************************************************************/
/***************************************************************************/
int
dg_cli (FILE *fp, int sockfd, struct sockaddr *pserv_addr, int servlen)
{
  int           n;
  unsigned int              slen;
  char          sendline[MAXLINE],
                recvline[MAXLINE + 1];

  slen = servlen;

  printf ("START ENTERING STRINGS\n");
  while (fgets (sendline, MAXLINE, fp) != NULL)
  {
    n = strlen (sendline);
    if (sendto (sockfd, sendline, n, 0, pserv_addr, servlen) != n)
    {
      printf ("dg_cli: sendto error on socket");
      return (-1);
    }

    n = recvfrom (sockfd, recvline, MAXLINE, 0,
		  (struct sockaddr *) pserv_addr, (int *) &slen);
    if (n < 0)
    {
      printf ("dg_cli: recvfrom error");
      return(-1);
    }
    recvline[n] = 0;
    fputs (recvline, stdout);
  }

  if (ferror (fp))
  {
    printf ("dg_cli: error reading file");
    return (-1);
  }
  return (0);
}

/***************************************************************************/
/***************************************************************************/
