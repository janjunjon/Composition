import os
import sys
import subprocess

class Execution:
    @classmethod
    def main(cls, path, savedir):
        files = os.listdir(path)
        for file in files:
            filepath = '{}/{}'.format(path, file)
            filename = cls.combineStr(file)
            command = "ffmpeg -i \"{}\" -vn -ac 2 -ar 44100 -ab 256k -acodec libmp3lame -f mp3 \"{}/{}.mp3\"".format(
                filepath, savedir, filename
            )
            print(command)
            subprocess.run(command, shell=True)

    @classmethod
    def combineStr(cls, file):
        strs = file.split('.')
        if len(strs) > 2:
            strs.pop(-1)
            filename = ''
            for i in range(len(strs)):
                if i == 0:
                    filename += '{}'.format(strs[i])
                else:
                    filename += '.{}'.format(strs[i])
        else:
            filename = strs[0]
        return filename

