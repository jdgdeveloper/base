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
PRJ_ROOT_DIR := C:/WindRiver/workspace/jdgFinalTask
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

IDE_INCLUDES = -I$(WIND_BASE)/target/h -I$(WIND_BASE)/target/h/wrn/coreip -I$(WIND_BASE)/target/h/WPILib -IC:/WindRiver/workspace/jdgFinalTask 

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
PROJECT_TARGETS = jdgFinalTask/$(MODE_DIR)/jdgFinalTask.out


#Rules

# jdgFinalTask
ifeq ($(DEBUG_MODE),1)
jdgFinalTask/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -g
jdgFinalTask/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -g
jdgFinalTask/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -g
jdgFinalTask/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
jdgFinalTask/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
jdgFinalTask/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -g
else
jdgFinalTask/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -O2 -fstrength-reduce -fno-builtin
jdgFinalTask/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -O2 -fstrength-reduce -fno-builtin
jdgFinalTask/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -O2 -fstrength-reduce -fno-builtin
jdgFinalTask/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
jdgFinalTask/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
jdgFinalTask/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -O2 -fstrength-reduce -fno-builtin
endif
jdgFinalTask/$(MODE_DIR)/% : IDE_INCLUDES = -I$(WIND_BASE)/target/h -I$(WIND_BASE)/target/h/wrn/coreip -I$(WIND_BASE)/target/h/WPILib -IC:/WindRiver/workspace/jdgFinalTask 
jdgFinalTask/$(MODE_DIR)/% : IDE_LIBRARIES = $(WIND_BASE)/target/lib/WPILib.a 
jdgFinalTask/$(MODE_DIR)/% : PROJECT_TYPE = DKM
jdgFinalTask/$(MODE_DIR)/% : DEFINES = 
jdgFinalTask/$(MODE_DIR)/% : EXPAND_DBG = 0
jdgFinalTask/$(MODE_DIR)/% : VX_CPU_FAMILY = ppc
jdgFinalTask/$(MODE_DIR)/% : CPU = PPC603
jdgFinalTask/$(MODE_DIR)/% : TOOL_FAMILY = gnu
jdgFinalTask/$(MODE_DIR)/% : TOOL = gnu
jdgFinalTask/$(MODE_DIR)/% : TOOL_PATH = 
jdgFinalTask/$(MODE_DIR)/% : CC_ARCH_SPEC = -mcpu=603 -mstrict-align -mno-implicit-fp
jdgFinalTask/$(MODE_DIR)/% : LIBPATH = 
jdgFinalTask/$(MODE_DIR)/% : LIBS = 
jdgFinalTask/$(MODE_DIR)/% : OBJ_DIR := jdgFinalTask/$(MODE_DIR)

jdgFinalTask/$(MODE_DIR)/Objects/jdgFinalTask/libSocket.o : C:/WindRiver/workspace/jdgFinalTask/libSocket.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


jdgFinalTask/$(MODE_DIR)/Objects/jdgFinalTask/libUtil.o : C:/WindRiver/workspace/jdgFinalTask/libUtil.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


jdgFinalTask/$(MODE_DIR)/Objects/jdgFinalTask/mainTask.o : C:/WindRiver/workspace/jdgFinalTask/mainTask.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


jdgFinalTask/$(MODE_DIR)/Objects/jdgFinalTask/telnetServer.o : C:/WindRiver/workspace/jdgFinalTask/telnetServer.cpp
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


OBJECTS_jdgFinalTask = jdgFinalTask/$(MODE_DIR)/Objects/jdgFinalTask/libSocket.o \
	 jdgFinalTask/$(MODE_DIR)/Objects/jdgFinalTask/libUtil.o \
	 jdgFinalTask/$(MODE_DIR)/Objects/jdgFinalTask/mainTask.o \
	 jdgFinalTask/$(MODE_DIR)/Objects/jdgFinalTask/telnetServer.o

jdgFinalTask/$(MODE_DIR)/jdgFinalTask.out : $(OBJECTS_jdgFinalTask)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@";rm -f "$@";nmppc $(OBJECTS_jdgFinalTask) $(IDE_LIBRARIES) | tclsh $(WIND_BASE)/host/resource/hutils/tcl/munch.tcl -c ppc > $(OBJ_DIR)/ctdt.c; $(TOOL_PATH)ccppc $(DEBUGFLAGS_Linker) $(CC_ARCH_SPEC) -fdollars-in-identifiers -Wall $(ADDED_CFLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES)  -o $(OBJ_DIR)/ctdt.o -c $(OBJ_DIR)/ctdt.c; $(TOOL_PATH)ccppc -r -nostdlib -Wl,-X -T $(WIND_BASE)/target/h/tool/gnu/ldscripts/link.OUT -o "$@" $(OBJ_DIR)/ctdt.o $(OBJECTS_jdgFinalTask) $(IDE_LIBRARIES) $(LIBPATH) $(LIBS)  $(ADDED_LIBPATH) $(ADDED_LIBS) && if [ "$(EXPAND_DBG)" = "1" ]; then plink "$@";fi

jdgFinalTask/$(MODE_DIR)/jdgFinalTask_compile_file : $(FILE) ;

_clean :: jdgFinalTask/$(MODE_DIR)/jdgFinalTask_clean

jdgFinalTask/$(MODE_DIR)/jdgFinalTask_clean : 
	$(TRACE_FLAG)if [ -d "jdgFinalTask" ]; then cd "jdgFinalTask"; rm -rf $(MODE_DIR); fi

DEP_FILES := jdgFinalTask/$(MODE_DIR)/Objects/jdgFinalTask/libSocket.d jdgFinalTask/$(MODE_DIR)/Objects/jdgFinalTask/libUtil.d jdgFinalTask/$(MODE_DIR)/Objects/jdgFinalTask/mainTask.d \
	 jdgFinalTask/$(MODE_DIR)/Objects/jdgFinalTask/telnetServer.d
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
