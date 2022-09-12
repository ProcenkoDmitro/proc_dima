from dataclasses import replace
from pathlib import Path
import os
#BASE_DIR = "/Users/proce/Desktop/Хламіщє_тест/"
translit = {
    'а': 'a', 'А': 'A',
    'б': 'b', 'Б': 'B',
    'в': 'v', 'В': 'V',
    'г': 'g', 'Г': 'G',
    'ґ': 'g', 'Ґ': 'G',
    'д': 'd', 'Д': 'D',
    'е': 'e', 'Е': 'E',
    'є': 'ye', 'Є': 'Ye',
    'ж': 'j', 'Ж': 'J' ,
    'з': 'z', 'З': 'Z',
    'и': 'i', 'И': 'I',
    'і': 'i', 'І': 'I',
    'ї': 'yi', 'Ї': 'Yi',
    'й': 'y', 'Й': 'Y',
    'к': 'k', 'К': 'K',
    'л': 'l', 'Л': 'L',
    'м': 'm', 'М': 'M',
    'н': 'n', 'Н': 'N',
    'о': 'o', 'О': 'O',
    'п': 'p', 'П': 'P',
    'р': 'r', 'Р': 'R',
    'с': 's', 'С': 'S',
    'т': 't', 'Т': 'T',
    'у': 'u', 'У': 'U',
    'ф': 'f', 'Ф': 'F',
    'х': 'h', 'Х': 'H',
    'ц': 'c', 'Ц': 'C',
    'ч': 'ch', 'Ч': 'Ch',
    'ш': 'sh', 'Ш': 'Sc',
    'щ': 'sch', 'Щ': 'Sch',
    'ь': '',
    'ю': 'yu', 'Ю': 'Yu',
    'я': 'ya', 'Я': 'Ya'
}

def normalize(name_file):
    norm_name = ""
    for key in translit:
        name_file = name_file.replace(key, translit[key])
    for i in name_file:
        if not i.isnumeric() and not i.isalpha():
            norm_name = norm_name + "_"            
        else:
            norm_name = norm_name + i
    return norm_name   

p = Path('/Users/proce/Desktop/Хламіщє_тест/')

def sorting(dir):
    images_path = dir + "images"
    videos_path = dir + "videos"
    docs_path = dir + "docs"
    musics_path = dir + "musics"
    zips_path = dir + "zips"
    not_recognize_path = dir + "not_recognize"

    if not os.path.exists(images_path):
        os.makedirs(images_path)
    if not os.path.exists(videos_path):
        os.makedirs(videos_path)
    if not os.path.exists(docs_path):
        os.makedirs(docs_path)
    if not os.path.exists(musics_path):
        os.makedirs(musics_path)
    if not os.path.exists(zips_path):
        os.makedirs(zips_path)
    if not os.path.exists(not_recognize_path):
        os.makedirs(not_recognize_path)
    
    for i in os.listdir(dir):    
        norm_name = normalize(os.path.splitext(i)[0])
        #print(norm_name)
        old_name = os.path.join(dir, i)
        new_name = os.path.join(dir, norm_name + os.path.splitext(i)[1])
        #print(old_name)
        #print(new_name)
        os.rename(old_name, new_name)

    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        if file_path.endswith( '.jpg') or file_path.endswith( '.png') or file_path.endswith( '.png') or file_path.endswith( '.svg') or file_path.endswith( '.jfif') or file_path.endswith( '.gif'):
            new_file = os.path.join(images_path, file)
            os.replace(file_path, new_file)
        elif file_path.endswith( '.avi') or file_path.endswith( '.mp4') or file_path.endswith( '.mov') or file_path.endswith( '.mkv'):
            new_file = os.path.join(videos_path, file)
            os.replace(file_path, new_file)
        elif file_path.endswith( '.doc') or file_path.endswith( '.docx') or file_path.endswith( '.txt') or file_path.endswith( '.pdf') or file_path.endswith( '.xlxs') or file_path.endswith( '.pptx'):
            new_file = os.path.join(docs_path, file)
            os.replace(file_path, new_file)
        elif file_path.endswith( '.mp3') or file_path.endswith( '.ogg') or file_path.endswith( '.wav') or file_path.endswith( '.amr'):
            new_file = os.path.join(musics_path, file)
            os.replace(file_path, new_file)
        elif file_path.endswith( '.zip') or file_path.endswith( '.gz') or file_path.endswith( '.tar'):
            new_file = os.path.join(zips_path, file)
            os.replace(file_path, new_file)
        elif os.path.isfile(dir + file):
            new_file = os.path.join(not_recognize_path, file)
            os.replace(file_path, new_file)
        #elif os.path.isdir(dir + file):
            #if file != 'docs' and file != 'images' and file != 'videos' and file != 'musics' and file != 'not_recognize' and file != 'zips':
                #sorting(dir + file)   
    

BASE_DIR = str(input())
sorting(BASE_DIR)