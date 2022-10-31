from Process.Convert import Execution as ConvertExecution

def main(path, savedir):
    ConvertExecution.main(path, savedir)

if __name__ == '__main__':
    # main(sys.argv[-1])
    path = '/mnt/c/Users/juntaro ishihara/Music/cubase/j.j.thomson/test'
    savedir = '/mnt/c/Users/juntaro ishihara/Music/cubase/j.j.thomson/mp3'
    main(path, savedir)