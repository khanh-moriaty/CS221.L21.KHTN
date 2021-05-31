import json
import os
import unicodedata

def process(dataset, max_timespan=60*60*1000):
    '''
    Group mpz's messages into conversations.
    Messages that are less than 60 minutes apart from each other is grouped into one.
    
    Parameters:
        - dataset: loaded from load_facebook_dataset()
        - max_timespan: maximum time between mpz's messages. Default: 60 minutes.
    
    Returns: List of conversations.
    '''
    groups = []
    messages = dataset['messages']
    p1 = p2 = last = 0
    while p1 < len(messages):
        while p2 < len(messages) and messages[p2]['timestamp_ms'] - messages[last]['timestamp_ms'] <= max_timespan:
            if messages[p2]['is_mpz']: last = p2
            p2 += 1
        if messages[last]['is_mpz']:
            groups.append((p1, p2))
        last = p1 = last+1
        
    messages_list = set()
    conversations = []
    for i, group in enumerate(groups):
        conversations.append({
            'id': i,
            'conversation': list(range(group[0], group[1]))),
        })
        for id in range(group[0], group[1]):
            messages_list.add(id)
            
    return {
        "conversations": conversations,
        "messages": [messages[id] for id in messages_list],
    }
        
def load_facebook_dataset(dir_path='messages/'):
    '''
    Loads Facebook message dataset from Dirty messenger group 
    and attempts to merge messages from all json files together.
    
    Parameters:
        - dir_path: path to a directory containing json files.
    
    Returns: a dictionary representing json object in the following format:
        - participants: list.
        - messages: list. sorted ascending by time.
            + sender_name: str.
            + timestamp_ms: int.
            + content: latin-1 encoded str.
            + type: 'Generic' or 'Share'.
            + is_unsent: bool.
            + is_mpz: bool.
            + num_{photos|gifs|videos|audios|files}: number of medias.
            + is_sticker: if this is a sticker.
            + id: int.
        - title: str.
        - is_still_participant: bool.
        - thread_type: str.
        - thread_path: str.
        - magic_words: list.
    '''
    dataset = None
    dir = os.listdir(dir_path)
    dir = [fn for fn in dir if fn.endswith('.json')]
    dir.sort()
    for fn in dir:
        with open(os.path.join(dir_path, fn), 'r') as fi:
            messages = json.load(fi)
        if not dataset: # If this is the first json read: init.
            dataset = messages
        else: # Else attempts to merge.
            dataset['messages'] += messages['messages']
    
    # Sorts messages ascending by time.
    dataset['messages'].sort(key = lambda message: message['timestamp_ms'])
    # Generate id and is_mpz for messages
    for id, message in enumerate(dataset['messages']):
        message['is_mpz'] = (message['sender_name'] == 'Minh Ph\u00c6\u00b0\u00c6\u00a1ng')
        message['num_photos'] = len(message['photos']) if 'photos' in message else 0
        message['num_gifs'] = len(message['gifs']) if 'gifs' in message else 0
        message['num_videos'] = len(message['videos']) if 'videos' in message else 0
        message['num_audios'] = len(message['audio_files']) if 'audio_files' in message else 0
        message['num_files'] = len(message['files']) if 'files' in message else 0
        message['is_sticker'] = ('sticker' in message)
        if 'content' not in message: message['content'] = ''
        message['content'] = unicodedata.normalize('NFC', message['content'].encode('latin-1').decode('utf-8'))
        message['sender_name'] = unicodedata.normalize('NFC', message['sender_name'].encode('latin-1').decode('utf-8'))
        message['id'] = id
        
    # Remove empty messages and not generic-type messages
    dataset['messages'] = [message for message in dataset['messages'] if message['content'] and message['type'] == 'Generic']
    
    return dataset
    

if __name__ == '__main__':
    dataset = load_facebook_dataset()
    conversations = process(dataset)
    with open('conversations.json', 'w', encoding='utf-8') as fo:
        json.dump(conversations, fo, indent=4)
