from datetime import datetime
import time

'''
Get A Character 
https://stackoverflow.com/questions/510357/how-to-read-a-single-character-from-the-user
'''


class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty
        import sys

    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getChar = _Getch()

'''
Business casual is an ambiguously defined dress code that has been adopted by many professional \
and white-collar workplaces in Western countries. It entails neat yet casual attire and is \
generally more casual than informal attire but more formal than casual or smart casual attire. \
Casual Fridays preceded widespread acceptance of business casual attire in many offices.
'''

paragraph = '''Business casual is an ambiguously defined dress code that has been adopted by many professional and white-collar workplaces in Western countries. It entails neat yet casual attire and is generally more casual than informal attire but more formal than casual or smart casual attire. Casual Fridays preceded widespread acceptance of business casual attire in many offices.'''


def recordTyping(paragraph):
    print('Starting the record process...')
    print('Total words: {}'.format(len(paragraph.split())))
    time.sleep(1)
    print('Starting in 3s')
    time.sleep(1)
    print('Starting in 2s')
    time.sleep(1)
    print('Starting in 1s')
    time.sleep(1)
    print('Started!')
    timeChar = list()
    start = datetime.now()
    timeChar.append(start)
    for ch in paragraph:
        print('>>', ch)
        while True:
            inCh = getChar().decode('utf-8')
            if (inCh == ch):
                stop = datetime.now()
                timeChar.append(stop)
                break

    return timeChar


def makeDigraph(paragraph, timeChar):
    digraph = dict()

    return digraph


if __name__ == '__main__':
    timeChar = recordTyping(paragraph)
    makeDigraph(paragraph, timeChar)
