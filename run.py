import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'INTERFAZ'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'LOGICA'))

from INTERFAZ import main

if __name__ == "__main__":
    main.run()
