# from .forms import loginviews


# def post_comment(request, blog_id):
#    if request.method == 'POST':
#        form = CommentForm(request.POST)
#        if form.is_valid():
#            data = form.cleaned_data
#            blog = get_object_or_404(Blog, id=blog_id)
#            Comment.objects.create(
#                blog = blog,
#                name = data.name
#                email = data.email
#                text = data.text
#                date = timezone.now()
#            )