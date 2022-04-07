from django.shortcuts import render
from .models import Author
from .forms import PostForm
from django.shortcuts import redirect


def authors_list(request):
    context = {'authors_list': Author.objects.all()}
    return render(request, 'author/authors_List.html', context)


def author_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('authors_list')
    else:
        form = PostForm()
    return render(request, 'author/author_create.html', {'form': form})


def author_delete(request, a_id):
    try:
        author = Author.objects.get(id=a_id)
        author.delete()
    except Author.DoesNotExist:
        # LOGGER.error("User does not exist")
        pass
    return redirect('authors_list')


def author_update(request, a_id):
    if request.method == "POST":
        author = Author.objects.get(id=a_id)
        form = PostForm(request.POST, instance=author)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('authors_list')
    else:
        author = Author.objects.get(id=a_id)
        form = PostForm(instance=author)
    return render(request, 'author/author_create.html', {'form': form})
