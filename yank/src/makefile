NAME = yank

ifeq ($(OS), Windows_NT)
	RM = del /f
	CLS = cls
else
	RM = rm -f
	CLS = clear
endif

b: c
	@g++ -std=c++20 -O2 -Wall $(NAME).cpp -o $(NAME).exe

c:
	@$(RM) $(NAME).exe;

r:
	@$(CLS)
	@./$(NAME).exe