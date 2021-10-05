import argparse
import sys

def main():
    if (len(sys.argv)-1 == 0):
         print("Please enter parameter as add | update | list | delete")
         quit()
    parser = argparse.ArgumentParser()
    parser.add_argument('function', type=str, help='function to call')
    args = parser.parse_args()
    if (args != ""):
        try:  
            eval(args.function)()
        except:
          print("Please enter parameter as add | update | list | delete")

def add():
    print("called add function")

def update():
    print("called update function")
    delete()
    add()

def list():
    print("called list function")

def delete():
    print("called delete function")

if __name__ == '__main__':
    main()
