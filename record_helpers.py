import datetime

def create_wav_file_name():
    """Create a .wav filename with the current date and time
    
    Returns:
        string -- the filename
    
    Example:
    './data/2019-06-30 15:25:50.034163.wav'
    """
    return "./data/" + str(datetime.datetime.now()) + ".wav"
