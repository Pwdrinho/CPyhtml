from package.graphics import Monitor
import os



def workspace():

    sistema = Monitor()
    sistema.iniciar()




if __name__ == "__main__":

    workspace()
    os.system('rm -rf package/__pycache__')
