import time as t

def ask_ok(prompt, retries = 4, reminder = "Please try again"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        
        retries -= 1
        if retries < 0:
            raise ValueError('invalid user response')

        print(reminder)

def parrot(voltage, state = "a stiff", action = "voom", type = "Norwegian Blue"):
    print("-- This is parrot wouldn't ", action, end = " ")

def main():
    print('你好 Python')
    print(t.time())
    local_time = t.localtime(t.time())  # convert time to time tuple through timestamp.
    print(local_time.tm_year)
    ft_time = t.strftime("%Y-%M-%d %H:%M:%S", t.localtime())
    print(ft_time)

    a = "Sat Mar 28 22:24:24 2016"
    ts_time = t.mktime(t.strptime(a, "%a %b %d %H:%M:%S %Y"))
    print(ts_time)

    sum = lambda arg1, arg2: arg1 + arg2   # lambda expression to create function
    print(sum(1, 2))

    fo = open("Users\\sucong\\Desktop\\Test.txt", "w")
    fo.write("Clever.S noted this")
    print(fo.name)
    fo.close()
main()