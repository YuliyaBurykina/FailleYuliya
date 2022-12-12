def status_working(func):
    def _wrapper():
        print("vv")
        func()
        print("GG")
    return _wrapper

@bot.message_handler()
def something():
    for i in range(10):
         print(i + 1)
something()