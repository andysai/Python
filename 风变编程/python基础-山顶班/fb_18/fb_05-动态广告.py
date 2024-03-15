import os, time
def main():
    msg = '立即下斑,禁止痘留!'
    while True:
        os.system('clear')
        print(msg)
        msg = msg[1:] + msg[0]
        time.sleep(1)

if __name__ == '__main__':
    main()