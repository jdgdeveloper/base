# Wind River Workbench generated Makefile.
# Do not edit!!!
#
# The file ".wrmakefile" is the template used by the Wind River Workbench to
# generate the makefiles of this project. Add user-specific build targets and
# make rules only(!) in this project's ".wrmakefile" file. These will then be
# automatically dumped into the makefiles.

WIND_HOME := $(subst \,/,$(WIND_HOME))
WIND_BASE := $(subst \,/,$(WIND_BASE))
WIND_USR := $(subst \,/,$(WIND_USR))

all : pre_build main_all post_build

_clean ::
	@echo "make: removing targets and objects of `pwd`"

TRACE=0
TRACEON=$(TRACE:0=@)
TRACE_FLAG=$(TRACEON:1=)

MAKEFILE := Makefile

FLEXIBLE_BUILD := 1

BUILD_SPEC = PPC32diab
DEBUG_MODE = 1
ifeq ($(DEBUG_MODE),1)
MODE_DIR := Debug
else
MODE_DIR := NonDebug
endif
OBJ_DIR := .
PRJ_ROOT_DIR := C:/WindRiver/workspace/jdgTask
WS_ROOT_DIR := C:/WindRiver/workspace



#Global Build Macros
PROJECT_TYPE = DKM
DEFINES = 
EXPAND_DBG = 0


#BuildSpec specific Build Macros
VX_CPU_FAMILY = ppc
CPU = PPC32
TOOL_FAMILY = diab
TOOL = diab
TOOL_PATH = 
CC_ARCH_SPEC = -tPPCFH:vxworks63 -Xstmw-slow -DPPC32_fp60x
LIBPATH = 
LIBS = 

IDE_INCLUDES = -I$(WIND_BASE)/target/h -I$(WIND_BASE)/target/h/wrn/coreip 

IDE_LIBRARIES = 



#BuildTool flags
ifeq ($(DEBUG_MODE),1)
DEBUGFLAGS_C-Compiler = -g
DEBUGFLAGS_C++-Compiler = -g
DEBUGFLAGS_Linker = -g
DEBUGFLAGS_Partial-Image-Linker = 
DEBUGFLAGS_Librarian = 
DEBUGFLAGS_Assembler = -g
else
DEBUGFLAGS_C-Compiler = -XO -Xsize-opt
DEBUGFLAGS_C++-Compiler = -XO -Xsize-opt
DEBUGFLAGS_Linker = -XO -Xsize-opt
DEBUGFLAGS_Partial-Image-Linker = 
DEBUGFLAGS_Librarian = 
DEBUGFLAGS_Assembler = -XO -Xsize-opt
endif


#Project Targets
PROJECT_TARGETS = telnetTask/$(MODE_DIR)/telnetTask.out \
	 telnetTask_partialImage/$(MODE_DIR)/telnetTask_partialImage.o


#Rules

# telnetTask
ifeq ($(DEBUG_MODE),1)
telnetTask/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -g
telnetTask/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -g
telnetTask/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -g
telnetTask/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
telnetTask/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
telnetTask/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -g
else
telnetTask/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -XO -Xsize-opt
telnetTask/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -XO -Xsize-opt
telnetTask/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -XO -Xsize-opt
telnetTask/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
telnetTask/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
telnetTask/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -XO -Xsize-opt
endif
telnetTask/$(MODE_DIR)/% : IDE_INCLUDES = -I$(WIND_BASE)/target/h -I$(WIND_BASE)/target/h/wrn/coreip 
telnetTask/$(MODE_DIR)/% : IDE_LIBRARIES = 
telnetTask/$(MODE_DIR)/% : PROJECT_TYPE = DKM
telnetTask/$(MODE_DIR)/% : DEFINES = 
telnetTask/$(MODE_DIR)/% : EXPAND_DBG = 0
telnetTask/$(MODE_DIR)/% : VX_CPU_FAMILY = ppc
telnetTask/$(MODE_DIR)/% : CPU = PPC32
telnetTask/$(MODE_DIR)/% : TOOL_FAMILY = diab
telnetTask/$(MODE_DIR)/% : TOOL = diab
telnetTask/$(MODE_DIR)/% : TOOL_PATH = 
telnetTask/$(MODE_DIR)/% : CC_ARCH_SPEC = -tPPCFH:vxworks63 -Xstmw-slow -DPPC32_fp60x
telnetTask/$(MODE_DIR)/% : LIBPATH = 
telnetTask/$(MODE_DIR)/% : LIBS = 
telnetTask/$(MODE_DIR)/% : OBJ_DIR := telnetTask/$(MODE_DIR)

OBJECTS_telnetTask = telnetTask_partialImage/$(MODE_DIR)/telnetTask_partialImage.o

telnetTask/$(MODE_DIR)/telnetTask.out : $(OBJECTS_telnetTask)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@";rm -f "$@";ddump -Ng $(OBJECTS_telnetTask) $(IDE_LIBRARIES) | tclsh $(WIND_BASE)/host/resource/hutils/tcl/munch.tcl -c ppc > $(OBJ_DIR)/ctdt.c; $(TOOL_PATH)dcc $(DEBUGFLAGS_Linker) $(CC_ARCH_SPEC) -Xdollar-in-ident -Xforce-declarations $(ADDED_CFLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES)  -o $(OBJ_DIR)/ctdt.o -c $(OBJ_DIR)/ctdt.c; $(TOOL_PATH)dld -tPPCFH:vxworks63 -X -r5 -r4 -o "$@" $(OBJ_DIR)/ctdt.o $(OBJECTS_telnetTask) $(IDE_LIBRARIES) $(LIBPATH) $(LIBS)  $(ADDED_LIBPATH) $(ADDED_LIBS) && if [ "$(EXPAND_DBG)" = "1" ]; then plink "$@";fi

telnetTask/$(MODE_DIR)/telnetTask_compile_file : $(FILE) ;

_clean :: telnetTask/$(MODE_DIR)/telnetTask_clean

telnetTask/$(MODE_DIR)/telnetTask_clean : 
	$(TRACE_FLAG)if [ -d "telnetTask" ]; then cd "telnetTask"; rm -rf $(MODE_DIR); fi


# telnetTask_partialImage
ifeq ($(DEBUG_MODE),1)
telnetTask_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -g
telnetTask_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -g
telnetTask_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -g
telnetTask_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
telnetTask_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
telnetTask_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -g
else
telnetTask_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -XO -Xsize-opt
telnetTask_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -XO -Xsize-opt
telnetTask_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -XO -Xsize-opt
telnetTask_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
telnetTask_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
telnetTask_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -XO -Xsize-opt
endif
telnetTask_partialImage/$(MODE_DIR)/% : IDE_INCLUDES = -I$(WIND_BASE)/target/h -I$(WIND_BASE)/target/h/wrn/coreip 
telnetTask_partialImage/$(MODE_DIR)/% : IDE_LIBRARIES = 
telnetTask_partialImage/$(MODE_DIR)/% : PROJECT_TYPE = DKM
telnetTask_partialImage/$(MODE_DIR)/% : DEFINES = 
telnetTask_partialImage/$(MODE_DIR)/% : EXPAND_DBG = 0
telnetTask_partialImage/$(MODE_DIR)/% : VX_CPU_FAMILY = ppc
telnetTask_partialImage/$(MODE_DIR)/% : CPU = PPC32
telnetTask_partialImage/$(MODE_DIR)/% : TOOL_FAMILY = diab
telnetTask_partialImage/$(MODE_DIR)/% : TOOL = diab
telnetTask_partialImage/$(MODE_DIR)/% : TOOL_PATH = 
telnetTask_partialImage/$(MODE_DIR)/% : CC_ARCH_SPEC = -tPPCFH:vxworks63 -Xstmw-slow -DPPC32_fp60x
telnetTask_partialImage/$(MODE_DIR)/% : LIBPATH = 
telnetTask_partialImage/$(MODE_DIR)/% : LIBS = 
telnetTask_partialImage/$(MODE_DIR)/% : OBJ_DIR := telnetTask_partialImage/$(MODE_DIR)

telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/lib_socket.o : C:/WindRiver/workspace/jdgTask/lib_socket.c
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)dcc $(DEBUGFLAGS_C-Compiler) $(CC_ARCH_SPEC) -W:c:,-Xclib-optim-off -Xansi -Xlocal-data-area-static-only -Xforce-declarations  -Xmake-dependency=0xd $(ADDED_CFLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/lib_util.o : C:/WindRiver/workspace/jdgTask/lib_util.c
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)dcc $(DEBUGFLAGS_C-Compiler) $(CC_ARCH_SPEC) -W:c:,-Xclib-optim-off -Xansi -Xlocal-data-area-static-only -Xforce-declarations  -Xmake-dependency=0xd $(ADDED_CFLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/sock_utility.o : C:/WindRiver/workspace/jdgTask/sock_utility.c
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)dcc $(DEBUGFLAGS_C-Compiler) $(CC_ARCH_SPEC) -W:c:,-Xclib-optim-off -Xansi -Xlocal-data-area-static-only -Xforce-declarations  -Xmake-dependency=0xd $(ADDED_CFLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/sys_error.o : C:/WindRiver/workspace/jdgTask/sys_error.c
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)dcc $(DEBUGFLAGS_C-Compiler) $(CC_ARCH_SPEC) -W:c:,-Xclib-optim-off -Xansi -Xlocal-data-area-static-only -Xforce-declarations  -Xmake-dependency=0xd $(ADDED_CFLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/telnet_server.o : C:/WindRiver/workspace/jdgTask/telnet_server.c
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)dcc $(DEBUGFLAGS_C-Compiler) $(CC_ARCH_SPEC) -W:c:,-Xclib-optim-off -Xansi -Xlocal-data-area-static-only -Xforce-declarations  -Xmake-dependency=0xd $(ADDED_CFLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


OBJECTS_telnetTask_partialImage = telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/lib_socket.o \
	 telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/lib_util.o \
	 telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/sock_utility.o \
	 telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/sys_error.o \
	 telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/telnet_server.o

telnetTask_partialImage/$(MODE_DIR)/telnetTask_partialImage.o : $(OBJECTS_telnetTask_partialImage)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)dld -tPPCFH:vxworks63 -X -r5  -o "$@" $(OBJECTS_telnetTask_partialImage) $(LIBPATH) $(LIBS) $(ADDED_LIBPATH) $(ADDED_LIBS)  && if [ "$(EXPAND_DBG)" = "1" ]; then plink "$@";fi

telnetTask_partialImage/$(MODE_DIR)/telnetTask_partialImage_compile_file : $(FILE) ;

_clean :: telnetTask_partialImage/$(MODE_DIR)/telnetTask_partialImage_clean

telnetTask_partialImage/$(MODE_DIR)/telnetTask_partialImage_clean : 
	$(TRACE_FLAG)if [ -d "telnetTask_partialImage" ]; then cd "telnetTask_partialImage"; rm -rf $(MODE_DIR); fi

DEP_FILES := telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/lib_socket.d telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/lib_util.d telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/sock_utility.d \
	 telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/sys_error.d telnetTask_partialImage/$(MODE_DIR)/Objects/jdgTask/telnet_server.d
-include $(DEP_FILES)



-include $(PRJ_ROOT_DIR)/*.makefile

-include *.makefile

main_all : external_build $(PROJECT_TARGETS)
	@echo "make: built targets of `pwd`"

# entry point for extending the build
external_build ::
	@echo ""

# main entry point for pre processing prior to the build
pre_build :: $(PRE_BUILD_STEP) generate_sources
	@echo ""

# entry point for generating sources prior to the build
generate_sources ::
	@echo ""

# main entry point for post processing after the build
post_build :: $(POST_BUILD_STEP) deploy_output
	@echo ""

# entry point for deploying output after the build
deploy_output ::
	@echo ""

clean :: external_clean $(CLEAN_STEP) _clean

# entry point for extending the build clean
external_clean ::
	@echo ""
