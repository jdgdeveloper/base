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

BUILD_SPEC = PPC603gnu
DEBUG_MODE = 1
ifeq ($(DEBUG_MODE),1)
MODE_DIR := Debug
else
MODE_DIR := NonDebug
endif
OBJ_DIR := .
PRJ_ROOT_DIR := C:/WindRiver/workspace/jdgSecTask
WS_ROOT_DIR := C:/WindRiver/workspace



#Global Build Macros
PROJECT_TYPE = DKM
DEFINES = 
EXPAND_DBG = 0


#BuildSpec specific Build Macros
VX_CPU_FAMILY = ppc
CPU = PPC603
TOOL_FAMILY = gnu
TOOL = gnu
TOOL_PATH = 
CC_ARCH_SPEC = -mcpu=603 -mstrict-align -mno-implicit-fp
LIBPATH = 
LIBS = 

IDE_INCLUDES = -I$(WIND_BASE)/target/h -IC:/WindRiver/workspace/jdgTaskGlobal -I$(WIND_BASE)/target/h/wrn/coreip -I$(WIND_BASE)/target/h/WPILib -IC:/WindRiver/workspace/jdgSecTask 

IDE_LIBRARIES = $(WIND_BASE)/target/lib/WPILib.a 



#BuildTool flags
ifeq ($(DEBUG_MODE),1)
DEBUGFLAGS_C-Compiler = -g
DEBUGFLAGS_C++-Compiler = -g
DEBUGFLAGS_Linker = -g
DEBUGFLAGS_Partial-Image-Linker = 
DEBUGFLAGS_Librarian = 
DEBUGFLAGS_Assembler = -g
else
DEBUGFLAGS_C-Compiler = -O2 -fstrength-reduce -fno-builtin
DEBUGFLAGS_C++-Compiler = -O2 -fstrength-reduce -fno-builtin
DEBUGFLAGS_Linker = -O2 -fstrength-reduce -fno-builtin
DEBUGFLAGS_Partial-Image-Linker = 
DEBUGFLAGS_Librarian = 
DEBUGFLAGS_Assembler = -O2 -fstrength-reduce -fno-builtin
endif


#Project Targets
PROJECT_TARGETS = jdgSecTask/$(MODE_DIR)/jdgSecTask.out


#Rules

# jdgSecTask
ifeq ($(DEBUG_MODE),1)
jdgSecTask/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -g
jdgSecTask/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -g
jdgSecTask/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -g
jdgSecTask/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
jdgSecTask/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
jdgSecTask/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -g
else
jdgSecTask/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -O2 -fstrength-reduce -fno-builtin
jdgSecTask/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -O2 -fstrength-reduce -fno-builtin
jdgSecTask/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -O2 -fstrength-reduce -fno-builtin
jdgSecTask/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
jdgSecTask/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
jdgSecTask/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -O2 -fstrength-reduce -fno-builtin
endif
jdgSecTask/$(MODE_DIR)/% : IDE_INCLUDES = -I$(WIND_BASE)/target/h -IC:/WindRiver/workspace/jdgTaskGlobal -I$(WIND_BASE)/target/h/wrn/coreip -I$(WIND_BASE)/target/h/WPILib -IC:/WindRiver/workspace/jdgSecTask 
jdgSecTask/$(MODE_DIR)/% : IDE_LIBRARIES = $(WIND_BASE)/target/lib/WPILib.a 
jdgSecTask/$(MODE_DIR)/% : PROJECT_TYPE = DKM
jdgSecTask/$(MODE_DIR)/% : DEFINES = 
jdgSecTask/$(MODE_DIR)/% : EXPAND_DBG = 0
jdgSecTask/$(MODE_DIR)/% : VX_CPU_FAMILY = ppc
jdgSecTask/$(MODE_DIR)/% : CPU = PPC603
jdgSecTask/$(MODE_DIR)/% : TOOL_FAMILY = gnu
jdgSecTask/$(MODE_DIR)/% : TOOL = gnu
jdgSecTask/$(MODE_DIR)/% : TOOL_PATH = 
jdgSecTask/$(MODE_DIR)/% : CC_ARCH_SPEC = -mcpu=603 -mstrict-align -mno-implicit-fp
jdgSecTask/$(MODE_DIR)/% : LIBPATH = 
jdgSecTask/$(MODE_DIR)/% : LIBS = 
jdgSecTask/$(MODE_DIR)/% : OBJ_DIR := jdgSecTask/$(MODE_DIR)

jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/lib_socket.o : C:/WindRiver/workspace/jdgSecTask/lib_socket.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/lib_util.o : C:/WindRiver/workspace/jdgSecTask/lib_util.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/sock_utility.o : C:/WindRiver/workspace/jdgSecTask/sock_utility.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/sys_error.o : C:/WindRiver/workspace/jdgSecTask/sys_error.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/telnet_server.o : C:/WindRiver/workspace/jdgSecTask/telnet_server.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


OBJECTS_jdgSecTask = jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/lib_socket.o \
	 jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/lib_util.o \
	 jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/sock_utility.o \
	 jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/sys_error.o \
	 jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/telnet_server.o

jdgSecTask/$(MODE_DIR)/jdgSecTask.out : $(OBJECTS_jdgSecTask)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@";rm -f "$@";nmppc $(OBJECTS_jdgSecTask) $(IDE_LIBRARIES) | tclsh $(WIND_BASE)/host/resource/hutils/tcl/munch.tcl -c ppc > $(OBJ_DIR)/ctdt.c; $(TOOL_PATH)ccppc $(DEBUGFLAGS_Linker) $(CC_ARCH_SPEC) -fdollars-in-identifiers -Wall $(ADDED_CFLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES)  -o $(OBJ_DIR)/ctdt.o -c $(OBJ_DIR)/ctdt.c; $(TOOL_PATH)ccppc -r -nostdlib -Wl,-X -T $(WIND_BASE)/target/h/tool/gnu/ldscripts/link.OUT -o "$@" $(OBJ_DIR)/ctdt.o $(OBJECTS_jdgSecTask) $(IDE_LIBRARIES) $(LIBPATH) $(LIBS)  $(ADDED_LIBPATH) $(ADDED_LIBS) && if [ "$(EXPAND_DBG)" = "1" ]; then plink "$@";fi

jdgSecTask/$(MODE_DIR)/jdgSecTask_compile_file : $(FILE) ;

_clean :: jdgSecTask/$(MODE_DIR)/jdgSecTask_clean

jdgSecTask/$(MODE_DIR)/jdgSecTask_clean : 
	$(TRACE_FLAG)if [ -d "jdgSecTask" ]; then cd "jdgSecTask"; rm -rf $(MODE_DIR); fi

DEP_FILES := jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/lib_socket.d jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/lib_util.d jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/sock_utility.d \
	 jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/sys_error.d jdgSecTask/$(MODE_DIR)/Objects/jdgSecTask/telnet_server.d
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
