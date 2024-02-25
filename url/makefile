# Build Command  ::
BUILD   = g++ -std=c++23 -O2 -Wall
EXE     = url.exe

# Source Files   ::
SRC-01  = url.cpp
SRC     = $(SRC-01)

# Platform Check ::
ifeq ($(OS), Windows_NT)
	RM = del /f
	CLS = cls
else
	RM = rm -f
	CLS = clear
endif

# Build Target   ::
b: c
	@$(BUILD) $(SRC) -o $(EXE)

# Clean Target   ::
c:
	@$(RM) $(EXE);

# Run Target     ::
r:
	@$(CLS)
	@./$(EXE)