from playAudio import playAudio
playAudio('update.mp3')
import supervisor
supervisor.set_next_code_file('code.py')
supervisor.reload()
