from django.urls import path, include
from app.views.home import home
from app.views.spills_over_time import spills_over_time
from app.views.spill_events_map import spill_events_map
from app.views.oil_trade_flows import oil_trade_flows
from app.views.spills_cost_analysis import spills_cost_analysis
from app.views.ajax import choropleth_data, cause_categories
from app.views.reserves import get_reserves_by_year

urlpatterns = [
    path('', home, name='home'),
    # path("__reload__/", include("django_browser_reload.urls")),
    path('spills-over-time/', spills_over_time, name='spills_over_time'),        
    path('spill-events-map/', spill_events_map, name='spill_events_map'),    
    path('oil-trade-flows/', oil_trade_flows, name='oil_trade_flows'),        
    path('spills-cost-analysis/', spills_cost_analysis, name='spills_cost_analysis'),            
    path("ajax/choropleth-data/", choropleth_data, name="choropleth_data"),
    path('ajax/cause-categories/', cause_categories, name='cause_categories'),
    path('reserves_by_year/', get_reserves_by_year, name='reserves_by_year'),     
]