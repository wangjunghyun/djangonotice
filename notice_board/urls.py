from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice_list, name='notice_list'),  # お知らせリスト
    path('new/', views.notice_register, name='notice_register'),  # お知らせ登録
    path('re/<int:notice_id>/', views.notice_rewrite, name='notice_rewrite'),  # お知らせ事項の修正
    path('page/<int:notice_id>/', views.notice_page, name='notice_page'),  # お知らせ詳細ページ
    path('success/', views.notice_success, name='notice_success'),  # 成功ページ
]
