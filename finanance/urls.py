from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

# FactFr
    path('factsFr/<int:pk>/update/', views.FactFrUpdateView.as_view(), name='factFr_update'),
    path('factFr/<int:pk>/delete/', views.FactFrDeleteView.as_view(), name='delete_factFr'),
    path('factFr/', views.factFr, name='factFr'),
    path('create_factFr/', views.FactFrCreateView.as_view(), name='create_factFr'),
    
# FactCl
    path('factCl/<int:pk>/update/', views.FactClUpdateView.as_view(), name='factCl_update'),
    path('factCl/<int:pk>/delete/', views.FactClDeleteView.as_view(), name='delete_factCl'),
    path('factCl/', views.factCl, name='factCl'),
    path('create_fact/', views.FactClCreateView.as_view(), name='create_factCl'),
   
# Note
    path('note/<int:pk>/update/', views.NoteUpdateView.as_view(), name='note_update'),
    path('note/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='delete_note'),
    path('notes/', views.notes, name='notes'),
    path('create_note/', views.NoteCreateView.as_view(), name='create_note'),
   
# Client
    path('client/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='delete_client'),
    path('clientList/', views.clientList, name='clientList'),
    path('create_client/', views.ClientCreateView.as_view(), name='create_client'),
# Prod
    path('prod/<int:pk>/update/', views.ProdUpdateView.as_view(), name='prod_update'),
    path('prod/<int:pk>/delete/', views.ProdDeleteView.as_view(), name='delete_prod'),
    path('produits/', views.produits, name='produits'),
    path('create_prod/', views.ProdCreateView.as_view(), name='create_prod'),
   
# Fournisseurs
    path('fourn/<int:pk>/update/', views.FournUpdateView.as_view(), name='fourn_update'),
    path('fours/<int:pk>/delete/', views.FournDeleteView.as_view(), name='delete_fourn'),
    path('foursList/', views.foursList, name='foursList'),
    path('create_fours/', views.FoursCreateView.as_view(), name='create_fours'),


    path('GL/', views.GL, name='GL'),
    path('journaux/', views.Journaux, name='journaux'),
    
# Paiements
    path('paiments/', views.Paiments, name='paiments'),
    path('paiments/<int:pk>/update/', views.PaiementUpdateView.as_view(), name='pie_update'),
    path('paiment/<int:pk>/delete/', views.PaiementDeleteView.as_view(), name='delete_pie'),
    path('create_pie/', views.PaiementCreateView.as_view(), name='create_pie'),
# Ecritures Comptable
    path('ecriture/', views.EcritureComp, name='ecriture'),
    path('ecrit/<int:pk>/update/', views.EcritUpdateView.as_view(), name='ecrit_update'),
# Pieces
    path('piece/<int:pk>/update/', views.PieceUpdateView.as_view(), name='piece_update'),
    path('piece/<int:pk>/delete/', views.PieceDeleteView.as_view(), name='delete_piece'),
    path('pieces/', views.Pieces, name='pieces'),
    path('create_piece/', views.PieceCreateView.as_view(), name='create_piece'),
    
# Graph
    path('factures_graphique/', views.factures_graphique, name='factures_graphique'),
    path('facturesFr_graphique/', views.facturesFr_graphique, name='facturesFr_graphique'),

] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
