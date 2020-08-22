# creating a function for saving an object to a file
def save_pickle (self, filename=None):
    ''' takes an object variable as `self` and a file name
    as `filename`; saves the object as a serialized file
    in the `data` subdirectory
    '''
    import os
    import pickle
    # making a pickles directory, if it does not exist
    try:
        if not os.path.exists('pickles'):
            os.mkdir('pickles')
    except:
        print("directory 'pickles' already exists")
        pass

    print("-"*15, f"PICKLING {filename}", "-"*25)
    with open(f'pickles/{filename}', 'wb') as filename:
        pickle.dump(self, filename, pickle.HIGHEST_PROTOCOL)
    print("Saved as ", filename, "\n")
