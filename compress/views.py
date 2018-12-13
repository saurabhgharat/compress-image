import magic
import os
from django.shortcuts import render,redirect
from .models import Compress,CompressedImage
from .forms import ImageForm
from django.views.generic import TemplateView,View
from django.http import HttpResponse
from image_compression.settings import BASE_DIR
from PIL import Image


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('compress:image_compress')
    else:
        form = ImageForm()
    return render(request, 'compress/model_form_upload.html', {
        'form': form
    })

def compress_image(request):
    img=Compress.objects.latest('id')

    im=Image.open(img.image.path,"r")
    # if im.mode in ("RGBA", "P"):
    #     im = im.convert("RGB")

    pix_val = list(im.getdata())  # get pixel value in RGB format

    a= [x for sets in pix_val for x in sets] #Convert list of tuples into one list

    myRoundedList =  [round(x,-1) for x in a]  #Round integers to nearest 10
    if im.mode in("RGBA","p"):
        b=[tuple(myRoundedList[i:i+4]) for i in range(0, len(myRoundedList), 4)]  #Group list to a tuple of 4 integers
    elif im.mode in("RGB"):
        b=[tuple(myRoundedList[i:i+3]) for i in range(0, len(myRoundedList), 3)]   #Group list to a tuple of 3 integers
    list_of_pixels = list(b)

    new_image= Image.new(im.mode, im.size) #Create a new image

    new_image.putdata(list_of_pixels) #input image data into the new image
    image_name="new_r"+img.image.name.split('/')[-1]

    image_path=os.path.join(BASE_DIR,'media/generated_images/'+image_name)

    if im.mode in("RGBA","p"):
        new_image.save(image_path,"PNG")
    elif im.mode in("RGB"):
        new_image.save(image_path,"JPEG")
    compressedimage=CompressedImage()
    compressedimage.new_compressed_image=os.path.join('generated_images/'+image_name)
    compressedimage.save()
    generated_compress_image=CompressedImage.objects.latest('id')
    return render(request,'compress/compress_image.html',{'img':img,"generated_compress_image":generated_compress_image})

class ImageDownloadView(View):

    def get(self, request, *args, **kwargs):
        selected_image = CompressedImage.objects.latest('id')
        image_buffer = open(selected_image.new_compressed_image.path, "rb").read()
        content_type = magic.from_buffer(image_buffer, mime=True)
        response = HttpResponse(image_buffer, content_type=content_type);
        response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(selected_image.new_compressed_image.path)
        return response
