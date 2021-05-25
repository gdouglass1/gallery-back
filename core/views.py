from django.shortcuts import render, redirect, get_object_or_404
from .models import GalleryImg, Comments
from django.contrib import messages


def index(request):

    if request.method == 'POST':
        img = request.FILES['image']

        if img != '':
            gallery_db = GalleryImg(image=img)
            gallery_db.save()
            msg = "New image has been added!"
            messages.success(request, msg)
            return redirect('galleryIndex')
        else:
            msg = "There is something wrong!"
            messages.warning(request, msg)
            return redirect('galleryIndex')

    # grab all the images from database
    images_from_db = GalleryImg.objects.all()

    context = {
        'images' : images_from_db,
    }
    return render(request, 'front-end/index.html', context)


def image_details(request, pk):

    #grab single image
    img_detail = get_object_or_404(GalleryImg, pk=pk)

    if request.method == 'POST':
        comment = request.POST.get('comment')

        if comment != '':
            comments = Comments(comment=comment, img=img_detail)
            comments.save()
            return redirect('galleryImgDetails', pk=pk)


    #grab all comments
    cmmnts = Comments.objects.all()

    context = {
        'img'     : img_detail,
        'pk'      : pk,
        'comments': cmmnts,
    }

    return render(request, 'front-end/image_details.html', context)


