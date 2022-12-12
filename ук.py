import keyboard
a = int(input("цифра: ", ))
n = int(input("повторение: ", ))
for i in range(n): 
  keyboard.add_hotkey('w', command=print(a))

keyboard.wait("e")