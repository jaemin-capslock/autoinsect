import requests
import os

try :
    os.mkdir(r"E:/insect_dataset/vespa_mandarinia")
except OSError:
    print ("target directory already exists.")


f = open(r"E:/insect_dataset/urls/vespa_mandarinia_url.txt", 'r')
new_data_list = []
for line in f:
    x = line[:line.find("/n")]
    new_data_list.append(x)


# %%

def load_requests(source_url, sink_path):
    """
    Load a file from an URL (e.g. http).

    Parameters
    ----------
    source_url : str
        Where to load the file from.
    sink_path : str
        Where the loaded file is stored.
    """

    with open(sink_path, 'wb') as handle:
        response = requests.get(source_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)




def load_dataset(data, ind):
    ##data_index = str(data.loc[ind])
    ###if "Name" in data_single_line:
    ##data_single_line = str(data_single_line[:data_single_line.find("Name")])

    return data[ind]


def download_images(data, dir):
    row_count = len(data)
    for l in range(row_count):

        download_dir = dir + str(1 + l) + ".jpg"
        load_requests(load_dataset(data, l), download_dir)
        if l % 10 == 0:
            print(str(l) + " th download initiated")


# %%




directory = r"E:/insect_dataset/vespa_mandarinia/hornet"

##print(load_dataset(test_data,1))
download_images(new_data_list, directory)