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
PRJ_ROOT_DIR := C:/WindRiver/workspace/jdgTask
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

IDE_INCLUDES = -I$(WIND_BASE)/target/h -IC:/WindRiver/workspace/jdgTaskGlobal -I$(WIND_BASE)/target/h/wrn/coreip -I$(WIND_BASE)/target/h/WPILib -IC:/WindRiver/workspace/jdgTask 

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
PROJECT_TARGETS = jdgTask/$(MODE_DIR)/jdgTask.out


#Rules

# jdgTask
ifeq ($(DEBUG_MODE),1)
jdgTask/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -g
jdgTask/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -g
jdgTask/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -g
jdgTask/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
jdgTask/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
jdgTask/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -g
else
jdgTask/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -O2 -fstrength-reduce -fno-builtin
jdgTask/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -O2 -fstrength-reduce -fno-builtin
jdgTask/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -O2 -fstrength-reduce -fno-builtin
jdgTask/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
jdgTask/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
jdgTask/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -O2 -fstrength-reduce -fno-builtin
endif
jdgTask/$(MODE_DIR)/% : IDE_INCLUDES = -I$(WIND_BASE)/target/h -IC:/WindRiver/workspace/jdgTaskGlobal -I$(WIND_BASE)/target/h/wrn/coreip -I$(WIND_BASE)/target/h/WPILib -IC:/WindRiver/workspace/jdgTask 
jdgTask/$(MODE_DIR)/% : IDE_LIBRARIES = $(WIND_BASE)/target/lib/WPILib.a 
jdgTask/$(MODE_DIR)/% : PROJECT_TYPE = DKM
jdgTask/$(MODE_DIR)/% : DEFINES = 
jdgTask/$(MODE_DIR)/% : EXPAND_DBG = 0
jdgTask/$(MODE_DIR)/% : VX_CPU_FAMILY = ppc
jdgTask/$(MODE_DIR)/% : CPU = PPC603
jdgTask/$(MODE_DIR)/% : TOOL_FAMILY = gnu
jdgTask/$(MODE_DIR)/% : TOOL = gnu
jdgTask/$(MODE_DIR)/% : TOOL_PATH = 
jdgTask/$(MODE_DIR)/% : CC_ARCH_SPEC = -mcpu=603 -mstrict-align -mno-implicit-fp
jdgTask/$(MODE_DIR)/% : LIBPATH = 
jdgTask/$(MODE_DIR)/% : LIBS = 
jdgTask/$(MODE_DIR)/% : OBJ_DIR := jdgTask/$(MODE_DIR)

jdgTask/$(MODE_DIR)/Objects/jdgTask/lib_socket.o : C:/WindRiver/workspace/jdgTask/lib_socket.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


jdgTask/$(MODE_DIR)/Objects/jdgTask/lib_util.o : C:/WindRiver/workspace/jdgTask/lib_util.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


jdgTask/$(MODE_DIR)/Objects/jdgTask/sock_utility.o : C:/WindRiver/workspace/jdgTask/sock_utility.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


jdgTask/$(MODE_DIR)/Objects/jdgTask/sys_error.o : C:/WindRiver/workspace/jdgTask/sys_error.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


jdgTask/$(MODE_DIR)/Objects/jdgTask/telnet_server.o : C:/WindRiver/workspace/jdgTask/telnet_server.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


OBJECTS_jdgTask = jdgTask/$(MODE_DIR)/Objects/jdgTask/lib_socket.o \
	 jdgTask/$(MODE_DIR)/Objects/jdgTask/lib_util.o \
	 jdgTask/$(MODE_DIR)/Objects/jdgTask/sock_utility.o \
	 jdgTask/$(MODE_DIR)/Objects/jdgTask/sys_error.o \
	 jdgTask/$(MODE_DIR)/Objects/jdgTask/telnet_server.o

jdgTask/$(MODE_DIR)/jdgTask.out : $(OBJECTS_jdgTask)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@";rm -f "$@";nmppc $(OBJECTS_jdgTask) $(IDE_LIBRARIES) | tclsh $(WIND_BASE)/host/resource/hutils/tcl/munch.tcl -c ppc > $(OBJ_DIR)/ctdt.c; $(TOOL_PATH)ccppc $(DEBUGFLAGS_Linker) $(CC_ARCH_SPEC) -fdollars-in-identifiers -Wall $(ADDED_CFLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES)  -o $(OBJ_DIR)/ctdt.o -c $(OBJ_DIR)/ctdt.c; $(TOOL_PATH)ccppc -r -nostdlib -Wl,-X -T $(WIND_BASE)/target/h/tool/gnu/ldscripts/link.OUT -o "$@" $(OBJ_DIR)/ctdt.o $(OBJECTS_jdgTask) $(IDE_LIBRARIES) $(LIBPATH) $(LIBS)  $(ADDED_LIBPATH) $(ADDED_LIBS) && if [ "$(EXPAND_DBG)" = "1" ]; then plink "$@";fi

jdgTask/$(MODE_DIR)/jdgTask_compile_file : $(FILE) ;

_clean :: jdgTask/$(MODE_DIR)/jdgTask_clean

jdgTask/$(MODE_DIR)/jdgTask_clean : 
	$(TRACE_FLAG)if [ -d "jdgTask" ]; then cd "jdgTask"; rm -rf $(MODE_DIR); fi

DEP_FILES := jdgTask/$(MODE_DIR)/Objects/jdgTask/lib_socket.d jdgTask/$(MODE_DIR)/Objects/jdgTask/lib_util.d jdgTask/$(MODE_DIR)/Objects/jdgTask/sock_utility.d \
	 jdgTask/$(MODE_DIR)/Objects/jdgTask/sys_error.d jdgTask/$(MODE_DIR)/Objects/jdgTask/telnet_server.d
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
