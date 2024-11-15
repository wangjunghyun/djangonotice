from django.shortcuts import render, get_object_or_404, redirect
from .models import noticedb
from django.utils import timezone

def notice_list(request):
    # すべてのお知らせを最新順に並べ替えて持ってくる
    notices = noticedb.objects.all().order_by('-publishDate')
    return render(request, 'notice_board/list.html', {'notice_list': notices})

def parse_date(date_string):
    date_string = date_string.replace('/', '-')  # 슬래시를 하이픈으로 변환
    return date_string

def notice_register(request):
    if request.method == 'POST':
        # POSTリクエストによりお知らせ登録処理
        title = request.POST['title']
        contents = request.POST['contents']
        publishType = request.POST.get('release_type')
        pushType = request.POST['push_notification']

        publishDate = parse_date(request.POST.get('issue_date'))
        expiryDate = parse_date(request.POST.get('expiry_date'))

        if publishType == 'h':
            publishDate = timezone.now()
            expiryDate = timezone.now()
        elif publishType == 'i':
            publishDate = timezone.now()

        if len(title) != 0 and len(contents) != 0 and expiryDate != ""  and publishDate != "":
            # 新しいお知らせオブジェクト作成後に保存
            new_notice = noticedb(
                title=title,
                contents=contents,
                publishType=publishType,
                pushType=pushType,
                publishDate=publishDate,
                expiryDate=expiryDate
            )
            new_notice.save()

            return redirect('notice_success')  # 成功ページへ移動

    return render(request, 'notice_board/register.html')

def notice_page(request, notice_id):
    # お知らせ詳細ページ
    notice = get_object_or_404(noticedb, pk=notice_id)
    return render(request, 'notice_board/page.html', {'notice': notice})

def notice_success(request):
    # お知らせ登録/修正済みページ
    return render(request, 'notice_board/success.html')

def notice_rewrite(request, notice_id):
    #お知らせ事項IDを基盤にデータをもたらす
    notice = get_object_or_404(noticedb, pk=notice_id)

    if request.method == 'POST':
        # POSTリクエストの場合、修正されたデータを保存
        notice.title = request.POST['title']
        notice.contents = request.POST['contents']
        notice.publishType = request.POST.get('release_type')
        notice.pushType = request.POST['push_notification']
        notice.publishDate = parse_date(request.POST.get('issue_date'))
        notice.expiryDate = parse_date(request.POST.get('expiry_date'))

        if notice.publishType == 'h':
            notice.publishDate = timezone.now()
            notice.expiryDate = timezone.now()
        elif notice.publishType == 'i':
            notice.publishDate = timezone.now()


        if len(notice.title) != 0 and len(notice.contents) != 0 and notice.expiryDate != "" and notice.publishDate != "":
            notice.save()  # 修正された内容を保存
            return redirect('notice_success')  # 成功ページへ移動

    # GET 요청일 경우 수정 폼을 반환
    return render(request, 'notice_board/rewrite.html', {'notice': notice})
