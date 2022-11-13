import threading
import requests
import queue
import pathlib
import os
import time

start = time.perf_counter()

destination = os.path.abspath(str(pathlib.Path(__file__).parent) + '\\' + 'Photos')
# creates a folder if missing.
if not os.path.exists(destination):
    os.mkdir(destination)

que_obj = queue.Queue()
# dict of api names and keys format: api_name => link
# standart picture size: width => 2000 / height => 2000
photo_api = { 
    'lorem_space' : 'https://api.lorem.space/image?w=2000&h=2000',
    "Lorem Picsum" : 'https://picsum.photos/2000/2000',
    'Unsplash' : "https://source.unsplash.com/2000x2000" # slow and not recommended to use.
}

def random_image_put(q_instance,t_tag):
    r = requests.get(photo_api['lorem_space'])
    img_bin_data = r.content
    print(f'i finished thread # => {t_tag}')
    q_instance.put(img_bin_data)


def create_pic(q_instance):
    name_num = -1
    while True:
        name_num +=1
        img_bin_data = q_instance.get()
        with open(destination + '\\' + str(name_num) + '.jpg', 'wb+') as file:
            file.write(img_bin_data)

getter_threads = []

for num in range(11):
    t_get = threading.Thread(target= random_image_put , args=(que_obj, num))
    getter_threads.append(t_get)
    t_get.start()

t_create = threading.Thread(target=create_pic, args=(que_obj,), daemon = True)
t_create.start()

for t in getter_threads:
    t.join()

stop = time.perf_counter()

print(f'Finished script in {round(stop-start, 2)}')
t_create.join(timeout=0.5) # this allows the daemon thread to block one last before terminating application.