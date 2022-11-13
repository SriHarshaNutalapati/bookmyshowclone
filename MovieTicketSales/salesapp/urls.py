from django.urls import path

from . import views

urlpatterns = [
    path('', views.customerHome, name='customerHome'),
    path('customerhome', views.customerHome, name='customerHome'),
    path('theatrehome', views.theatreHome, name='theatreHome'),
    path('signup', views.userSignUp, name='userSignUp'),
    path('userlogin', views.userLogin, name='userLogin'),
    path('profile', views.changeUserProfile, name='changeUserProfile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('addtheatre', views.addTheatre, name='addTheatre'),
    path('addMovieShow', views.addMovieShow, name='addMovieShow'),
    path('getTheatres', views.getTheatres, name='getTheatres'),
    path('getAvailableSeats', views.getAvailableSeats, name='getAvailableSeats'),
    path('initiateBooking', views.initiateBooking, name='initiateBooking'),
    path('bookingSummary/<slug:bookingid>', views.bookingSummary, name='bookingSummary'),
    path('confirmBooking', views.confirmBooking, name='confirmBooking'),
    path('purchasehistory', views.purchasehistory, name='purchasehistory'),
    path('userPaymentInfo', views.userPaymentInfo, name='userPaymentInfo'),
    path('viewticketsales', views.viewticketsales, name='viewticketsales'),
    path('viewticketsalesondate', views.viewticketsalesondate, name='viewticketsalesondate'),
    path('viewtheatres', views.viewtheatres, name='viewtheatres'),
    path('viewticketsalesadmin', views.viewticketsalesadmin, name='viewticketsalesadmin'),
    path('viewcustomers', views.viewcustomers, name='viewcustomers'),
    path('appsettings', views.appsettings, name='appsettings'),
    path('viewshows', views.viewshows, name='viewshows'),
    path('cancelshow', views.cancelshow, name='cancelshow'),
    path('addmovie', views.addmovie, name='addmovie'),
    path('archiveuser', views.archiveuser, name='archiveuser'),
]