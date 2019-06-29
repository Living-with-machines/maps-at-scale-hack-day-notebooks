import image_slicer
from PIL import Image
from tqdm import tqdm
from pathlib import Path
import glob
import concurrent.futures

Image.MAX_IMAGE_PIXELS = None

p = Path("/Volumes/Work/multi-label").rglob('*.tif')
images = [x for x in p if x.is_file()]
 
for image in tqdm(images):
    fname = Path(image).stem
    tiles = image_slicer.slice(image, 4, save=False)
    image_slicer.save_tiles(tiles, prefix=fname, format='jpeg')


def read_files(path, extension):
    return glob.glob(f'{path}.{extension}')

    # Restrict file size to 1000KB
def file_size(image):
    statinfo = os.stat(image)
    file_size = statinfo.st_size
    return file_size

# restrict file size to 1000kb
def resize_image(image):
    f_name = Path(image).stem
    out_file = f_name + "_CB" + ".jpg"
    im = Image.open(image).convert('L')
    im.save(out_file, quality=15, optimize=True, progressive=True)

# Process the list of files, but split the work across the process pool to use all CPUs!

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        image_files = glob.glob("test/0227/*.jp2")    
        result = executor.map(resize_image, image_files)
        
