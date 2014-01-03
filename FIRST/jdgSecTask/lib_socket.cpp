#define CRIO
/******************************************************************************
**
**  Name : lib_socket.c
**
**  Description :  A library of interprocess communication routines to aid
**                 in the use of socket based communication.
**
**
******************************************************************************/
/*****************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <netdb.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <strings.h>
#if defined CRIO
#include <strLib.h>
#include <hostLib.h>
#include <sockLib.h>
#include <ctype.h>
#endif
#include "lib_socket.h"
#include "lib_util.h"

#define LIB_SOCK_PRINTERR	if (1) printf
#define LIB_SOCK_MAXPCONN	5
#define LIB_SOCK_MAXSTR	1024


/******************************************************************************
**  Routine Name : LIB_SOCKET_client_setup
**
**  Purpose      : Initiate a connection to a specified port and host.
**
**                 RESTRICTIONS: Service name must be defined in
**                               /etc/service for "inet" family.
**                               Family name (if used) must be defined
**                               in /etc/hosts.
**
**  Returns      : - Socket descriptor of established connection.
**                 - Value of less than zero indicates error.
******************************************************************************/
int LIB_SOCKET_client_setup (char *host_name,char *service_name,char *family_name)
{
  int           flag = 1;	/* TCP_NODELAY flag value */
  char          hostbuffer[LIB_SOCK_MAXSTR];	/* Buffer to hold host name */
  int           socket_fd;	/* socket descriptor of connection */
  struct sockaddr_in client_in;	/* socket parameter structure */
  struct sockaddr_un client_un;	/* socket parameter structure */
  struct hostent *hostent;	/* pointer to host information */
  struct servent *servent;
  int portNumber;


 /* Check for valid input parameters */
  if (family_name == NULL)
    return (-1);

  if (!strcasecmp (family_name, "unix"))
  {
  /* Name socket */
    memset ((char *) &client_un, 0, sizeof (client_un));
    client_un.sun_family = PF_UNIX;
    strcpy (client_un.sun_path, "/tmp/");
    strcat (client_un.sun_path, service_name);

  /* Create socket */
    if ((socket_fd = socket (client_un.sun_family, SOCK_STREAM, 0)) < 0)
    {
      LIB_SOCK_PRINTERR ("LIB_SOCKET_client_setup: socket() error");
      return (-1);
    }

  /* Connect socket */
    if (connect (socket_fd, (struct sockaddr *) &client_un,
		 sizeof (client_un)) < 0)
    {
      LIB_SOCK_PRINTERR ("LIB_SOCKET_client_setup: connect() error");
      LIB_SOCKET_disconnect (socket_fd);
      return (-1);
    }
  }

  else
  {
    if (host_name == NULL)
    {
    /* If host name is not specified, then get local hostname */
      if ((gethostname (hostbuffer, sizeof (hostbuffer))) == -1)
      {
	LIB_SOCK_PRINTERR ("LIB_SOCKET_client_setup: gethostname() error");
	return (-1);
      }
      host_name = hostbuffer;
    }

    if ((hostent = gethostbyname (host_name)) == NULL)
    {
      LIB_SOCK_PRINTERR ("LIB_SOCKET_client_setup: gethostbyname() error");
      return (-1);
    }

  /* Service name must be specified, otherwise an error exists */
    if (service_name == NULL)
      return (-1);

  /* Get port number */
#if !defined CRIO
    setservent (0);
#endif
    if (!isdigit(service_name[0])) {
      if ((servent = getservbyname (service_name, NULL)) == NULL)
      {
        LIB_SOCK_PRINTERR ("LIB_SOCKET_client_setup: getservbyname() error");
        return (-1);
      }
    } else {
      servent = NULL;
      portNumber = htons(atoi(service_name));
    }
#if !defined CRIO
    endservent ();
#endif
  /* Name socket */
    memset ((char *) &client_in, 0, sizeof (client_in));
    client_in.sin_family = PF_INET;
    memcpy (&client_in.sin_addr, hostent->h_addr, hostent->h_length);
    if (servent != NULL)
      client_in.sin_port = servent->s_port;
    else
      client_in.sin_port = portNumber;

  /* Create socket */
    if ((socket_fd = socket (client_in.sin_family, SOCK_STREAM, 0)) < 0)
    {
      LIB_SOCK_PRINTERR ("LIB_SOCKET_client_setup: socket() error");
      return (-1);
    }

  /* Connect socket */
    if (connect (socket_fd, (struct sockaddr *) & client_in,
		 sizeof (client_in)) < 0)
    {
      LIB_SOCK_PRINTERR ("LIB_SOCKET_client_setup: connect() error");
      LIB_SOCKET_disconnect (socket_fd);
      return (-1);
    }
  }

  return (socket_fd);

}				/* end LIB_SOCKET_client_setup */


/******************************************************************************
**  Routine Name : LIB_SOCKET_server_setup
**
**  Purpose      : Creates a socket at the specified portnumber and listens.
**
**                 RESTRICTIONS: Service name must be defined in
**                               /etc/service for "inet" family.
**                               Family name (if used) must be defined
**                               in /etc/hosts.
**
**  Returns      : - Socket descriptor of created socket.
**                 - Value of less than zero indicates error.
******************************************************************************/
int LIB_SOCKET_server_setup (char *host_name,char *service_name,char *family_name)
{
  int           flag = 1;	/* flag value */
  int           reuse_flag;	/* reuse flag value */
  unsigned int           reuse_flag_size;/* reuse flag size */
  char          hostbuffer[LIB_SOCK_MAXSTR];	/* Buffer to hold host name */
  int           socket_fd;	/* socket descriptor of connection */
  struct sockaddr_in server_in;	/* socket parameter structure */
  struct sockaddr_un server_un;	/* socket parameter structure */
  struct hostent *hostent;	/* pointer to host information */
  struct servent *servent;
  int portNumber;


 /* Check for valid input parameters */
  if (family_name == NULL)
    return (-1);

  if (!strcasecmp (family_name, "unix"))
  {
  /* Name socket */
    memset ((char *) &server_un, 0, sizeof (server_un));
    server_un.sun_family = PF_UNIX;
    strcpy (server_un.sun_path, "/tmp/");
    strcat (server_un.sun_path, service_name);
    unlink (server_un.sun_path);

  /* Create socket */
    if ((socket_fd = socket (server_un.sun_family, SOCK_STREAM, 0)) < 0)
    {
      LIB_SOCK_PRINTERR ("LIB_SOCKET_server_setup: socket() error");
      return (-1);
    }

  /* Bind to the socket */
    if (bind (socket_fd, (struct sockaddr *)&server_un, sizeof (server_un)) < 0)
    {
      LIB_SOCK_PRINTERR ("LIB_SOCKET_server_setup: bind() error");
      LIB_SOCKET_disconnect (socket_fd);
      return (-1);
    }
  }

  else
  {
    if (host_name == NULL)
    {
      if ((gethostname (hostbuffer, sizeof (hostbuffer))) == -1)
      {
	LIB_SOCK_PRINTERR ("LIB_SOCKET_server_setup: gethostname() error");
	return (-1);
      }
      host_name = hostbuffer;
    }
#if 0
    if ((hostent = gethostbyname (host_name)) == NULL)
    {
      LIB_SOCK_PRINTERR ("LIB_SOCKET_server_setup: gethostbyname() error");
      return (-1);
    }
#endif
    if (service_name == NULL)
      return (-1);

#if !defined CRIO
    setservent (0);
#endif
    if (!isdigit(service_name[0])) {
      if ((servent = getservbyname (service_name, NULL)) == NULL)
      {
        LIB_SOCK_PRINTERR ("LIB_SOCKET_server_setup: getservbyname() error");
        return (-1);
      }
    } else {
      servent = NULL;
#if defined CRIO
      portNumber = atoi(service_name);
#else
      portNumber = htons(atoi(service_name));
#endif
    }
#if !defined CRIO
    endservent ();
#endif

  /* Name socket */
    memset ((char *) &server_in, 0, sizeof (server_in));
    server_in.sin_family = PF_INET;
    //memcpy (&server_in.sin_addr, hostent->h_addr, hostent->h_length);
    server_in.sin_addr.s_addr = htonl(INADDR_ANY);
    if (servent != NULL)
      server_in.sin_port = servent->s_port;
    else
      server_in.sin_port = portNumber;

  /* Create socket */
    if ((socket_fd = socket (server_in.sin_family, SOCK_STREAM, 0)) < 0)
    {
      LIB_SOCK_PRINTERR ("LIB_SOCKET_server_setup: socket() error");
      return (-1);
    }

  /* Bind to the socket */
    if (bind (socket_fd, (struct sockaddr *)&server_in, sizeof (server_in)) < 0)
    {
      LIB_SOCK_PRINTERR ("LIB_SOCKET_server_setup: bind() error");
      LIB_SOCKET_disconnect (socket_fd);
      return (-1);
    }
  }
#if 0
  reuse_flag_size = sizeof (reuse_flag);
  if (getsockopt (socket_fd, SOL_SOCKET, SO_REUSEADDR,
		  (char *) &reuse_flag, &reuse_flag_size) == -1)
  {
    LIB_SOCK_PRINTERR ("LIB_SOCKET_server_setup: getsockopt() error");
    LIB_SOCKET_disconnect (socket_fd);
    return (-1);
  }

  if (!reuse_flag)
  {
    if (setsockopt (socket_fd, SOL_SOCKET, SO_REUSEADDR,
		    (char *) &flag, sizeof (flag)) == -1)
    {
      LIB_SOCK_PRINTERR ("LIB_SOCKET_server_setup: setsockopt() error");
      LIB_SOCKET_disconnect (socket_fd);
      return (-1);
    }
  }
#endif
 /* Start socket listening */
  if (listen (socket_fd, LIB_SOCK_MAXPCONN) < 0)
  {
    LIB_SOCK_PRINTERR ("LIB_SOCKET_server_setup: listen() error");
    LIB_SOCKET_disconnect (socket_fd);
    return (-1);
  }

  return (socket_fd);

}				/* end LIB_SOCKET_server_setup */


/******************************************************************************
**  Routine Name : LIB_SOCKET_server_accept
**
**  Purpose      : Accept a connection at an established and listening socket.
**
**  Returns      : - Socket descriptor of accepted connection.
**                 - Value of less than zero indicates error.
******************************************************************************/
int LIB_SOCKET_server_accept (int socket_fd)
{
  int           flag = 1;	/* TCP_NODELAY flag value */
  int           new_socket_fd;	/* socket descriptor of connection */
  int           server_len;	/* length of server structure */
  struct sockaddr server;	/* socket parameter structure */


 /* Check for valid input parameters */
  if (socket_fd <= 0)
    return (-1);

  for (;;)
  {
    server_len = sizeof (server);
    if ((new_socket_fd = accept (socket_fd, &server, &server_len)) == -1)
    {
      if (errno == EINTR)
	continue;
      else
      {
	LIB_SOCK_PRINTERR ("LIB_SOCKET_server_accept: accept() error");
	return (-1);
      }
    }

    break;
  }

  return (new_socket_fd);

}				/* end LIB_SOCKET_server_accept */


/******************************************************************************
**  Routine Name : LIB_SOCKET_disconnect
**
**  Purpose      : Closes down the socket.
**
**  Returns      : - Zero indicates successful operation.
**                 - Value of less than zero indicates error.
******************************************************************************/
int LIB_SOCKET_disconnect (int socket_fd)
{
  struct linger linger_opt;
  int           rtnval = 0;


 /* Check for valid input parameters */
  if (socket_fd <= 0)
    return (-1);

  linger_opt.l_onoff = 1;
  linger_opt.l_linger = 10;

#if 0
  if (setsockopt (socket_fd, SOL_SOCKET, SO_LINGER,
		  &linger_opt, sizeof (linger_opt)) < 0)
  {
    LIB_SOCK_PRINTERR ("LIB_SOCKET_disconnect: setsockopt() error");
    rtnval = -1;
  }
#endif
 /* Close the socket down */
  if (close (socket_fd) < 0)
  {
    LIB_SOCK_PRINTERR ("LIB_SOCKET_disconnect: close() error");
    rtnval = -1;
  }

  return (rtnval);

}				/* end LIB_SOCKET_disconnect */


/******************************************************************************
**  Routine Name : LIB_SOCKET_read
**
**  Purpose      : Reads the specified number of bytes
**                 from the socket descriptor.
**
**  Returns      : - Number of bytes actually read.
**                 - Value of less than zero indicates error.
******************************************************************************/
int LIB_SOCKET_read (int socket_fd,char *ptr,int nbytes)
{
  int           nleft,
                nread;


 /* Check for valid input parameters */
  if (socket_fd <= 0 || ptr == NULL || nbytes == 0)
    return (-1);

  nleft = nbytes;
  while (nleft > 0)
  {
    if ((nread = read (socket_fd, ptr, nleft)) < 0)
    {
      if (errno != EINVAL)	/* Retry if interrupted */
	return (nbytes - nleft);
      nread = 0;
    }
    else if (nread == 0)
      break;

    nleft -= nread;
    ptr += nread;
  }

  return (nbytes - nleft);

}				/* end LIB_SOCKET_read */


/******************************************************************************
**  Routine Name : LIB_SOCKET_write
**
**  Purpose      : Writes the specified number of bytes
**                 to the socket descriptor.
**
**  Returns      : - Number of bytes actually written.
**                 - Value of less than zero indicates error.
******************************************************************************/
int LIB_SOCKET_write (int socket_fd,char *ptr,int nbytes)
{
  int           nleft,
                nwritten;


 /* Check for valid input parameters */
  if (socket_fd <= 0 || ptr == NULL || nbytes == 0)
    return (-1);

  nleft = nbytes;
  while (nleft > 0)
  {
    if ((nwritten = write (socket_fd, ptr, nleft)) < 0)
    {
      if (errno != EINVAL)	/* Retry if interrupted. */
	return (nbytes - nleft);
      nwritten = 0;
    }

    nleft -= nwritten;
    ptr += nwritten;
  }

  return (nbytes - nleft);

}				/* end LIB_SOCKET_write */


/******************************************************************************
**  Routine Name : LIB_DATAGRAM_client_setup
**
**  Purpose      : Initiate a connection to a specified port and host.
**
**                 RESTRICTIONS: Service name must be defined in
**                               /etc/service for "inet" family.
**                               Family name (if used) must be defined
**                               in /etc/hosts.
**
**  Returns      : - Socket descriptor of established connection.
**                 - Value of less than zero indicates error.
******************************************************************************/
int LIB_DATAGRAM_client_setup (char *host_name,char *service_name,char *family_name)
{
  int           flag = 1;	/* TCP_NODELAY flag value */
  char          hostbuffer[LIB_SOCK_MAXSTR];	/* Buffer to hold host name */
  int           socket_fd;	/* socket descriptor of connection */
  struct sockaddr_in client_in;	/* socket parameter structure */
  struct sockaddr_un client_un;	/* socket parameter structure */
  int           client_un_len;
  struct hostent *hostent;	/* pointer to host information */
  struct servent *servent;
  int portNumber;


 /* Check for valid input parameters */
  if (family_name == NULL)
    return (-1);

  if (!strcasecmp (family_name, "unix"))
  {
    return (-1);
  }

  else
  {
    if (host_name == NULL)
    {
    /* If host name is not specified, then get local hostname */
      if ((gethostname (hostbuffer, sizeof (hostbuffer))) == -1)
      {
	LIB_SOCK_PRINTERR ("LIB_DATAGRAM_client_setup: gethostname() error");
	return (-1);
      }
      host_name = hostbuffer;
    }

    if ((hostent = gethostbyname (host_name)) == NULL)
    {
      LIB_SOCK_PRINTERR ("LIB_DATAGRAM_client_setup: gethostbyname() error");
      return (-1);
    }

  /* Service name must be specified, otherwise an error exists */
    if (service_name == NULL)
      return (-1);

  /* Get port number */
#if !defined CRIO
    setservent (0);
#endif
    if (!isdigit(service_name[0])) {
      if ((servent = getservbyname (service_name, NULL)) == NULL)
      {
        LIB_SOCK_PRINTERR ("LIB_SOCKET_client_setup: getservbyname() error");
        return (-1);
      }
    } else {
      servent = NULL;
      portNumber = htons(atoi(service_name));
    }
#if !defined CRIO
    endservent ();
#endif

  /* Name socket */
    memset ((char *) &client_in, 0, sizeof (client_in));
    client_in.sin_family = PF_INET;
    memcpy (&client_in.sin_addr, hostent->h_addr, hostent->h_length);
    if (servent != NULL)
      client_in.sin_port = servent->s_port;
    else
      client_in.sin_port = portNumber;

  /* Create socket */
    if ((socket_fd = socket (client_in.sin_family, SOCK_DGRAM, 0)) < 0)
    {
      LIB_SOCK_PRINTERR ("LIB_DATAGRAM_client_setup: socket() error");
      return (-1);
    }

  }

  return (socket_fd);

}				/* end LIB_DATAGRAM_client_setup */


/******************************************************************************
**  Routine Name : LIB_DATAGRAM_server_setup
**
**  Purpose      : Creates a socket at the specified portnumber and listens.
**
**                 RESTRICTIONS: Service name must be defined in
**                               /etc/service for "inet" family.
**                               Family name (if used) must be defined
**                               in /etc/hosts.
**
**  Returns      : - Socket descriptor of created socket.
**                 - Value of less than zero indicates error.
******************************************************************************/
int LIB_DATAGRAM_server_setup (char *host_name,char *service_name,char *family_name)
{
  int           flag = 1;	/* flag value */
  int           reuse_flag;	/* reuse flag value */
  unsigned int           reuse_flag_size;/* reuse flag size */
  char          hostbuffer[LIB_SOCK_MAXSTR];	/* Buffer to hold host name */
  int           socket_fd;	/* socket descriptor of connection */
  struct sockaddr_in server_in;	/* socket parameter structure */
  struct sockaddr_un server_un;	/* socket parameter structure */
  struct hostent *hostent;	/* pointer to host information */
  struct servent *servent;
  int portNumber;


 /* Check for valid input parameters */
  if (family_name == NULL)
    return (-1);

  if (!strcasecmp (family_name, "unix"))
  {
    return (-1);
  }

  else
  {
    if (host_name == NULL)
    {
      if ((gethostname (hostbuffer, sizeof (hostbuffer))) == -1)
      {
	LIB_SOCK_PRINTERR ("LIB_DATAGRAM_client_setup: gethostname() error");
	return (-1);
      }
      host_name = hostbuffer;
    }

    if ((hostent = gethostbyname (host_name)) == NULL)
    {
      LIB_SOCK_PRINTERR ("LIB_DATAGRAM_client_setup: gethostbyname() error");
      return (-1);
    }

    if (service_name == NULL)
      return (-1);

#if !defined CRIO
    setservent (0);
#endif
    if (!isdigit(service_name[0])) {
      if ((servent = getservbyname (service_name, NULL)) == NULL)
      {
        LIB_SOCK_PRINTERR ("LIB_SOCKET_client_setup: getservbyname() error");
        return (-1);
      }
    } else {
      servent = NULL;
      portNumber = htons(atoi(service_name));
    }
#if !defined CRIO
    endservent ();
#endif

  /* Name socket */
    memset ((char *) &server_in, 0, sizeof (server_in));
    server_in.sin_family = PF_INET;
    memcpy (&server_in.sin_addr, hostent->h_addr, hostent->h_length);
    if (servent != NULL)
      server_in.sin_port = servent->s_port;
    else
      server_in.sin_port = portNumber;

  /* Create socket */
    if ((socket_fd = socket (server_in.sin_family, SOCK_DGRAM, 0)) < 0)
    {
      LIB_SOCK_PRINTERR ("LIB_DATAGRAM_client_setup: socket() error");
      return (-1);
    }

  /* Bind to the socket */
    if (bind (socket_fd, (struct sockaddr *)&server_in, sizeof (server_in)) < 0)
    {
      LIB_SOCK_PRINTERR ("LIB_DATAGRAM_server_setup: bind() error");
      LIB_DATAGRAM_disconnect (socket_fd);
      return (-1);
    }
  }

#if 0
  reuse_flag_size = sizeof (reuse_flag);
  if (getsockopt (socket_fd, SOL_SOCKET, SO_REUSEADDR,
		  (char *) &reuse_flag, &reuse_flag_size) == -1)
  {
    LIB_SOCK_PRINTERR ("LIB_DATAGRAM_server_setup: getsockopt() error");
    LIB_DATAGRAM_disconnect (socket_fd);
    return (-1);
  }

  if (!reuse_flag)
  {
    if (setsockopt (socket_fd, SOL_SOCKET, SO_REUSEADDR,
		    (char *) &flag, sizeof (flag)) == -1)
    {
      LIB_SOCK_PRINTERR ("LIB_DATAGRAM_server_setup: setsockopt() error");
      LIB_DATAGRAM_disconnect (socket_fd);
      return (-1);
    }
  }
#endif

  return (socket_fd);

}				/* end LIB_DATAGRAM_server_setup */


/******************************************************************************
**  Routine Name : LIB_DATAGRAM_write_setup
**
**  Purpose      : Initiate a connection to a specified port and host.
**
**                 RESTRICTIONS: Service name must be defined in
**                               /etc/service for "inet" family.
**                               Family name (if used) must be defined
**                               in /etc/hosts.
**
**  Returns      : - Socket descriptor of established connection.
**                 - Value of less than zero indicates error.
******************************************************************************/
int LIB_DATAGRAM_write_setup ()
{
  int           flag = 1;	/* TCP_NODELAY flag value */
  char          hostbuffer[LIB_SOCK_MAXSTR];	/* Buffer to hold host name */
  int           socket_fd;	/* socket descriptor of connection */
  struct sockaddr_in client_in;	/* socket parameter structure */
  struct sockaddr_un client_un;	/* socket parameter structure */
  struct hostent *hostent;	/* pointer to host information */
  struct servent *servent;


 /* Create socket */
  if ((socket_fd = socket (PF_INET, SOCK_DGRAM, 0)) < 0)
  {
    LIB_SOCK_PRINTERR ("LIB_DATAGRAM_write_setup: socket() error");
    return (-1);
  }

  return (socket_fd);

}				/* end LIB_DATAGRAM_write_setup */


/******************************************************************************
**  Routine Name : LIB_DATAGRAM_read_setup
**
**  Purpose      : Creates a socket at the specified portnumber and listens.
**
**                 RESTRICTIONS: Service name must be defined in
**                               /etc/service for "inet" family.
**                               Family name (if used) must be defined
**                               in /etc/hosts.
**
**  Returns      : - Socket descriptor of created socket.
**                 - Value of less than zero indicates error.
******************************************************************************/
int LIB_DATAGRAM_read_setup (char *host_name,char *service_name)
{
  int           flag = 1;	/* TCP_NODELAY flag value */
  char          hostbuffer[LIB_SOCK_MAXSTR];	/* Buffer to hold host name */
  int           socket_fd;	/* socket descriptor of connection */
  struct sockaddr_in server_in;	/* socket parameter structure */
  struct sockaddr_un server_un;	/* socket parameter structure */
  struct hostent *hostent;	/* pointer to host information */
  struct servent *servent;
  int portNumber;


  if (host_name == NULL)
  {
    if ((gethostname (hostbuffer, sizeof (hostbuffer))) == -1)
    {
      LIB_SOCK_PRINTERR ("LIB_DATAGRAM_read_setup: gethostname() error");
      return (-1);
    }
    host_name = hostbuffer;
  }

  if ((hostent = gethostbyname (host_name)) == NULL)
  {
    LIB_SOCK_PRINTERR ("LIB_DATAGRAM_read_setup: gethostbyname() error");
    return (-1);
  }

  if (service_name == NULL)
    return (-1);

#if !defined CRIO
  setservent (0);
#endif
  if (!isdigit(service_name[0])) {
    if ((servent = getservbyname (service_name, NULL)) == NULL)
    {
      LIB_SOCK_PRINTERR ("LIB_SOCKET_read_setup: getservbyname() error");
      return (-1);
    }
  } else {
    servent = NULL;
    portNumber = htons(atoi(service_name));
  }
#if !defined CRIO
  endservent ();
#endif

 /* Name socket */
  memset ((char *) &server_in, 0, sizeof (server_in));
  server_in.sin_family = PF_INET;
  memcpy (&server_in.sin_addr, hostent->h_addr, hostent->h_length);
  if (servent != NULL)
    server_in.sin_port = servent->s_port;
  else
    server_in.sin_port = portNumber;

 /* Create socket */
  if ((socket_fd = socket (server_in.sin_family, SOCK_DGRAM, 0)) < 0)
  {
    LIB_SOCK_PRINTERR ("LIB_DATAGRAM_read_setup: socket() error");
    return (-1);
  }

 /* Bind to the socket */
  if (bind (socket_fd, (struct sockaddr *)&server_in, sizeof (server_in)) < 0)
  {
    LIB_SOCK_PRINTERR ("LIB_DATAGRAM_read_setup: bind() error");
    LIB_DATAGRAM_disconnect (socket_fd);
    return (-1);
  }

  return (socket_fd);

}				/* end LIB_DATAGRAM_read_setup */


/******************************************************************************
**  Routine Name : LIB_DATAGRAM_disconnect
**
**  Purpose      : Closes down the socket.
**
**  Returns      : - Zero indicates successful operation.
**                 - Value of less than zero indicates error.
******************************************************************************/
int LIB_DATAGRAM_disconnect (int socket_fd)
{
  struct linger linger_opt;
  int           rtnval = 0;


 /* Check for valid input parameters */
  if (socket_fd <= 0)
    return (-1);

  linger_opt.l_onoff = 1;
  linger_opt.l_linger = 10;

#if 0
  if (setsockopt (socket_fd, SOL_SOCKET, SO_LINGER,
		  &linger_opt, sizeof (linger_opt)) < 0)
  {
    LIB_SOCK_PRINTERR ("LIB_DATAGRAM_disconnect: setsockopt() error");
    rtnval = -1;
  }
#endif

 /* Close the socket down */
  if (close (socket_fd) < 0)
  {
    LIB_SOCK_PRINTERR ("LIB_DATAGRAM_disconnect: close() error");
    rtnval = -1;
  }

  return (rtnval);

}				/* end LIB_DATAGRAM_disconnect */


/******************************************************************************
**  Routine Name : LIB_DATAGRAM_read
**
**  Purpose      : Reads the specified number of bytes
**                 from the socket descriptor.
**
**  Returns      : - Number of bytes actually read.
**                 - Value of less than zero indicates error.
******************************************************************************/
int LIB_DATAGRAM_read(struct sockaddr_in * from,int socket_fd,char *ptr,int nbytes)
{
  int           nread;
  struct sockaddr_in name;
  int           length;


 /* Check for valid input parameters */
  if (socket_fd <= 0 || ptr == NULL || nbytes == 0)
    return (-1);

  length = sizeof (name);

  if ((nread = recvfrom (socket_fd, ptr, nbytes, 0, (struct sockaddr *)&name, &length)) < 0)
  {
    return (-1);
  }

  if (from != NULL)
    memcpy (from, &name, sizeof (struct sockaddr_in));

  return (nread);

}				/* end LIB_DATAGRAM_read */


/******************************************************************************
**  Routine Name : LIB_DATAGRAM_write
**
**  Purpose      : Writes the specified number of bytes
**                 to the socket descriptor.
**
**  Returns      : - Number of bytes actually written.
**                 - Value of less than zero indicates error.
******************************************************************************/
int LIB_DATAGRAM_write(char *host_name,char *service_name,int socket_fd,char *ptr,int nbytes)
{
  int           nleft,
                nwritten;
  char          hostbuffer[LIB_SOCK_MAXSTR];	/* Buffer to hold host name */
  struct sockaddr_in client_in;	/* socket parameter structure */
  struct sockaddr_un client_un;	/* socket parameter structure */
  struct hostent *hostent;	/* pointer to host information */
  struct servent *servent;
  int portNumber;


 /* Check for valid input parameters */
  if (socket_fd <= 0 || ptr == NULL || nbytes == 0)
    return (-1);

  if (host_name == NULL)
  {
  /* If host name is not specified, then get local hostname */
    if ((gethostname (hostbuffer, sizeof (hostbuffer))) == -1)
    {
      LIB_SOCK_PRINTERR ("LIB_DATAGRAM_write: gethostname() error");
      return (-1);
    }
    host_name = hostbuffer;
  }

  if ((hostent = gethostbyname (host_name)) == NULL)
  {
    LIB_SOCK_PRINTERR ("LIB_DATAGRAM_write: gethostbyname() error");
    return (-1);
  }

 /* Service name must be specified, otherwise an error exists */
  if (service_name == NULL)
    return (-1);

 /* Get port number */
#if !defined CRIO
  setservent (0);
#endif
  if (!isdigit(service_name[0])) {
    if ((servent = getservbyname (service_name, NULL)) == NULL)
    {
      LIB_SOCK_PRINTERR ("LIB_SOCKET_write: getservbyname() error");
      return (-1);
    }
  } else {
    servent = NULL;
    portNumber = htons(atoi(service_name));
  }
#if !defined CRIO
  endservent ();
#endif

 /* Name socket */
  memset ((char *) &client_in, 0, sizeof (client_in));
  client_in.sin_family = PF_INET;
  memcpy (&client_in.sin_addr, hostent->h_addr, hostent->h_length);
  if (servent != NULL)
    client_in.sin_port = servent->s_port;
  else
    client_in.sin_port = portNumber;

  if ((nwritten = sendto
       (socket_fd, ptr, nbytes, 0, (struct sockaddr *)&client_in, sizeof (client_in))) < 0)
  {
    return (-1);
  }

  return (nwritten);

}				/* end LIB_DATAGRAM_write */


/******************************************************************************
**  Routine Name : LIB_DATAGRAM_write_to
**
**  Purpose      : Writes the specified number of bytes
**                 to the socket descriptor.
**
**  Returns      : - Number of bytes actually written.
**                 - Value of less than zero indicates error.
******************************************************************************/
int LIB_DATAGRAM_write_to(struct sockaddr_in * to,int socket_fd,char *ptr,int nbytes)
{
  int           nwritten;

 /* Check for valid input parameters */
  if (socket_fd <= 0 || ptr == NULL || nbytes == 0)
    return (-1);

  if ((nwritten = sendto
       (socket_fd, ptr, nbytes, 0, (struct sockaddr *)to, sizeof (struct sockaddr_in))) < 0)
  {
    return (-1);
  }

  return (nwritten);

}				/* end LIB_DATAGRAM_write_to */

int LIB_SOCK_UTIL_readn (int fd,char *ptr,int nbytes)
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

int LIB_SOCK_UTIL_writen (int fd,char *ptr,int nbytes)
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

int LIB_SOCK_UTIL_readline (int fd,char *ptr,int maxlen)
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

void LIB_SOCK_UTIL_str_echo (int sockfd)
{
  int           n,
                i;
  char          line[LIB_SOCK_MAXSTR];

  for (;;)
  {
    n = LIB_SOCK_UTIL_readline (sockfd, line, LIB_SOCK_MAXSTR);
    if (n == 0)
      return;
    else if (n < 0)
      LIB_UTIL_error_exit ("str_echo: LIB_SOCK_UTIL_readline error");

    printf ("received:%s",line);
    for (i = 0; i < n; i++)
    {
      if (isupper (line[i]))
	line[i] = tolower (line[i]);
      else
	line[i] = toupper (line[i]);
    }

    if (LIB_SOCK_UTIL_writen (sockfd, line, n) != n)
      LIB_UTIL_error_exit ("str_echo: LIB_SOCK_UTIL_writen error");

  }
}

void LIB_SOCK_UTIL_str_cli (FILE *fp,int sockfd)
{
  int           n;
  char          sendline[LIB_SOCK_MAXSTR],
                recvline[LIB_SOCK_MAXSTR + 1];

  printf ("START ENTERING STRINGS\n");
  while (fgets (sendline, LIB_SOCK_MAXSTR, fp) != NULL)
  {
    n = strlen (sendline);
    if (LIB_SOCK_UTIL_writen (sockfd, sendline, n) != n)
      LIB_UTIL_error_return ("str_cli: LIB_SOCK_UTIL_writen error on socket");

    n = LIB_SOCK_UTIL_readline (sockfd, recvline, LIB_SOCK_MAXSTR);
    if (n < 0)
      LIB_UTIL_error_exit ("str_cli: LIB_SOCK_UTIL_readline error");
    recvline[n] = 0;
    fputs (recvline, stdout);
  }
  if (ferror (fp))
    LIB_UTIL_error_return ("str_cli: error reading file");
}

void LIB_SOCK_UTIL_dg_echo (int sockfd,struct sockaddr *pcli_addr,int maxclilen)
{
  int           n;
  int              clilen;
  char          mesg[LIB_SOCK_MAXSTR];

  for (;;)
  {
    clilen = maxclilen;
    n = recvfrom (sockfd, mesg, LIB_SOCK_MAXSTR, 0, pcli_addr, &clilen);
    if (n < 0)
      LIB_UTIL_error_exit ("dg_echo: recvfrom error");
    mesg[n] = 0;
    printf ("RECVFROM: %s\n", mesg);

    if (sendto (sockfd, mesg, n, 0, pcli_addr, clilen) != n)
      LIB_UTIL_error_exit ("dg_echo: sendto error");
  }
}

void LIB_SOCK_UTIL_dg_cli (FILE *fp,int sockfd,struct sockaddr *pserv_addr,int servlen)
{
  int           n;
  unsigned int              slen;
  char          sendline[LIB_SOCK_MAXSTR],
                recvline[LIB_SOCK_MAXSTR + 1];

  slen = servlen;

  printf ("START ENTERING STRINGS\n");
  while (fgets (sendline, LIB_SOCK_MAXSTR, fp) != NULL)
  {
    n = strlen (sendline);
    if (sendto (sockfd, sendline, n, 0, pserv_addr, servlen) != n)
      LIB_UTIL_error_exit ("dg_cli: sendto error on socket");

    n = recvfrom (sockfd, recvline, LIB_SOCK_MAXSTR, 0,
		  (struct sockaddr *) pserv_addr, (int *) &slen);
    if (n < 0)
      LIB_UTIL_error_exit ("dg_cli: recvfrom error");
    recvline[n] = 0;
    fputs (recvline, stdout);
  }

  if (ferror (fp))
    LIB_UTIL_error_exit ("dg_cli: error reading file");

}
