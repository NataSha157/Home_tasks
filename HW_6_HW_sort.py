import sys, pathlib, os, shutil

new_folders = ['archives', 'audio', 'documents', 'images', 'unknown', 'video'] # Назви папок, що створяться
end_docs = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', '.odt', '.rtf', '.xml', '.docm', '.dot', '.dotx',
           '.ott', '.uot', '.fodt', '.doc#', '.DOC', '.PDF'] # Перелік розширень папки 'documents'
end_images = ['.jpeg', '.png', '.jpg', '.svg'] # Перелік розширень папки 'images'
end_videos = ['.avi', '.mp4', '.mov', '.mkv'] # Перелік розширень папки 'video'
end_audios = ['.mp3', '.ogg', '.wav', '.amr'] # Перелік розширень папки 'audio'
end_archives = ['.zip', '.gz', '.tar'] # Перелік розширень папки 'archives'


res_docs = [] # Перелік файлів в кінцевій папці 'documents'
res_images = [] # Перелік файлів в кінцевій папці 'images'
res_unknowns = [] # Перелік файлів в кінцевій папці 'unknown'
res_videos = [] # Перелік файлів в кінцевій папці 'video'
res_audios = [] # Перелік файлів в кінцевій папці 'audio'
res_archives = [] # Перелік файлів в кінцевій папці 'archives'
end_sort_direct = []  # Перелік усіх відомих скрипту розширень, які зустрічаються в цільовій папці
end_unknowns = []  # Перелік розширень папки 'unknown'

def translit(leter: str) -> str:  # Приймає символ, повертає латинський, з урахуванням регістру, або цифру, або '_'
    alphabet_cyrillic = ('а','б','в','г','ґ','д','е','є','ж','з','и','і','ї','й','к','л','м','н','о','п','р','с',
                         'т','у','ф','х','ц','ч','ш','щ','ю','я', 'А','Б','В','Г','Ґ','Д','Е','Є','Ж','З','И','І',
                         'Ї','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ю','Я')
    alphabet_latin = ('a','b','v','h','g','d','e','ie','zh','z','y','i','i','i','k','l','m','n','o','p','r','s',
                      't','u','f','kh','ts','ch','sh','shch','iu','ia', 'A','B','V','H','G','D','E','Ye','Zh','Z','Y',
                      'I','Yi','Y','K','L','M','N','O','P','R','S','T','U','F','Kh','Ts','Ch','Sh','Shch','Yu','Ya')
    dict_translit = dict(zip(alphabet_cyrillic, alphabet_latin))
    leter_latin = []
    for i in range(65, 91):
        leter_latin.append(chr(i))
    for i in range(97, 123):
        leter_latin.append(chr(i))
    if leter in alphabet_cyrillic:
        return dict_translit[leter]
    elif leter in leter_latin or leter in '0123456789':
        return leter
    else:
        return '_'

def mk_dir(new_name: str): # Створює папку за str-адресою
    new_dir = pathlib.Path(new_name)
    new_dir.mkdir(parents=True, exist_ok=False)

def normalize(name: str) -> str: # Перейменовує строку
    new_name = ''
    for symbol in name:
        new_name += translit(symbol)
    return new_name

def parse_recursion(path: pathlib.Path):
    for i in path.iterdir():
        if i.is_dir(): #Папки не перейменовуємо, бо вони видаляютьсям
            parse_recursion(i)
            if len(os.listdir(i)) == 0:
                os.rmdir(i)
        else:
            file_name = i.stem
            file_name_new = str(i.parent) + '\\' + normalize(file_name) + i.suffix
            a = pathlib.Path(i.rename(file_name_new))
            if a.suffix in end_docs: # Переміщення до відповідної папки
                new_path_folder = pathlib.Path('D:' + '\\' + new_folders[2] + '\\' + a.name)
                if not pathlib.Path(new_path_folder).exists():
                    b = a.rename(new_path_folder)
                    res_docs.append(b.name)
                    end_sort_direct.append(b.suffix)
                else:
                    print('Файл з такою назвою вже існує', new_path_folder)
            elif a.suffix in end_images:
                new_path_folder = pathlib.Path('D:' + '\\' + new_folders[3] + '\\' + a.name)
                if not pathlib.Path(new_path_folder).exists():
                    b = a.rename(new_path_folder)
                    res_images.append(b.name)
                    end_sort_direct.append(b.suffix)
                else:
                    print('Файл з такою назвою вже існує', new_path_folder)
            elif a.suffix in end_videos:
                new_path_folder = pathlib.Path('D:' + '\\' + new_folders[5] + '\\' + a.name)
                if not pathlib.Path(new_path_folder).exists():
                    b = a.rename(new_path_folder)
                    res_videos.append(b.name)
                    end_sort_direct.append(b.suffix)
                else:
                    print('Файл з такою назвою вже існує', new_path_folder)
            elif a.suffix in end_audios:
                new_path_folder = pathlib.Path('D:' + '\\' + new_folders[1] + '\\' + a.name)
                if not pathlib.Path(new_path_folder).exists():
                    b = a.rename(new_path_folder)
                    res_audios.append(b.name)
                    end_sort_direct.append(b.suffix)
                else:
                    print('Файл з такою назвою вже існує', new_path_folder)
            elif a.suffix in end_archives:
                new_path_folder = pathlib.Path('D:' + '\\' + new_folders[0] + '\\' + a.name)
                if not pathlib.Path(new_path_folder).exists():
                    b = a.rename(new_path_folder)
                    res_archives.append(b.name)
                    end_sort_direct.append(b.suffix)
                    new_path_archive_folder = pathlib.Path('D:' + '\\' + new_folders[0] + '\\' + a.stem)
                    shutil.unpack_archive(b, new_path_archive_folder)
                else:
                    print('Файл з такою назвою вже існує', new_path_folder)
            else:
                new_path_folder = pathlib.Path('D:' + '\\' + new_folders[4] + '\\' + a.name)
                if not pathlib.Path(new_path_folder).exists():
                    b = a.rename(new_path_folder)
                    res_unknowns.append(b.name)
                    end_sort_direct.append(b.suffix)
                    end_unknowns.append(b.suffix)
                else:
                    print('Файл з такою назвою вже існує', new_path_folder)


# створюємо папки для подальшого сортування
def create_folder (path):
    for folder in new_folders: # Створення папок в кореневому каталозі D:\
        path_folder = 'D:' + '\\' + folder
        if not pathlib.Path(path_folder).exists():
            mk_dir(path_folder)
            print(f'Нова папка: {path_folder}')
        else:
            print(f"Папка {path_folder} вже існує, сортуватимемо в неї")
    parse_recursion(path)
    os.rmdir(path)
    print('Перелік усіх розширень, що зустрічались при роботі скрипта', set(end_sort_direct))
    print("Перелік усіх розширень, які скрипту не відомі", set(end_unknowns))
    print("Перелік файлів в кінцевій папці 'documents'", res_docs)
    print("Перелік файлів в кінцевій папці 'images'", res_images)
    print("Перелік файлів в кінцевій папці 'video'", res_videos)
    print("Перелік файлів в кінцевій папці 'audio'", res_audios)
    print("Перелік файлів в кінцевій папці 'archives'", res_archives)
    print("Перелік файлів в кінцевій папці 'unknown'", res_unknowns)


def main():
    arg = sys.argv[1]
    path = pathlib.Path(arg)
    create_folder(path)

if __name__ == '__main__':
    main()





