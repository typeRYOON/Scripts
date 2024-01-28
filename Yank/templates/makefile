NAME01 = main

ifeq ($(OS),Windows_NT)
	RM = del /f
	CLS = cls
else
	RM = rm -f
	CLS = clear
endif

b: c
	@g++ -std=c++23 -O2 -Wall $(NAME01).cpp -o $(NAME01).exe

c:
	@$(RM) $(NAME01).exe;

r:
	@$(CLS)
	@./$(NAME01).exe
