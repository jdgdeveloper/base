#ifndef _mainGlobal_h_
#define _mainGlobal_h_

#ifdef _define_storage_
#define EXTERN
#else
#define EXTERN extern
#endif

typedef struct {
	int parameter;
	int frameCount;
	int testCount;
	char parameterString[80];
} global_data_type;

EXTERN global_data_type globalData;

#endif
