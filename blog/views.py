from django.shortcuts import get_object_or_404,render
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from django.contrib.contenttypes.models import ContentType

from blog.models import Blog,BlogType
from read_statistics.utils import read_statistics_once_read
from comment.models import Comment
from comment.forms import CommentForm


def get_blog_list_common_data(request, blog_all_list):
    paginator = Paginator(blog_all_list,settings.NUMBER_OF_BLOG_IN_EACH_PAGE)
    page_num = request.GET.get('page',1) #获取url请求的页面参数值（GET请求，参数是page，？page=N,N是page的值）
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number #获取当前页
    #获取当前页面前后各两页的范围
    page_range = list(range(max(current_page_num - 2,1),current_page_num))+\
                 list(range(current_page_num, min(current_page_num +2,paginator.num_pages)+1))
    #加上省略号
    if page_range[0] - 1 >= 2:
        page_range.insert(0,"...")
    if page_range[-1] +2 <= paginator.num_pages:
        page_range.append("...")
    #加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    #获取博客分类对应的博客数量,方法1（将blog_count作为blog_type的属性来实现）
    # blog_types = BlogType.objects.all()
    # blog_type_list = []
    # for blog_type in blog_types:
    #     blog_type.blog_count = Blog.objects.filter(blog_type=blog_type).count()
    #     blog_type_list.append(blog_type)
    # context['blog_types'] = blog_type_list

    #获取博客分类对应的博客数量,方法2
    # BlogType.objects.annotate(blog_count=Count('blog'))

    #获取日期归档对应的博客数量
    blog_dates = Blog.objects.dates('created_time','month',order='DESC') #基于创建时间的“月份”来Group聚合出创建时间，按时间倒序排列
    # print(blog_dates)
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year,created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count


    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))
    context['blog_dates'] = blog_dates_dict
    return context

def blog_list(request):
    blog_all_list = Blog.objects.all()
    print(blog_all_list)
    context = get_blog_list_common_data(request,blog_all_list)
    return render(request,'blog/blog_list.html',context)

def blog_with_type(request,blog_type_pk):
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request,blogs_all_list)
    context['blog_type'] = blog_type

    return render(request,'blog/blog_with_type.html',context)

def blogs_with_date(request,year,month):
    blogs_all_list = Blog.objects.filter(created_time__year=year,created_time__month=month)
    # print(blogs_all_list) debug调试，打印日志看为什么mysql获取不到year\month的过滤
    context = get_blog_list_common_data(request,blogs_all_list)
    context['blogs_with_date'] = "%s年%s月" %(year,month)
    return render(request,'blog/blog_with_date.html',context)

def blog_detail(request,blog_pk):
    # 以blog_pk为主键值，在Blog类中取出实例，并赋值给变量blog
    blog = get_object_or_404(Blog,pk=blog_pk)
    read_cookie_key = read_statistics_once_read(request,blog)
    blog_content_type = ContentType.objects.get_for_model(blog)
    comments = Comment.objects.filter(content_type=blog_content_type,object_id=blog.pk,parent=None)

    context = {}
    context['blog'] = blog
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['comments'] = comments.order_by('-comment_time')
    context['comment_form'] = CommentForm(initial={'content_type':blog_content_type.model,
                                                   'object_id':blog_pk,'reply_comment_id':0})
    response = render(request,'blog/blog_detail.html',context)
    response.set_cookie(read_cookie_key,'true') #阅读cookie标记
    return response