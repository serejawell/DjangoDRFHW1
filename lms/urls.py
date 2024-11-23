from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.views import CourseViewSet, LessonListAPIView, LessonRetrieveAPIView, LessonCreateAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, SubscriptionView
from lms.apps import LmsConfig

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  # lessons
                  path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
                  path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
                  path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
                  path('lessons/<int:pk>/update', LessonUpdateAPIView.as_view(), name='lesson-update'),
                  path('lessons/<int:pk>/delete', LessonDestroyAPIView.as_view(), name='lesson-delete'),
                  # subscription
                  path('subscription/', SubscriptionView.as_view(), name='subscription'),

              ] + router.urls
