/*******************************************************************************
*
* PROJECT ID : dftst
* CATEGORY   : DELIVERABLE SOFTWARE
* SUBSYSTEM  : SNOW SHED
* FILECLASS  : CCC
*
*
* File Name:       stripallcr.c
* SU Name:       TEST  
* SU Title:         Test 
* Author:          JC
* Creation Date:   
* Classification:  UNCLASSIFIED
*
* ABSTRACT: gcc stripallcr.c -o stripallcr
*
*
* ASSUMPTIONS/LIMITATIONS: None
*
*
* Revision History:  Software revision history can be obtained from the 
*                    configuration management database server.
*
*******************************************************************************/
/*******************************************************************
 * 	System include files
 *******************************************************************/
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int main(int argc, char **argv, char **envp)
{
FILE *in, *out;
char cin, cout;

if(argv[1] != NULL)
{
  in=fopen(argv[1],"r");
  if(in==NULL)
  {
    fprintf(stderr,"Cannot open %s for input\n",argv[1]);
    exit(-1);
  }
}
else
{
  in=stdin;
}
if(argv[2] != NULL)
{
  out=fopen(argv[2],"w");
  if(out==NULL)
  {
    fprintf(stderr,"Cannot open %s for output\n",argv[2]);
    exit(-2);
  }
}
else
{
  out=stdout;
}

cin=fgetc(in);
while(!feof(in))
{
  cout=fgetc(in);
  if ((cout == EOF) && ferror(in))
  {
      fprintf(stderr,"Cannot read from %s...errno is %d\n",argv[1],errno);
      exit(-3);
  }

  {
    if(cin != 0x0d)
        cin=fputc(cin,out);
    if(cin == EOF)
    {
      fprintf(stderr,"Cannot write to %s...errno is %d\n",argv[2],errno);
      exit(-4);
    }
    cin=cout;
    fflush(out);
  }
}
fflush(out);
exit(0);
}
