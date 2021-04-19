"""Command line entry points (exec file)
"""
import sys

from PySide2.QtWidgets import QApplication

from .gui import calc_main


def foo_run():
    """ Prints unicorm.
    """
    print(r"""
       .,,.
     ,;;*;;;;,
  |\.-'``;-');;.
  |/'  .-.  /*;;
 .'    \d    \;;               .;;;,
/ o      `    \;    ,__.     ,;*;;;*;,
\__, _.__,'   \_.-') __)--.;;;;;*;;;;,
 `""`;;;\       /-')_) __)  `\' ';;;;;;
    ;*;;;        -') `)_)  |\ |  ;;;;*;
    ;;;;|        `---`    O | | ;;*;;;
    *;*;\|                 O  / ;;;;;*
   ;;;;;/|    .-------\      / ;*;;;;;
  ;;;*;/ \    |        '.   (`. ;;;*;;;
  ;;;;;'. ;   |          )   \ | ;;;;;;
  ,;*;;;;\/   |.        /   /` | ';;;*;
   ;;;;;;/    |/       /   /__/   ';;;
   '*jgs/     |       /    |      ;*;
        `\"""`        `\"""`     ;'""")


def run():
    app = QApplication([])
    widget = calc_main()
    widget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
